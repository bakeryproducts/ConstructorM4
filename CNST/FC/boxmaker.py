import sys
path = 'C:\\Users\\User\Miniconda3\envs\FCENV\Library\\bin'
sys.path.append(path)
import FreeCAD,Mesh,MeshPart,Part
from FreeCAD import Base


class FC:
    def __init__(self):
        self.doc = App.newDocument("boxdoc")

    def newobject(self,obj):
        self.doc.addObject(obj.cat,obj.name)


class Box:
    def __init__(self,w,d,h):
        self.w = w
        self.h = h
        self.d = d
        self.loadinit()

    def loadinit(self):
        self.obj = Part.makeBox(self.w,self.h,self.d)
        self.geoinit()

    def geoinit(self):
        self.objmesh = MeshPart.meshFromShape(self.obj)
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

    def getgeo(self):
        return self.points,self.faces,self.edges

        #print(len(self.edges))
        #print(len(self.faces))

#box = Box(100,200,100)

# bpoints,bfaces,bedges = boxshape.Vertexes,boxshape.Faces,boxshape.Edges
# for point in bpoints:
#     cds = point.X,point.Y,point.Z
#     points.append(point)
#     print(cds)
#
# for face in bfaces:
#     for point in
#
#     print(face)


class Revolver:
    def __init__(self,points,axis):
        self.points = points
        self.axis = axis
        self.cont = []
        #self.obj = 0
        self.loadinit()

    def loadinit(self):
        self.points = [Base.Vector(point) for point in self.points]
        self.axis = Base.Vector(self.axis[0]),Base.Vector(self.axis[1])
        for i in range(len(self.points)-1):
            iline = Part.makeLine(self.points[i],self.points[i+1])
            self.cont.append(iline)
        self.cont.append(Part.makeLine(self.points[-1],self.points[0]))


        lshape = Part.Shape(self.cont)
        w = Part.Wire(self.cont)
        print(w.isClosed())
        face = Part.Face(w)
        self.obj = face.revolve(*self.axis,90)
        #self.om = MeshPart.meshFromShape(self.obj)
        self.r = Part.makeRevolution(self.cont[0])
        #Part.show(self.r)

    def getobj(self):
        #Mesh.export([self.om],'test.stl')
        self.r.exportStl('newfile.stl')
        print("done")
        #return self.obj

rev = Revolver([(0,0,0),(100,0,0),(100,100,0),(0,100,0)],[(0,0,0),(1,0,0)])
rev.getobj()
