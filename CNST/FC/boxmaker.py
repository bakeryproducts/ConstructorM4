import FreeCAD,Mesh,MeshPart,Part
import numpy as np
import CNST.remesh,CNST.techs

class FC:
    def geoinit(self,obj):

        #TODO self repeating stuff right here
        faces = []
        shape = obj
        triangles = shape.tessellate(1)  # the number represents the precision of the tessellation)
        for tri in triangles[1]:
            face = []
            for i in range(3):
                vindex = tri[i]
                face.append(triangles[0][vindex])
            faces.append(face)
        self.objmesh = Mesh.Mesh(faces)

        meshpoints,meshfaces = self.objmesh.Topology
        self.points,self.faces,self.edges = [],[],[]

        for point in meshpoints:
            #cds = point.x,point.y,point.z
            self.points.append(point)

        for face in meshfaces:
            iface = []
            for indexp in face:
                iface.append(indexp+1)
            self.faces.append(iface)

        for face in self.faces:
            iface = face[:]
            iface.append(face[0])
            for i in range(len(iface) - 1):
                edge = [iface[i], iface[i + 1]]
                if (edge not in self.edges) and (list(reversed(edge)) not in self.edges):
                    self.edges.append(edge)

        return self.points,self.faces,self.edges

    def getgeo(self):
        return self.points,self.faces,self.edges

    def getremshgeo(self):
        print('remestart',len(self.faces),len(self.points))
        points,faces,edges = CNST.remesh.remeshing(self.points[:],self.faces[:])
        print('remeend')
        return points,faces,edges

class Box(FC):
    def __init__(self,w,d,h):
        self.w = w
        self.h = h
        self.d = d
        self.loadinit()

    def loadinit(self):
        self.obj = Part.makeBox(self.w,self.h,self.d)
        self.geoinit(self.obj)


class Slatarmor(FC):
    def __init__(self, points, thick, depth, nx=2, ny=2, dx=20, dy=20, ix=5, iy=5):
        self.points = points
        self.nx, self.ny = nx, ny
        self.dx, self.dy = dx, dy
        self.ix, self.iy = ix, iy
        self.thick = thick
        self.depth = depth
        self.cont = []
        self.loadinit()

    def loadinit(self):
        ipoints = []
        xs, ys = [], []
        for point in self.points:
            ipoints.append((*point[:2],0))
            xs.append(point[0])
            ys.append(point[1])

        self.points = ipoints
        xmax, xmin = max(xs), min(xs)
        ymax, ymin = max(ys), min(ys)

        for i in range(len(self.points) - 1):
            iline = Part.makeLine(self.points[i], self.points[i + 1])
            self.cont.append(iline)
        self.cont.append(Part.makeLine(self.points[-1], self.points[0]))

        w = Part.Wire(self.cont)

        fin = Part.Face(w)
        wout = w.makeOffset2D(self.thick, join=2)

        fout = Part.Face(wout)

        fd = fout.cut(fin)
        extfacedelta = fd.extrude(FreeCAD.Vector(0, 0, self.depth))

        bars = []
        for i in range(self.nx):
            p1 = FreeCAD.Vector(xmin + (i + 1) * self.dx, ymin, 0)
            rect = Part.makePlane(self.ix, ymax - ymin, p1, FreeCAD.Vector(0, 0, 1))
            bars.append(rect)

        for i in range(self.ny):
            p1 = FreeCAD.Vector(xmin, (i + 1) * self.dy + ymin, 0)
            rect = Part.makePlane(xmax - xmin, self.iy, p1, FreeCAD.Vector(0, 0, 1))
            bars.append(rect)

        facebars = bars[0]
        for bar in bars[1:]:
            facebars = facebars.fuse(bar)
        #facebars = facebars.cut(fd)
        facebars = facebars.common(fin)
        #slat = facebars.fuse(fd)
        extbars = facebars.extrude(FreeCAD.Vector(0, 0, self.depth))
        #self.obj = slat.extrude(FreeCAD.Vector(0, 0, self.depth))
        self.obj = extbars.fuse(extfacedelta)
        self.geoinit(self.obj)

    def getobj(self):
        #TODO this is only way its working: adding newdoc
        pf = FreeCAD.newDocument('Doc').addObject("Part::Feature", "MyShape")
        pf.Shape = self.obj
        Mesh.export([pf], 'SLAT.stl')


class Revolver(FC):
    def __init__(self,points,axis,arcs,galts,freverse,angle=360):
        self.pointsdict=points
        if freverse:
            self.points = reversed(list(points.values()))
        else:
            self.points = points.values()
        self.axis = axis
        self.cont = []
        self.angle=angle
        #self.obj = 0
        self.arcs = arcs
        self.galts=galts
        self.loadinit()

    def loadinit(self):
        self.points = [FreeCAD.Vector(point) for point in self.points]
        #print(len(self.points))
        self.axis = FreeCAD.Vector(self.axis[0]),FreeCAD.Vector(self.axis[1])
        for i in range(len(self.points)-1):
            if self.points[i]:

                k = list(self.pointsdict.keys())[i]
                #print(k)
                if k in self.arcs.keys():
                #if t in self.arcs.keys():
                    r = self.arcs[k]
                    #print(k,r)
                    p1,p3 = np.array(self.points[i]),np.array(self.points[i+1])
                    p2 = self.getarcpoint(p1,p3,r)
                    ps = FreeCAD.Vector(p3),FreeCAD.Vector(p2),FreeCAD.Vector(p1)
                    #print(ps)
                    iline = Part.Arc(*ps).toShape()
                else:
                    iline = Part.makeLine(self.points[i],self.points[i+1])
                self.cont.append(iline)
        self.cont.append(Part.makeLine(self.points[-1],self.points[0]))
        w = Part.Wire(self.cont)
        face = Part.Face(w)
        self.obj = face.revolve(*self.axis,self.angle)
        self.geoinit(self.obj)

    def getarcpoint(self, p1, p2, r):
        # p1 = np.array((10, 0, 0))
        # p2 = np.array((20, 0, 0))
        # r = 5
        pm = (p2 + p1) / 2
        #print(pm)
        v1 = p2 - pm
        n = np.array((0, 0, 1))
        rv = np.cross(v1,n)
        rv = rv / np.linalg.norm(rv)
        if rv[0]+pm[0]>pm[0]:
            n = np.array((0, 0, -1))
            rv = np.cross(v1, n)
            rv = rv / np.linalg.norm(rv)

        #print(rv,v1)
        lr = np.sqrt(r * r - (np.linalg.norm(v1) * np.linalg.norm(v1)))
        #print(r,np.linalg.norm(v1))
        xv = pm-rv * (r - lr)
        #print(xv)
        return xv

    def getobj(self):
        #TODO this is only way its working: adding newdoc
        pf = FreeCAD.newDocument('Doc').addObject("Part::Feature", "MyShape")
        pf.Shape = self.obj
        Mesh.export([pf], 'REVOLVER.stl')

# rev = Revolver([(0,0,0),(100,0,0),(100,100,0),(0,100,0)],[(0,0,0),(200,0,0)])
# rev.getobj()
# print(rev.getgeo())