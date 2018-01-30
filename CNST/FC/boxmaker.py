import sys
path = 'C:\\Users\\User\Miniconda3\envs\FCENV\Library\\bin'
sys.path.append(path)
import FreeCAD,Mesh,MeshPart,Part


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
