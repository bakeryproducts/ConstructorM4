import sys
path = 'C:\\Users\\User\Miniconda3\envs\FCENV\Library\\bin'
sys.path.append(path)
import FreeCAD,Mesh,MeshPart,Part
from FreeCAD import Base
import CNST.remesh,CNST.techs


class FC:
    def geoinit(self,obj):

        #TODO self repeating stuff right here
        faces = []
        shape = obj
        triangles = shape.tessellate(10)  # the number represents the precision of the tessellation)
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
        points,faces = CNST.remesh.remeshing(self.points[:],self.faces[:])
        edges = CNST.techs.getedges(faces)
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
            #ipoints.append(Base.Vector(*point[:2], 0))
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
        extfacedelta = fd.extrude(Base.Vector(0, 0, self.depth))

        bars = []
        for i in range(self.nx):
            p1 = Base.Vector(xmin + (i + 1) * self.dx, ymin, 0)
            rect = Part.makePlane(self.ix, ymax - ymin, p1, Base.Vector(0, 0, 1))
            bars.append(rect)

        for i in range(self.ny):
            p1 = Base.Vector(xmin, (i + 1) * self.dy + ymin, 0)
            rect = Part.makePlane(xmax - xmin, self.iy, p1, Base.Vector(0, 0, 1))
            bars.append(rect)

        facebars = bars[0]
        for bar in bars[1:]:
            facebars = facebars.fuse(bar)
        #facebars = facebars.cut(fd)
        facebars = facebars.common(fin)
        #slat = facebars.fuse(fd)
        extbars = facebars.extrude(Base.Vector(0, 0, self.depth))
        #self.obj = slat.extrude(Base.Vector(0, 0, self.depth))
        self.obj = extbars.fuse(extfacedelta)
        self.geoinit(self.obj)

    def getobj(self):
        #TODO this is only way its working: adding newdoc
        pf = FreeCAD.newDocument('Doc').addObject("Part::Feature", "MyShape")
        pf.Shape = self.obj
        Mesh.export([pf], 'SLAT.stl')


class Revolver(FC):
    def __init__(self,points,axis,angle=360):
        self.points = points
        self.axis = axis
        self.cont = []
        self.angle=angle
        #self.obj = 0
        self.loadinit()

    def loadinit(self):
        self.points = [Base.Vector(point) for point in self.points]
        self.axis = Base.Vector(self.axis[0]),Base.Vector(self.axis[1])
        for i in range(len(self.points)-1):
            iline = Part.makeLine(self.points[i],self.points[i+1])
            self.cont.append(iline)
        self.cont.append(Part.makeLine(self.points[-1],self.points[0]))
        w = Part.Wire(self.cont)
        face = Part.Face(w)
        self.obj = face.revolve(*self.axis,self.angle)
        self.geoinit(self.obj)

    def getobj(self):
        #TODO this is only way its working: adding newdoc
        pf = FreeCAD.newDocument('Doc').addObject("Part::Feature", "MyShape")
        pf.Shape = self.obj
        Mesh.export([pf], 'REVOLVER.stl')

# rev = Revolver([(0,0,0),(100,0,0),(100,100,0),(0,100,0)],[(0,0,0),(200,0,0)])
# rev.getobj()
# print(rev.getgeo())