#from CNST.clGEOOBJ import *

class ELEM:
    def __init__(self,geoobj):
        self.geoobj = geoobj#.getcp()
        self.facesnames = ["G"+str(i+1) for i in range(len(self.geoobj.faces))]

    def setname(self,name):
        self.geoobj.setname(name)

    def setfacename(self,name,i):
        self.facesnames[int(i)] = str(name)

    def getfacesnames(self):
        return self.facesnames

    def getcopy(self):
        return ELEM(self.geoobj.getcp())

    def show(self):
        self.geoobj.show()

    def update(self,mvMatrix):
        self.geoobj.update(mvMatrix)

    def getgeo(self):
        return self.geoobj

    def getname(self):
        return self.geoobj.getname()

    def getid(self):
        return self.geoobj.getid()

    def showcolors(self):
        self.geoobj.showcolors()

    def showplane(self,planeid,oid):
        self.geoobj.showplane(planeid,oid)

    def setcoord(self,pos):
        self.geoobj.setcoord(pos)

    def setrotate(self,angles):
        self.geoobj.setrotate(angles)