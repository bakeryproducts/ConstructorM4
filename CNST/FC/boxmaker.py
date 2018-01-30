import sys
path = 'C:\\Users\\User\Miniconda3\envs\FCENV\Library\\bin'
sys.path.append(path)
import FreeCAD,Mesh,MeshPart,Part
from FreeCAD import Base


class FC:
    # def __init__(self,obj):
    #     self.obj=obj

    def geoinit(self,obj):
        self.objmesh = MeshPart.meshFromShape(obj)
        meshpoints,meshfaces = self.objmesh.Topology
        self.points,self.faces,self.edges = [],[],[]

        for point in meshpoints:
            cds = point.x,point.y,point.z
            self.points.append(point)
            #print(cds)

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


class Box(FC):
    def __init__(self,w,d,h):
        self.w = w
        self.h = h
        self.d = d
        self.loadinit()

    def loadinit(self):
        self.obj = Part.makeBox(self.w,self.h,self.d)
        self.geoinit(self.obj)

# box = Box(100,200,100)
# box.getgeo()


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
        pf = App.newDocument('Doc').addObject("Part::Feature", "MyShape")
        pf.Shape = self.obj
        Mesh.export([pf], 'tests.stl')

# rev = Revolver([(0,0,0),(100,0,0),(100,100,0),(0,100,0)],[(0,0,0),(200,0,0)])
# rev.getobj()
# print(rev.getgeo())