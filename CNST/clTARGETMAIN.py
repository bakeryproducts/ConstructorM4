import numpy as np
from CNST.clELEM import *

class TARGETMAIN(ELEM):
    def __init__(self, geoobj):
        super(TARGETMAIN, self).__init__(geoobj)
        self.categoryname = 0
        self.comptype = 0

    def getcopy(self):
        copy = TARGETMAIN(self.geoobj.getcp())
        copy.facesnames = self.facesnames[:]
        copy.defthick = self.defthick
        #copy.defmat = self.defmat
        copy.thickarr = self.thickarr[:]
        #copy.matarr = self.matarr[:]
        copy.categoryname = self.categoryname
        copy.comptype = self.comptype
        return copy


    def export(self, f,index):
        # str1 = ':Цель агрегатная ' + filename + '\n:броня ' + self.getname() + '\n:точки\n'
        # str2 = ':грани 0\n'
        # str3 = ':end'
        #
        # f = open(path + filename + '.trg', 'w')
        # f = open('C:/Users/User/Desktop/OOEF2017/InGEOBDS/'+filename+'.trg', 'w')

        poi = ':точки\n'
        br = ':броня '+self.getname().split('.')[0]+str(index)+'\n'+poi
        fac = ':грани 0\n'

        try:
            f.write(br)
        except UnicodeEncodeError:
            f.write(br.encode('cp1251').decode('latin1'))

        for i, point in enumerate(self.geoobj.points):
            point = [np.round(cd, 3) for cd in point]
            poistr = '(' + str(point[0]) + ', ' + str(point[1]) + ', ' + str(point[2]) + ')'
            f.write('P' + str(i + 1) + '=' + poistr + '\n')

        try:
            f.write(fac)
        except UnicodeEncodeError:
            f.write(fac.encode('cp1251').decode('latin1'))

        for i, face in enumerate(self.geoobj.faces):
            f.write(self.facesnames[i] + ' = (' + str(list(face))[1:-1] + ')[' + str(self.thickarr[i]) +
                    ']' + '\n')

        self.exportmat(f)

