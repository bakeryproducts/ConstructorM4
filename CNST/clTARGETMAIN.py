from CNST.clELEM import *

class TARGETMAIN(ELEM):
    def __init__(self,geoobj):
        super(TARGETMAIN,self).__init__(geoobj)
        self.steq = 0
        self.steqarr = {}
        self.category=0


    def getcopy(self):
        copy =  TARGETMAIN(self.geoobj.getcp())
        copy.steq = self.steq
        copy.steqarr = self.steqarr
        copy.category = self.category
        return copy

    def setsteq(self,eq):
        self.steq = eq

    def changesteq(self,face,steq):
        self.steqarr[face]=steq

    def export(self,filename="new",path="RESULTS/"):
        str1 = ':Цель агрегатная ' + filename + '\n:броня '+self.getname()+'\n:точки\n'
        str2 = ':грани 0\n'
        str3 = ':end'

        f = open(path + filename + '.trg', 'w')
        #f = open('C:/Users/User/Desktop/OOEF2017/InGEOBDS/'+filename+'.trg', 'w')

        try:
            f.write(str1)
        except UnicodeEncodeError:
            f.write(str1.encode('cp1251').decode('latin1'))

        for i, point in enumerate(self.geoobj.points):
            f.write('P' + str(i + 1) + '=' + str(point) + '\n')

        try:
            f.write(str2)
        except UnicodeEncodeError:
            f.write(str2.encode('cp1251').decode('latin1'))

        for i, face in enumerate(self.geoobj.faces,start=1):
                if i in self.steqarr.keys():
                    f.write('G' + str(i) + ' = (' + str(face)[1:-1] + ')[' + str(self.steqarr[i]) + ']\n')
                else:
                    print("err")
                    #f.write('G' + str(i) + ' = (' + str(face)[1:-1] + ')[' + str(self.steq) + ']\n')

        try:
            f.write(str3)
        except UnicodeEncodeError:
            f.write(str3.encode('cp1251').decode('latin1'))

        f.close()
