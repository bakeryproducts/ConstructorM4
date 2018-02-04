import CNST.techs as techs
from itertools import count
import numpy as np
from OpenGL.GL import *


class GEOOBJ:
    _ids = count(0)
    _arids = []

    def __init__(self, geometry, name):
        self.name = name
        self.points, self.faces, self.edges = [np.array(item) for item in geometry]
        self.fedge=True
        self.setid()

        self.origin = self.points[0]

        self.objlist = 0
        self.colors = techs.setcolors(self.id, len(self.faces))
        self.mvMatrix = np.identity(4)
        self.norm = np.array([0, 200, 0])

        self.col = (.7, .5, .3)
        self.defcol = self.col
        self.opa = 1
        self.defopa = self.opa

        self.makelist()

    def __del__(self):
        self._arids.remove(self.id)

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

    def setid(self):
        maxid = len(self._arids)
        for i in range(maxid):
            if i not in self._arids:
                self._arids.append(i)
                self.id=i
                return i
        self._arids.append(maxid)
        self.id = maxid
        return maxid

    def getid(self):
        return self.id

    def getcp(self):
        geo = self.points,self.faces,self.edges
        copy = GEOOBJ(geo, self.name)
        copy.col = self.col
        return copy

    def getstartpoint(self):
        return self.points[0]

    def getpoints(self):
        return self.points

    def getfaces(self):
        return self.faces

    def getedges(self):
        return self.edges

    def edgeswitch(self):
        self.fedge  = not self.fedge
        self.makelist()

    def setcol(self, maincolor):
        self.col = maincolor

    def getcol(self):
        return self.col

    def defcolset(self):
        self.col = self.defcol

    def getopa(self):
        return self.opa

    def setopacity(self,opa):
        self.opa = opa

    def defopacityet(self):
        self.opa = self.defopa

    def getcolors(self):
        return self.colors

    def stats(self):
        print(20 * "_" + "\nObjects id: %s\n %s points\n %s faces\n" % (
            self.id, len(self.points), len(self.faces)) + 20 * "_")

    def update(self, mvMatrix):
        self.mvMatrix = mvMatrix

    def makelist(self):
        self.objlist = glGenLists(1)
        glNewList(self.objlist, GL_COMPILE)
        self.draw()
        glEndList()

    def draw(self):
        for i, face in enumerate(self.faces):
            glBegin(GL_POLYGON)
            norm = self.getnormaltoface(i + 1)
            glNormal3fv(norm)
            for point in face:
                glVertex3fv(self.points[point - 1])
            glEnd()
        if self.fedge:
            edges = self.edges
            thickness = GLfloat(2)
            glLineWidth(thickness)
            glBegin(GL_LINES)
            glColor3fv((0, 0, 0))
            for edge in edges:
                for point in edge:
                    glVertex3fv(self.points[point - 1])
            glEnd()

    def show(self):
        glColor4fv((*self.col,self.opa))
        glPushMatrix()
        glLoadIdentity()
        glMultMatrixf(self.mvMatrix)
        glCallList(self.objlist)
        glPopMatrix()

    def showcolors(self):
        glDisable(GL_LIGHTING)
        glPushMatrix()
        glMultMatrixf(self.mvMatrix)
        for i, face in enumerate(self.faces):
            glBegin(GL_POLYGON)
            glColor3ub(*self.colors[i])
            for point in face:
                glVertex3fv(self.points[point - 1])
            glEnd()
        glPopMatrix()
        glEnable(GL_LIGHTING)

    def showplane(self, planeid, oid):
        if oid == self.id and planeid <= len(self.faces) and planeid > 0:
            glDisable(GL_LIGHTING)
            glColor3fv((0.4, 1, 0.2))
            glPushMatrix()
            glMultMatrixf(self.mvMatrix)
            #glBegin(GL_TRIANGLES)
            glBegin(GL_POLYGON)
            for point in self.faces[planeid - 1]:
                glVertex3fv(self.points[point - 1])
            glEnd()
            glPopMatrix()
            glEnable(GL_LIGHTING)
            return 1
        return 0

    def setcoord(self, pos, point=None):
        if point is None:
            point = self.points[0]
        glPushMatrix()
        glLoadIdentity()
        glTranslatef(*(-1 * point))
        glTranslatef(*pos[:3])
        mv = glGetDoublev(GL_MODELVIEW_MATRIX)
        mv = np.transpose(mv)
        glPopMatrix()
        newpoints = []
        for point in self.points:
            ipoint = np.matmul(mv, (*point, 1))
            newpoints.append(ipoint[:3])

        self.points = newpoints
        self.makelist()

    def setrotate(self, angles):
        angx, angy, angz = [ang for ang in angles]
        # *180/np.pi
        op = self.points[0]
        glPushMatrix()
        glLoadIdentity()
        glTranslatef(*(-1 * op))
        glRotatef(angx, 1, 0, 0)
        glRotatef(angy, 0, 1, 0)
        glRotatef(angz, 0, 0, 1)
        glTranslatef(*op)
        mv = glGetDoublev(GL_MODELVIEW_MATRIX)
        glPopMatrix()
        newpoints = []
        for point in self.points:
            ipoint = np.matmul(mv, (*point, 1))
            newpoints.append(ipoint[:3])

        self.norm = np.matmul(mv, (*self.norm, 1))[:3]
        self.points = newpoints
        self.makelist()

    def getnormaltoface(self, planeid):
        face = self.faces[planeid - 1]
        tries = [(face[i],face[i+1],face[i+2]) for i in range(len(face)-2)]
        for tri in tries:
            p1,p2,p3 = [self.points[point-1] for point in tri]
            v1 = p2 - p1
            v2 = p3 - p1
            n = np.cross(v1, v2)
            if np.linalg.norm(n) > 0:
                break
        return n

    def setonmv(self, mv):
        newpoints = []
        for point in self.points:
            ipoint = np.matmul(mv, (*point, 1))
            newpoints.append(ipoint[:3])

        self.norm = np.matmul(mv, (*self.norm, 1))[:3]
        self.points = newpoints
        self.makelist()

    def getcentr(self, face):
        cds = []
        for point in self.faces[face - 1]:
            cds.append(self.points[point - 1])
        cdx = [cd[0] for cd in cds]
        cdy = [cd[1] for cd in cds]
        cdz = [cd[2] for cd in cds]
        cmx = sum(cdx) / len(cdx)
        cmy = sum(cdy) / len(cdy)
        cmz = sum(cdz) / len(cdz)

        return np.array([cmx, cmy, cmz])

    def setup(self, extnorm, planeid, basepoint, destpoint, offset, angle):
        ''' so in here we got : plane from this object, point in this plane
        (as planeid and basepoint), extern normal in which direction
         we want to orient this geo object, point where to move it and
         offset with angle from local basis
            obji obj,objn - orthonorm basis in this object
        '''

        objnorm = self.getnormaltoface(planeid)
        objnorm = objnorm / np.linalg.norm(objnorm)
        t = (1,0,0)
        ta = techs.getangle(t,objnorm)
        if ta == 0 or ta == 180:
            t = (0,1,0)
        objj = np.cross(t, objnorm)
        obji = np.cross(objnorm, objj)
        obji = obji / np.linalg.norm(obji)
        objj = objj / np.linalg.norm(objj)

        rotationangle = techs.getangle(extnorm, objnorm)
        if np.round(rotationangle) == 180.0:
            objnorm *=-1
            rotationaxis = obji
        else:
            rotationaxis = np.cross(extnorm, objnorm)
        glPushMatrix()
        glRotatef(rotationangle, *rotationaxis)
        glRotatef(angle, *extnorm)
        mv = glGetDoublev(GL_MODELVIEW_MATRIX)
        glPopMatrix()

        basepoint = np.matmul(mv, (*(basepoint), 1))[:3]
        obji = np.matmul(mv, (*obji, 1))[:3]
        objj = np.matmul(mv, (*objj, 1))[:3]
        objnorm  = np.matmul(mv, (*objnorm, 1))[:3]

        offset = offset[0] * obji + offset[1] * objj + offset[2] * objnorm

        basepoint = np.array([basepoint[i] + offset[i] for i in (0, 1, 2)])
        self.setonmv(mv)
        self.setcoord(destpoint, basepoint)
        self.origin = destpoint

    def makearrayitem(self, offset, angle, normal):
        objnorm = normal / np.linalg.norm(normal)

        extnorm = (0, 0, 1)
        rotationangle = techs.getangle(extnorm, objnorm)
        if rotationangle == 180:
            objnorm *= -1
        rotationaxis = np.cross(extnorm, objnorm)
        glPushMatrix()
        glRotatef(rotationangle, *rotationaxis)
        glRotate(angle, *objnorm)
        mv = glGetDoublev(GL_MODELVIEW_MATRIX)
        glPopMatrix()

        obji = np.matmul(mv, (*(1, 0, 0), 1))[:3]
        objj = np.matmul(mv, (*(0, 1, 0), 1))[:3]

        offset = offset[0] * obji + offset[1] * objj + offset[2] * objnorm
        #print(obji, objj, objnorm)

        basepoint = self.origin
        basepoint = np.array([basepoint[i] + offset[i] for i in (0, 1, 2)])
        self.setcoord(self.origin, basepoint)


    def move(self,vec):
        x,y,z=vec
        self.points = [np.array([point[0]+x,point[1]+y,point[2]+z]) for point in self.points]
        self.makelist()

    def rotate(self,vec):
        ax,ay,az = vec
        op = np.mean(self.points,0)
        glPushMatrix()
        glLoadIdentity()
        glTranslatef(*op)
        glRotatef(ax, 1, 0, 0)
        glRotatef(ay, 0, 1, 0)
        glRotatef(az, 0, 0, 1)
        glTranslatef(*(-1 * op))
        mv = glGetDoublev(GL_MODELVIEW_MATRIX)
        mv = np.transpose(mv)
        glPopMatrix()
        newpoints = []
        for point in self.points:
            ipoint = np.matmul(mv, (*point, 1))
            newpoints.append(ipoint[:3])

        self.norm = np.matmul(mv, (*self.norm, 1))[:3]
        self.points = newpoints
        self.makelist()