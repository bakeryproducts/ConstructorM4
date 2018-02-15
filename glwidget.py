from PyQt4 import QtGui
from PyQt4 import QtOpenGL
from PyQt4 import QtCore
import numpy as np
from OpenGL.GL import *
import mathutils as mth

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import CNST.techs as techs
import CNST.clGEOOBJ as clGEOOBJ
from CNST.draw import getmv  # TODO go from draaw to techs
from CNST.draw import drawinbuf, sph, drawpic


class GLWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)
        self.color = QtGui.QColor.fromCmykF(0.4, 0.21, 0.0, 0.0)
        self.rotx, self.roty = 0, 0
        self.mvMatrix = np.identity(4)
        self.sc, self.tr = 1, (0, 0)
        self.objects = []
        self.invisiblelist = []
        self.revmouse = 0, 0
        self.selection = []
        self.mode = "pick0"
        self.edgemode = 'on'
        self.axlist = 0
        self.rulerlist=0
        self.linecdlist=[]
        self.sphcdlist=[]
        self.crosscdlist=[]
        self.crosslist=0
        self.draftpoint = (0, 0, 0)
        self.setMouseTracking(True)
        self.ObjSelected = techs.Signal()
        self.RulerChange = techs.Signal()
        self.scalefree=1

    def addobj(self, obj):
        self.objects.append(obj)
        self.upmat()

    def addtmpobj(self,obj):
        #obj.setcol((*obj.defcol[:3],.8))
        obj.setopacity(.6)
        self.objects.append(obj)

    def cleartmpobjs(self):
        for obj in reversed(self.objects):
            if obj.getopa()==.6:
                self.objects.remove(obj)
                del(obj)

    def sphinit(self,r=10):
        self.sphlist=glGenLists(1)
        glNewList(self.sphlist, GL_COMPILE)
        if self.sphcdlist:
            for cd in self.sphcdlist:
                glPushMatrix()
                #glLoadIdentity()
                glTranslate(*cd)
                quad = gluNewQuadric()
                gluSphere(quad, r, 4, 4)
                glPopMatrix()
        glEndList()

    def axisinit(self):
        p0, p1, p2, p3 = (0, 0, 0), (100, 0, 0), (0, 100, 0), (0, 0, 100)

        self.axlist = glGenLists(1)
        glNewList(self.axlist, GL_COMPILE)

        thickness = GLfloat(4)
        glLineWidth(thickness)

        glBegin(GL_LINES)

        glColor3fv((1, 0, 0))
        glVertex3fv(p0)
        glVertex3fv(p1)

        glColor3fv((0, 1, 0))
        glVertex3fv(p0)
        glVertex3fv(p2)

        glColor3fv((0, 0, 1))
        glVertex3fv(p0)
        glVertex3fv(p3)

        glEnd()
        glEndList()

    def rulerinit(self):
        p0,p1,p2 = (self.wi/2,0,15000),(self.wi/2,self.he/2,15000),(self.wi/2,-self.he/2,15000)
        self.rulerlist = glGenLists(1)
        glNewList(self.rulerlist, GL_COMPILE)

        thickness = GLfloat(20)
        glLineWidth(thickness)

        glBegin(GL_LINES)
        glColor3fv((0,0,0))
        glVertex3fv(p0)
        glVertex3fv(p1)

        glColor3fv((1,1,1))
        glVertex3fv(p1)
        glVertex3fv(p2)
        glEnd()
        glEndList()

    def drawaxis(self):
        t = 1/self.scalefree
        glDisable(GL_LIGHTING)
        glPushMatrix()
        glMultMatrixf(self.mvMatrix)
        glScalef(t,t,t)
        glCallList(self.axlist)
        glPopMatrix()
        glEnable(GL_LIGHTING)

    def minimumSizeHint(self):
        return QtCore.QSize(50, 50)

    def sizeHint(self):
        return QtCore.QSize(400, 400)

    def initializeGL(self):
        self.qglClearColor(self.color)
        self.lineinit()
        self.axisinit()
        self.sphinit()
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_CULL_FACE)
        #glEnable(GL_POLYGON_STIPPLE)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        #glEnable(GL_LIGHT1)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_DEPTH_TEST)
        glLightfv(GL_LIGHT0, GL_POSITION, (-.3, .6, 1))
        glEnable(GL_NORMALIZE)

        #
        # cAmbientLight = GLfloat_4(0.5, 0.5, 0.5, 1.0)
        # glLightfv(GL_LIGHT1, GL_AMBIENT, cAmbientLight)
        #
        # cDiffuseLight = GLfloat_4(0.5, 0.5, 0.5, 1.0)
        # glLightfv(GL_LIGHT1, GL_DIFFUSE, cDiffuseLight)
        #
        # vLightPos = GLfloat_4(1, 3, 4, 1)
        # glLightfv(GL_LIGHT1, GL_POSITION, vLightPos);
        # glEnable(GL_LIGHT1)
        #
        # glEnable(GL_LIGHTING)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.drawruler()
        self.drawaxis()
        self.drawsph()
        self.drawline()
        self.drawcross()
        glLoadIdentity()

        #self.glut_print(10, 10, "Hallo World", 1.0, 1.0, 1.0, 1.0)

        opacitylist = [(i,obj,obj.getopa()) for i,obj in enumerate(self.objects)]
        sortedopalist = sorted(opacitylist,key = lambda t:t[2])
        sortedobj = [(p[0],p[1]) for p in reversed(sortedopalist)]

        for i,object in sortedobj:
            if i not in self.invisiblelist:
                for objid, planeid in self.selection:
                    object.showplane(planeid, objid)
                object.show()

    def resizeGL(self, width, height):
        self.wi = width
        self.he = height
        self.rulerinit()
        self.crossinit()
        self.FBO = techs.fbufinit(self.wi, self.he)

        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-width / 2, width / 2, -height / 2, height / 2, -15000, 15000)
        glMatrixMode(GL_MODELVIEW)

    def mousePressEvent(self, event):
        self.lastPos = event.pos()  # onPress and onRelease produces same events!?
        self.pos = (event.x(), event.y())
        # self.sph = (self.pos[0] - self.wi / 2, self.he / 2 - self.pos[1], 0)

    def getpic(self):
        picarr=[]
        for obj in self.objects:
            picarr.append(drawpic(obj,self.FBO,self.wi,self.he))
        return picarr,self.wi,self.he

    def mouseReleaseEvent(self, event):
        if (event.x(), event.y()) == self.pos:
            objid, planeid = drawinbuf(self.objects, self.FBO, self.revmouse,self.invisiblelist)
            pair = objid, planeid

            if self.mode == "pickmany":
                self.ObjSelected.register(pair)
                if pair not in self.selection:
                    self.selection.append(pair)
                else:
                    self.selection.remove(pair)
            elif self.mode == "pickone":
                if pair not in self.selection:
                    self.selection = [pair]
                    self.getint(*pair,self.pos)
                else:
                    self.selection.remove(pair)
            elif self.mode == "pickwhole":  # TODO oh this is ugly
                try:
                    if self.selection == []:
                        self.selection = [[objid, plid + 1] for plid in range(len(self.objects[0].faces))]
                    elif self.selection[0][0] != objid:
                        self.selection = [[objid, plid + 1] for plid in range(len(self.objects[0].faces))]
                    else:
                        self.selection = []
                except:
                    self.selection = []

            elif self.mode == "pick0":
                pass

        self.rotx, self.roty = 0, 0
        self.tr = 0, 0
        self.upmat()

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.sc = 1.05
        else:
            self.sc = 0.95
        self.scalefree *= self.sc
        #print(self.scalefree,self.he/self.scalefree)
        self.upmat()

    def mouseMoveEvent(self, event):
        self.revmouse = (event.pos()).x(), self.he - (event.pos()).y()

        if event.buttons() == QtCore.Qt.LeftButton:
            self.rotx = event.x() - self.lastPos.x()
            self.roty = event.y() - self.lastPos.y()
            self.lastPos = event.pos()

        if event.buttons() == QtCore.Qt.RightButton:
            dx = event.x() - self.lastRPos.x()
            dy = event.y() - self.lastRPos.y()
            k = 1  # TODO get rid of k after all
            self.tr = k * dx, k * dy
            self.lastRPos = event.pos()
        else:
            self.lastRPos = event.pos()

        self.upmat()

    def upmat(self):
        self.mvMatrix = getmv(self.sc, self.tr, self.rotx, self.roty, self.mvMatrix)
        try:
            for object in self.objects:
                object.update(self.mvMatrix)
        except:
            pass

        self.updateGL()
        self.sc = 1

    def addinvisible(self, components):
        try:
            for comp in components:
                index = self.getobjbyid(comp.getid())
                self.invisiblelist.append(index)
        except:
            pass
        self.upmat()

    def delinvisible(self, components):
        try:
            for comp in components:
                index = self.getobjbyid(comp.getid())
                self.invisiblelist.remove(index)
        except:
            pass

        self.upmat()

    def dropselection(self):
        self.selection = []
        self.upmat()

    def setselection(self, pair):
        self.selection = [pair]
        self.upmat()

    def getobjbyid(self, objid):
        for i, object in enumerate(self.objects):
            if objid == object.getid():
                return i

    def getint(self, objid, planeid, pos):
        '''sooo the thing is:
            1. gotta transpose MV if you tranlate things
            2. w=0/1 is important
            3. what is going on: getting plane(point and normal), go to world space coordinates
                then intersect plane with ray from mouse pick
                then go back to object space cd
        '''


        object = self.objects[self.getobjbyid(objid)]
        face = object.faces[planeid - 1]
        org = object.points[face[0] - 1]
        norm = object.getnormaltoface(planeid)

        px, py = pos
        px = px - self.wi/2
        py = self.he / 2 - py

        m = np.transpose(self.mvMatrix)
        org = np.matmul(m, (*org, 1))[:3]
        norm = np.matmul(m, (*norm, 0))[:3]

        line_a = mth.Vector((px, py, -1200))
        line_b = mth.Vector((px, py, 1200))
        ci = mth.geometry.intersect_line_plane(line_a, line_b, org, norm)
        m = np.linalg.inv(m)
        ci = np.matmul(m,(*ci,1))[:3]
        self.draftpoint = ci
        #self.sphcdlist=[ci]
        self.ObjSelected.register(((objid, planeid),ci))
        return list(ci)

    def dropsphs(self):
        self.sphcdlist=[]
        self.upmat()

    def drawsph(self):
        #t = 1 / self.scalefree
        glPushMatrix()
        glMultMatrixf(self.mvMatrix)
        glCallList(self.sphlist)
        glPopMatrix()

    def edgemodeswitch(self):
        flag = self.objects[0].fedge
        for obj in self.objects:
            obj.fedge = flag
            obj.edgeswitch()
        self.upmat()

    def drawruler(self):
        glDisable(GL_LIGHTING)
        glPushMatrix()
        glCallList(self.rulerlist)
        glPopMatrix()
        glEnable(GL_LIGHTING)

    def lineinit(self):
        self.linelist = glGenLists(1)
        glNewList(self.linelist, GL_COMPILE)
        if self.linecdlist:
            for line in self.linecdlist:
                p1,p2=line
                glPushMatrix()
                thickness = GLfloat(10)
                glLineWidth(thickness)
                glBegin(GL_LINES)
                glColor3fv((1, 0, 0))
                glVertex3fv(p1)
                glVertex3fv(p2)
                glEnd()
                glPopMatrix()
        glEndList()

    def droplines(self):
        self.linecdlist=[]
        self.lineinit()
        self.upmat()

    def drawline(self):
        glPushMatrix()
        glMultMatrixf(self.mvMatrix)
        glCallList(self.linelist)
        glPopMatrix()

    def drawcross(self):
        glPushMatrix()
        #glMultMatrixf(self.mvMatrix)
        glCallList(self.crosslist)
        glPopMatrix()

    def dropcross(self):
        self.crosscdlist=[]
        self.crossinit()
        self.upmat()

    def crossinit(self):
        self.crosslist = glGenLists(1)
        glNewList(self.crosslist, GL_COMPILE)
        if self.crosscdlist:
            for line in self.crosscdlist:
                p1, p2 = line
                glPushMatrix()
                thickness = GLfloat(5)
                glLineWidth(thickness)
                glBegin(GL_LINES)
                glColor3fv((.1, 0.5, 1))
                glVertex3fv(p1)
                glVertex3fv(p2)
                glEnd()
                glPopMatrix()
        glEndList()

    def crosscdinit(self):
        p1 = [-self.wi / 2, 0, 15000]
        p2 = [self.wi / 2, 0, 15000]
        p3 = [0, -self.he / 2, 15000]
        p4 = [0, self.he / 2, 15000]
        self.crosscdlist = [[p1, p2], [p3, p4]]


    # def glut_print(x, y, text, r, g, b, a):
    #
    #     glColor3f(1, 1, 1)
    #     glRasterPos2f(x, y)
    #     text = 'TEST'
    #     GL_Te
    #     for ch in text:
    #         glutBitmapCharacter(font, ctypes.c_int(ord(ch)))

