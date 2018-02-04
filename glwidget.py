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
        self.draftpoint = (0, 0, 0)
        self.sphcdlist=[]
        self.setMouseTracking(True)
        self.ObjSelected = techs.Signal()
        self.scalefree=1
    # def creobj(self, path):
    #     self.objname = path.split("/")[-1]
    #     #geos = techs.georedo(path, 100)
    #     geos = techs.georedo("C:\\Users\\User\PycharmProjects\CNSTgui\CNST\GEO\\dz.stl", 100)
    #     geoobj = clGEOOBJ.GEOOBJ(geos,self.objname)
    #     self.objects.append(geoobj)
    #     return geoobj

    def addobj(self, obj):
        self.objects.append(obj)

    def addtmpobj(self,obj):
        #obj.setcol((*obj.defcol[:3],.8))
        obj.setopacity(.6)
        self.objects.append(obj)

    def cleartmpobjs(self):
        for obj in reversed(self.objects):
            if obj.getopa()==.6:
                self.objects.remove(obj)
                del(obj)

    def sphinit(self):
        self.sphlist=glGenLists(1)
        glNewList(self.sphlist, GL_COMPILE)
        if self.sphcdlist:
            for cd in self.sphcdlist:
                glPushMatrix()
                #glLoadIdentity()
                glTranslate(*cd)
                quad = gluNewQuadric()
                gluSphere(quad, 10, 20, 20)
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
        # self.creobj("C:\\Users\\User\PycharmProjects\CNSTgui\CNST\GEO\\dz.stl")  # TODO DEL THIS
        self.qglClearColor(self.color)
        self.axisinit()
        self.sphinit()
        #glEnable(GL_CULL_FACE)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        #glEnable(GL_LIGHT1)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_DEPTH_TEST)
        glLightfv(GL_LIGHT0, GL_POSITION, (-.3, .6, 1))
        glEnable(GL_NORMALIZE)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
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
        self.drawaxis()
        self.drawsph()
        glLoadIdentity()
        try:
            for i, object in enumerate(self.objects):
                if i not in self.invisiblelist:
                    for objid, planeid in self.selection:
                        object.showplane(planeid, objid)
                    object.show()
        except:
            pass

    def resizeGL(self, width, height):
        self.wi = width
        self.he = height
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
        pic = drawpic(self.objects,self.FBO,self.wi,self.he)
        return pic,self.wi,self.he


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
        #glScalef(t, t, t)
        if self.sphcdlist:
            for cd in self.sphcdlist:
                sph(cd)
        glPopMatrix()

    def edgemodeswitch(self):
        flag = self.objects[0].fedge
        for obj in self.objects:
            obj.fedge = flag
            obj.edgeswitch()
        self.upmat()

