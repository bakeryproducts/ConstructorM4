from techs import *
from OpenGL.GL import *


class TDARRAY():
    def __init__(self, obj, point, norm, nx, ny, dx, dy, offsetpoint):
        self.obj = obj
        self.nx = nx
        self.ny = ny
        self.dx = dx
        self.dy = dy
        self.norm = norm
        self.origin = point
        self.offset = offsetpoint
        self.objarr = []

        self.setup()

    def show(self):
        for obj in self.objarr:
            obj.show()

    def update(self, mvMatrix):
        for obj in self.objarr:
            obj.update(mvMatrix)

    def showcolors(self):
        for obj in self.objarr:
            obj.showcolors()

    def showplane(self, planeid, oid):
        for obj in self.objarr:
            obj.showplane(planeid, oid)

    def getid(self):
        ids = []
        for obj in self.objarr:
            ids.append(obj.getid())
        return ids

    def setup(self):
        arx = np.arange(0, self.nx * (self.dx), self.dx)
        arz = np.arange(0, self.ny * (self.dy), self.dy)

        arpoints = []
        for x in arx:
            for z in arz:
                arpoints.append((x, 0, z))
        if self.norm != (0, 0, 0):
            objnorm = self.obj.geoobj.getnorm()[1]
            rotationaxis = np.cross(self.norm, objnorm)
            rotationangle = getangle(self.norm, objnorm)
        else:
            rotationangle = 0
            rotationaxis = (1, 0, 0)

        glPushMatrix()
        glRotatef(rotationangle, *rotationaxis)
        mv = glGetDoublev(GL_MODELVIEW_MATRIX)
        glPopMatrix()
        arpointsplace = []
        for point in arpoints:
            ipoint = np.matmul(mv, (*point, 1))
            arpointsplace.append(ipoint[:3])

        for ind in range(len(arpointsplace)):
            idz = self.obj.getcopy()
            idz.geoobj.setonmv(mv)
            idz.geoobj.setcoord(arpointsplace[ind] + self.origin + self.offset)
            self.objarr.append(idz)

    def stats(self):
        print(self.objarr)
        print(len(self.objarr))
        for obj in self.objarr:
            print(obj.geoobj)
