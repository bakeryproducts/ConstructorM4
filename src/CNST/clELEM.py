#from CNST.clGEOOBJ import *
#from MATERIALS.db import DB

class ELEM:
    def __init__(self,geoobj):
        self.geoobj = geoobj#.getcp()
        self.facesnames = ["G"+str(i+1) for i in range(len(self.geoobj.faces))]
        self.defthick = 50
        #self.defmat = self.matinit()
        self.thickarr = [self.defthick for i in range(len(self.facesnames))]
        #self.matarr = self.defmatinit(self.defmat)


    def setthick(self, face, thick):
        self.thickarr[face] = thick

    # def matinit(self):
    #     db = DB('MATERIALS\\GOST.xml')
    #     mat = db.getdefmat()
    #     return db.exportmat(mat)

    # def defmatinit(self,mat):
    #     return [mat for i in range(len(self.facesnames))]

    # def setmat(self, face, mat):
    #     self.matarr[face] = mat

    # def getmats(self):
    #     return set(self.matarr)

    def setname(self,name):
        self.geoobj.setname(name)

    def setid(self):
        self.geoobj.setid()

    def setfacename(self,name,i):
        self.facesnames[int(i)] = str(name)

    def getfacesnames(self):
        return self.facesnames

    # def getcopy(self):
    #     return ELEM(self.geoobj.getcp())

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

    def defcolset(self):
        self.geoobj.defcolset()

    def defopacityset(self):
        self.geoobj.defopacityet()

    def setcol(self,color):
        self.geoobj.setcol(color)

    def setopacity(self,opa):
        self.geoobj.setopacity(opa)

    def getcolor(self):
        self.geoobj.getcol()

    def getopacity(self):
        self.geoobj.getopa()