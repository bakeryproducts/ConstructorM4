from PyQt4 import QtGui
from PyQt4 import QtOpenGL
from PyQt4 import QtCore
import numpy as np
from OpenGL.GL import *
import mathutils as mth
import time

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import CNST.techs as techs
import CNST.clGEOOBJ as clGEOOBJ
from CNST.draw import getmv  # TODO go from draaw to techs
from CNST.draw import drawinbuf, sph, drawpic,newpic,multiget,multiset

from PIL import Image,ImageOps

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
        self.planesize=1000

        self.draftpoint = (0, 0, 0)
        self.setMouseTracking(True)
        self.ObjSelected = techs.Signal()
        self.RulerChange = techs.Signal()
        self.AngleChange = techs.Signal()
        self.key=None
        self.scalefree=1
        self.font = QtGui.QFont()
        self.font.setPointSize(14)
        self.fontscale = QtGui.QFont()
        self.fontscale.setPointSize(12)

        self.textlist=[]
        self.textconsole = []
        self.timer=False
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

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
                #del(obj)

    def sphinit(self,r=5,col=(0,0,1)):
        self.sphlist=glGenLists(1)
        glNewList(self.sphlist, GL_COMPILE)
        r = r / self.scalefree
        if self.sphcdlist:
            glColor3f(*col)
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
        w,h = self.wi,self.he
        yofs = 10
        p0,p1,p2 = (0,yofs-h/2,10000),(w/4,yofs-1*h/2,10000),(w/2-5,yofs-h/2,10000)
        self.rulerlist = glGenLists(1)
        glNewList(self.rulerlist, GL_COMPILE)

        thickness = GLfloat(10)
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
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

        self.qglClearColor(self.color)
        self.lineinit()
        self.axisinit()
        self.sphinit()

        self.planecdinit()
        self.planeinit()
        self.gridcdinit()
        self.gridinit()

        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        #glEnable(GL_CULL_FACE)

        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_DEPTH_TEST)
        # glLightfv(GL_LIGHT0, GL_POSITION, (-.3, .6, 1))

        mat_specular = GLfloat_4(1.0, 1.0, 1.0, 1.0)
        mat_shininess = GLfloat(80)
        # light_position[] = {1.0, 1.0, 1.0, 0.0};
        glShadeModel(GL_SMOOTH)

        glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
        glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

        glLightfv(GL_LIGHT0, GL_POSITION, (-1,1,1))
        cAmbientLight = GLfloat_4(0.4, 0.4, 0.4, .5)
        glLightfv(GL_LIGHT0, GL_AMBIENT, cAmbientLight)
        cDiffuseLight = GLfloat_4(1,1,1,.01)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, cDiffuseLight)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

        glEnable(GL_NORMALIZE)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.drawruler()
        self.drawaxis()
        self.drawsph()
        self.drawline()
        self.drawcross()
        self.drawtext()
        self.drawtextscale()
        glLoadIdentity()

        opacitylist = [(i,obj,obj.getopa()) for i,obj in enumerate(self.objects)]
        sortedopalist = sorted(opacitylist,key = lambda t:t[2])
        sortedobj = [(p[0],p[1]) for p in reversed(sortedopalist)]

        for i,object in sortedobj:
            if i not in self.invisiblelist:
                for objid, planeid in self.selection:
                    object.showplane(planeid, objid)
                object.show()

        # self.drawplane()
        # self.drawgrid()

    def resizeGL(self, width, height):
        self.wi = width
        self.he = height
        self.rulerinit()
        self.crossinit()

        self.FBO = techs.fbufinit(self.wi, self.he)
        self.PBOS,self.pbosize = techs.pbosinit(self.wi, self.he)

        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-width / 2, width / 2, -height / 2, height / 2, -10000,10000)#-15000, 15000)
        glMatrixMode(GL_MODELVIEW)

    def mousePressEvent(self, event):
        self.lastPos = event.pos()  # onPress and onRelease produces same events!?
        self.pos = (event.x(), event.y())
        # self.sph = (self.pos[0] - self.wi / 2, self.he / 2 - self.pos[1], 0)

    def getpic(self):
        clrarr=[]
        deparr = []
        for obj in self.objects:
            objclr,objdep = drawpic(obj,self.FBO,self.wi,self.he)
            # objclrnp = np.frombuffer(objclr,np.uint8,count=self.wi*self.he*4)
            # objclrnp = objclrnp.reshape((self.wi, self.he, 4))
            clrarr.append(objclr)
            deparr.append(objdep)
        return clrarr,deparr,self.wi,self.he

    from PIL import Image
    def modpic(self,ind,obj):
        data = newpic(obj, self.PBOS[ind], self.wi, self.he,self.pbosize,ind)
        objclrnp = np.frombuffer(data,np.uint8,count=self.wi*self.he*4)
        data = objclrnp.reshape((self.wi, self.he, 4))

        # imgc = Image.frombytes("RGBA", (self.wi, self.he), data)
        # #imgc = ImageOps.flip(imgc)
        # imgc.save('RESULTS\\PBOTEST'+str(ind)+'.png', 'PNG')
        return data

    def writepic(self,ind,obj):
        ind=0
        multiset(obj, self.PBOS[ind], self.wi, self.he)

    def readpic(self,ind):
        #ind=0
        data = multiget(self.PBOS[0], self.pbosize)
        objclrnp = np.frombuffer(data,np.uint8,count=self.wi*self.he*4)
        # data = objclrnp.reshape((self.he,self.wi, 4))
        # data = np.flipud(data)

        # img = Image.fromarray(data, 'RGBA')
        # img.save('RESULTS\\obj'+str(ind)+'.png', 'PNG')
        return np.flipud(objclrnp.reshape((self.he,self.wi, 4)))#data


    def mouseReleaseEvent(self, event):
        if (event.x(), event.y()) == self.pos:
            objid, planeid = drawinbuf(self.objects, self.FBO, self.revmouse,self.invisiblelist)
            pair = objid, planeid
            if objid!=255:
                if self.mode == "pickmany":
                    self.ObjSelected.register(pair)
                    if pair not in self.selection:
                        self.selection.append(pair)
                        self.addtoconsole('Added to selection:'+str(len(self.selection))+' elements')
                    else:
                        self.selection.remove(pair)
                        self.addtoconsole('Removed from selection:' + str(len(self.selection)) + ' elements')

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
        #self.textlist=[[str(round(self.scalefree,2)),0]]
        #self.addtoconsole('test'+str(self.scalefree))
        self.upmat()

    def mouseMoveEvent(self, event):
        self.revmouse = (event.pos()).x(), self.he - (event.pos()).y()

        if event.buttons() == QtCore.Qt.LeftButton:
            self.rotx = event.x() - self.lastPos.x()
            self.roty = event.y() - self.lastPos.y()
            self.lastPos = event.pos()
            self.upmat()
            los = (0,0,1,0)
            multlos = np.matmul(self.mvMatrix, los)[:3]
            ang1 = techs.getangle((0,1,0),multlos)
            # print(ang1,np.cos(ang1*np.pi/180))
            ang2 = techs.getangle(los[:3],multlos*np.sin(ang1*np.pi/180)),
            # print(*ang2)
            self.AngleChange.register((ang1,*ang2))

        elif event.buttons() == QtCore.Qt.RightButton:
            dx = event.x() - self.lastRPos.x()
            dy = event.y() - self.lastRPos.y()
            k = 1  # TODO get rid of k after all
            self.tr = k * dx, k * dy
            self.lastRPos = event.pos()
            self.upmat()
        else:
            self.lastRPos = event.pos()

        if self.key and self.mode=='pickmany':
            objid, planeid = drawinbuf(self.objects, self.FBO, self.revmouse, self.invisiblelist)
            pair = objid, planeid
            self.ObjSelected.register(pair)
            if objid!=255:
                if self.key=='ctrl':
                    #print('ctrl')
                    if pair not in self.selection:
                        self.selection.append(pair)
                        self.addtoconsole('Added to selection:' + str(len(self.selection)) + ' elements')
                elif self.key == 'alt':
                    try:
                        self.selection.remove(pair)
                        self.addtoconsole('Removed from selection:' + str(len(self.selection)) + ' elements')
                    except:
                        pass
                self.upmat()
        #self.upmat()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self.key = 'ctrl'
        elif event.key() == QtCore.Qt.Key_Alt:
            self.key = 'alt'
        else:
            self.key=None

    def keyReleaseEvent(self, event):
        self.key=None

    def upmat(self):
        self.mvMatrix = getmv(self.sc, self.tr, self.rotx, self.roty, self.mvMatrix)

        for object in self.objects:
            object.update(self.mvMatrix)

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
        #norm = object.normals[planeid-1]

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

    def lineinit(self,thick=10):
        self.linelist = glGenLists(1)
        glNewList(self.linelist, GL_COMPILE)
        if self.linecdlist:
            for line in self.linecdlist:
                p1,p2=line
                glPushMatrix()
                thickness = GLfloat(thick)
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
                thickness = GLfloat(1)
                glLineWidth(thickness)
                glBegin(GL_LINES)
                glColor3fv((.1, 0.5, 1))
                glVertex3fv(p1)
                glVertex3fv(p2)
                glEnd()
                glPopMatrix()
        glEndList()

    def crosscdinit(self):
        p1 = [-self.wi / 2, 0, 10000]
        p2 = [self.wi / 2, 0,  10000]
        p3 = [0, -self.he / 2, 10000]
        p4 = [0, self.he / 2,  10000]
        self.crosscdlist = [[p1, p2], [p3, p4]]

    def planeinit(self):
        self.planelist = glGenLists(1)
        glNewList(self.planelist, GL_COMPILE)
        if self.planecdlist:
            for plane in self.planecdlist:
                p1,p2,p3,p4 = plane
                glPushMatrix()
                #thickness = GLfloat(5)
                #glLineWidth(thickness)
                glBegin(GL_POLYGON)
                colp = 0.8
                glColor4fv((colp, colp, colp, .1))
                glVertex3fv(p1)
                #glColor4fv((colp, 0, 0, .1))
                glVertex3fv(p2)
                #glColor4fv((colp, colp, 0, .1))
                glVertex3fv(p3)
                #glColor4fv((0, colp, 0, .1))
                glVertex3fv(p4)
                glEnd()
                glPopMatrix()
        glEndList()

    def planecdinit(self):
        #l = 1000
        l = self.planesize
        p0 = [0,0,0]
        px = [l,0,0]
        py = [0,l,0]
        pz = [0,0,l]
        pxy = [l,l,0]
        pzx = [l,0,l]
        pzy = [0,l,l]
        self.planecdlist = [[p0,px,pzx,pz]]#[p0,px,pxy,py],[p0,py,pzy,pz]]

    def dropplane(self):
        self.planecdlist=[]
        self.planeinit()
        self.upmat()

    def drawplane(self):
        glDisable(GL_CULL_FACE)
        glPushMatrix()
        glMultMatrixf(self.mvMatrix)
        glCallList(self.planelist)
        glPopMatrix()
        glEnable(GL_CULL_FACE)

    def gridinit(self):
        self.gridlist = glGenLists(1)
        glNewList(self.gridlist, GL_COMPILE)
        if self.gridcdlist:
            for line in self.gridcdlist:
                p1, p2 = line
                glPushMatrix()
                thickness = GLfloat(4)
                glLineWidth(thickness)
                glBegin(GL_LINES)
                colp = 0.0
                glColor4fv((colp, colp, colp, .1))
                glVertex3fv(p1)
                glVertex3fv(p2)
                glEnd()
                glPopMatrix()
        glEndList()

    def gridcdinit(self):
        #l = 1000
        l = self.planesize
        nx,ny = 40,40
        dx,dy = l/nx,l/ny
        lines=[]
        jj=0
        for i in range(nx+1):
            p1=[i*dx,0,0]
            p2=[i*dx,0,l]
            lines.append([p1, p2])
        for j in range(ny+1):
            p1 = [0,0, j*dy]
            p2 = [l,0, j*dy]
            lines.append([p1, p2])

        self.gridcdlist = lines

    def dropgrid(self):
        self.gridcdlist = []
        self.gridinit()
        self.upmat()

    def drawgrid(self):
        glPushMatrix()
        glMultMatrixf(self.mvMatrix)
        glCallList(self.gridlist)
        glPopMatrix()

    def drawtext(self):
        off,a=0,0.25
        for s,p in self.textconsole:
            #self.textgen(s,p)
            self.texttoconsole(s,off,a)
            a*=2
            off+=30

    def droptext(self):
        self.strlist=[]
        self.upmat()

    def textgen(self,s='',pos=(0,0)):
        #s = 'Hello'
        glColor3f(.8,.8,1)
        #pos = -self.wi/2,-self.he/2
        self.renderText(*pos, 0, s, self.font)

    def drawtextscale(self):
        w, h = self.wi, self.he
        yofs = 20
        points = (0, yofs - h / 2), (w / 4-10, yofs - h / 2), (1 * w / 2-60, yofs- h / 2)
        pointst = w/4,w/2
        glColor3f(.2, .2, 0)
        self.renderText(*points[0], 0, '0', self.fontscale)
        for p,pt in zip(points[1:],pointst):
            self.renderText(*p, 0, str(round(pt/self.scalefree,1)), self.fontscale)

    def texttoconsole(self,s,offset=0,a=1):
        pos = (-self.wi / 2)*.95, (-self.he / 2)*.95+offset
        glColor4f(.2, .2, 0, a)
        self.renderText(*pos, 0, s, self.font)

    def addtoconsole(self,s):
        self.textconsole.append([s,0])
        if len(self.textconsole)>3:
            self.textconsole.pop(0)

    def act_btn_front(self):
        self.mvMatrix=np.identity(4)
        self.scalefree = 1

    def act_btn_right(self):
        self.mvMatrix = np.identity(4)
        self.scalefree = 1
        glPushMatrix()
        glLoadIdentity()
        glRotatef(-90, 0, 1, 0)
        mv = glGetDoublev(GL_MODELVIEW_MATRIX)
        #mv = np.transpose(mv)
        glPopMatrix()
        self.mvMatrix = mv

    def act_btn_left(self):
        self.mvMatrix = np.identity(4)
        self.scalefree = 1
        glPushMatrix()
        glLoadIdentity()
        glRotatef(90, 0, 1, 0)
        mv = glGetDoublev(GL_MODELVIEW_MATRIX)
        #mv = np.transpose(mv)
        glPopMatrix()
        self.mvMatrix = mv

    def act_btn_back(self):
        self.mvMatrix = np.identity(4)
        self.scalefree = 1
        glPushMatrix()
        glLoadIdentity()
        glRotatef(180, 0, 1, 0)
        mv = glGetDoublev(GL_MODELVIEW_MATRIX)
        #mv = np.transpose(mv)
        glPopMatrix()
        self.mvMatrix = mv

    def act_btn_top(self):
        self.mvMatrix = np.identity(4)
        self.scalefree = 1
        glPushMatrix()
        glLoadIdentity()
        glRotatef(90, 1, 0, 0)
        mv = glGetDoublev(GL_MODELVIEW_MATRIX)
        #mv = np.transpose(mv)
        glPopMatrix()
        self.mvMatrix = mv

    def act_btn_bottom(self):
        self.mvMatrix = np.identity(4)
        self.scalefree = 1
        glPushMatrix()
        glLoadIdentity()
        glRotatef(-90, 1, 0, 0)
        mv = glGetDoublev(GL_MODELVIEW_MATRIX)
        #mv = np.transpose(mv)
        glPopMatrix()
        self.mvMatrix = mv

    def dropui(self):
        self.dropplane()
        self.droplines()
        self.dropcross()
        self.dropgrid()
        self.droptext()

    def rot(self,anglex=1,angley=1):
        glPushMatrix()
        glLoadIdentity()
        glRotatef(anglex, 0, 1, 0)
        glMultMatrixf(self.mvMatrix)
        mv = glGetDoublev(GL_MODELVIEW_MATRIX)
        glLoadIdentity()
        glRotatef(angley, 1, 0, 0)
        glMultMatrixf(mv)
        mv = glGetDoublev(GL_MODELVIEW_MATRIX)
        glPopMatrix()
        self.mvMatrix = mv
        for object in self.objects:
            object.update(self.mvMatrix)

        self.updateGL()

        # if axis == 'x':
        #     self.rotx = anglex
        #     self.roty=0
        #     self.upmat()
        # elif axis == 'y':
        #     self.roty=angley
        #     self.rotx=0
        #     self.upmat()
        # elif axis=='xy':
        #     self.rotx = anglex
        #     self.mvMatrix = getmv(self.sc, self.tr, self.rotx, 0, self.mvMatrix)
        #     self.rotx=0
        #     self.roty = angley
        #     self.upmat()

    def rotp(self,angle,axis):
        glPushMatrix()
        glLoadIdentity()
        glRotatef(angle, *axis)
        glMultMatrixf(self.mvMatrix)
        mv = glGetDoublev(GL_MODELVIEW_MATRIX)
        glPopMatrix()
        self.mvMatrix = mv
        for object in self.objects:
            object.update(self.mvMatrix)

        self.updateGL()
