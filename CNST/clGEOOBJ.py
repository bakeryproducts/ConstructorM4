import CNST.techs as techs
from itertools import count
import numpy as np
from OpenGL.GL import *
from OpenGL.arrays import vbo

class GEOOBJ:
    _ids = count(0)
    _arids = []

    def __init__(self, geometry, name):
        self.setid()
        self.name = name

        self.points, self.faces, self.edges = [np.array(item) for item in geometry]
        self.normals = [self.getnormaltoface(i+1) for i in range(len(self.faces))]
        self.normals = np.array([self.normals[j] for j,face in enumerate(self.faces) for i in range(len(face))],dtype = np.float32)
        self.npoints = np.array([self.points[i-1] for face in self.faces for i in face],dtype = np.float32)
        self.colors = techs.setcolors(self.id, len(self.faces))
        self.colors = np.array([self.colors[j] for j, face in enumerate(self.faces) for i in range(len(face))],dtype=np.ubyte)
        self.bufinit()

        self.fedge=True
        self.ffc = False
        self.origin = self.points[0]

        self.mvMatrix = np.identity(4)
        self.psMatrix = np.identity(4)

        self.col = (.7, .5, .3)
        self.defcol = self.col
        self.opa = 1
        self.defopa = self.opa


    def __del__(self):
        self._arids.remove(self.id)
        # self.vbo.delete()
        # self.nbo.delete()
        # self.cbo.delete()
        del(self.vbo)
        del(self.nbo)
        del(self.cbo)

    def bufdrop(self):
        pass
        # self.vbo.delete()
        # self.nbo.delete()
        # self.cbo.delete()
        # del(self.vbo)
        # del(self.nbo)
        # del(self.cbo)

    def cbinit(self,cols):
        self.ccbo = vbo.VBO(cols)

    def bufinit(self):
        self.vbo = vbo.VBO(self.npoints)
        self.nbo = vbo.VBO(self.normals)
        self.cbo = vbo.VBO(self.colors)


    def updatenpoints(self):
        self.npoints = [self.points[i - 1] for face in self.faces for i in face]
        self.npoints = np.require(self.npoints, np.float32, 'F')

        # self.normals = [self.getnormaltoface(i + 1) for i in range(len(self.faces))]
        # self.normals = [self.normals[j] for j, face in enumerate(self.faces) for i in range(len(face))]
        # self.normals = np.array(self.normals, dtype=np.float32)

        self.vbo.set_array(self.npoints)
        # self.nbo.set_array(self.normals)

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
        copy.psMatrix = self.psMatrix
        copy.fedge = self.fedge
        copy.col = self.col
        #copy.fedge=self.fedge
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
        #self.makelist()

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

    def show(self):
        glPushMatrix()
        glLoadIdentity()
        glMultMatrixf(self.mvMatrix)

        glEnableClientState(GL_VERTEX_ARRAY)
        self.vbo.bind()
        glVertexPointer(3, GL_FLOAT, 0, self.vbo)

        glEnableClientState(GL_NORMAL_ARRAY)
        self.nbo.bind()
        glNormalPointer(GL_FLOAT, 0, self.nbo)

        if self.ffc:
            glEnableClientState(GL_COLOR_ARRAY)
            self.ccbo.bind()
            glColorPointer(3, GL_UNSIGNED_BYTE, 0, self.ccbo)
        else:
            glColor4fv((*self.col, self.opa))

        glDrawArrays(GL_TRIANGLES, 0, len(self.npoints))
        if self.ffc:
            self.ccbo.unbind()
            glDisableClientState(GL_COLOR_ARRAY)

        self.nbo.unbind()
        glDisableClientState(GL_NORMAL_ARRAY)

        self.vbo.unbind()
        glDisableClientState(GL_VERTEX_ARRAY)

        glPopMatrix()

        # glPushMatrix()
        # glLoadIdentity()
        # glMultMatrixf(self.mvMatrix)
        # glColor3fv((0, 0, 0))
        # glCallList(self.edgelist)
        # glColor4fv((*self.col,self.opa))
        # glCallList(self.objlist)
        # glPopMatrix()

    def showcolors(self):
        glDisable(GL_LIGHTING)
        glPushMatrix()
        glMultMatrixf(self.mvMatrix)
        glEnableClientState(GL_VERTEX_ARRAY)
        self.vbo.bind()
        glVertexPointer(3, GL_FLOAT, 0, self.vbo)

        glEnableClientState(GL_COLOR_ARRAY)
        self.cbo.bind()
        glColorPointer(3,GL_UNSIGNED_BYTE, 0, self.cbo)

        glDrawArrays(GL_TRIANGLES, 0, len(self.colors))

        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_COLOR_ARRAY)

        self.vbo.unbind()
        self.cbo.unbind()

        # glBegin(GL_TRIANGLES)
        # for i, face in enumerate(self.faces):
        #     #glBegin(GL_POLYGON)
        #     glColor3ub(*self.colors[i])
        #     for point in face:
        #         glVertex3fv(self.points[point - 1])
        #     #glEnd()
        # glEnd()
        glPopMatrix()
        glEnable(GL_LIGHTING)

    def showplane(self, planeid, oid):
        if oid == self.id and planeid <= len(self.faces) and planeid > 0:
            #glDisable(GL_LIGHTING)
            glColor3fv((0.4, 1, 0.2))
            glPushMatrix()
            glMultMatrixf(self.mvMatrix)
            glBegin(GL_TRIANGLES)
            #glBegin(GL_POLYGON)
            #norm = self.getnormaltoface(planeid)
            #glNormal3fv(norm)
            for point in self.faces[planeid - 1]:
                glVertex3fv(self.points[point - 1])
            glEnd()
            glPopMatrix()
            #glEnable(GL_LIGHTING)
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
        self.psMatrix = np.matmul(self.psMatrix,mv)

        newpoints = []
        for point in self.points:
            ipoint = np.matmul(mv, (*point, 1))
            newpoints.append(ipoint[:3])

        self.points = newpoints
        self.updatenpoints()

    def setrotate(self, angles):
        angx, angy, angz = [ang for ang in angles]
        op = self.points[0]
        glPushMatrix()
        glLoadIdentity()
        glTranslatef(*(-1 * op))
        glRotatef(angx, 1, 0, 0)
        glRotatef(angy, 0, 1, 0)
        glRotatef(angz, 0, 0, 1)
        glTranslatef(*op)
        mv = glGetDoublev(GL_MODELVIEW_MATRIX)
        self.psMatrix = np.matmul(self.psMatrix, mv)

        glPopMatrix()
        newpoints = []
        for point in self.points:
            ipoint = np.matmul(mv, (*point, 1))
            newpoints.append(ipoint[:3])

        self.points = newpoints
        self.updatenpoints()

    # def getnormaltoface(self, planeid):
    #     face = self.faces[planeid - 1]
    #     tries = [(face[i],face[i+1],face[i+2]) for i in range(len(face)-2)]
    #     for tri in tries:
    #         p1,p2,p3 = [self.points[point-1] for point in tri]
    #         v1 = p2 - p1
    #         v2 = p3 - p1
    #         n = np.cross(v1, v2)
    #         if np.linalg.norm(n) > 0:
    #             break
    #     return n

    def getnormaltoface(self, planeid):
        face = self.faces[planeid - 1]
        p1,p2,p3 = [self.points[point-1] for point in face][:3]
        v1 = p2 - p1
        v2 = p3 - p1
        n = np.cross(v1, v2)
        return n


    def setonmv(self, mv):
        newpoints = []
        for point in self.points:
            ipoint = np.matmul(mv, (*point, 1))
            newpoints.append(ipoint[:3])

        self.points = newpoints
        self.updatenpoints()

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
        #extnorm = extnorm / np.linalg.norm(extnorm)
        #print(extnorm,objnorm)
        rotationangle = techs.getangle(extnorm, objnorm)
        if np.round(rotationangle) == 180.0:
            objnorm *= -1
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
        objnorm = np.matmul(mv, (*objnorm, 1))[:3]

        offset = offset[0] * obji + offset[1] * objj + offset[2] * objnorm

        basepoint = np.array([basepoint[i] + offset[i] for i in (0, 1, 2)])
        self.setonmv(mv)
        self.setcoord(destpoint, basepoint)
        self.origin = destpoint
        self.updatenpoints()

    def move(self,vec):
        x,y,z=vec
        self.points = [np.array([point[0]+x,point[1]+y,point[2]+z]) for point in self.points]
        self.updatenpoints()

        vec = np.array(vec)
        glPushMatrix()
        glLoadIdentity()
        glTranslatef(*vec[:3])
        mv = glGetDoublev(GL_MODELVIEW_MATRIX)
        mv = np.transpose(mv)
        glPopMatrix()
        self.psMatrix = np.matmul(mv,self.psMatrix)

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

        self.psMatrix = np.matmul(self.psMatrix, mv)
        newps = np.zeros((len(self.points),3))
        for i,point in enumerate(self.points):
            ipoint = np.matmul(mv, (*point, 1))
            newps[i] = ipoint[:3]
        self.setnormals(mv)
        self.points = newps
        self.updatenpoints()

    def setnormals(self,mv):
        self.normals = [np.matmul(mv,(*n,1))[:3] for n in self.normals]


