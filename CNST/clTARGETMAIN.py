from CNST.clELEM import *


class TARGETMAIN(ELEM):
    def __init__(self, geoobj):
        super(TARGETMAIN, self).__init__(geoobj)
        self.category = 0

    def getcopy(self):
        copy = TARGETMAIN(self.geoobj.getcp())
        copy.facesnames = self.facesnames
        copy.defthick = self.defthick
        copy.defmat = self.defmat
        copy.thickarr = self.thickarr
        copy.matarr = self.matarr
        copy.category = self.category

        return copy


    def export(self, filename="new", path="RESULTS/"):
        str1 = ':Цель агрегатная ' + filename + '\n:броня ' + self.getname() + '\n:точки\n'
        str2 = ':грани 0\n'
        str3 = ':end'

        f = open(path + filename + '.trg', 'w')
        # f = open('C:/Users/User/Desktop/OOEF2017/InGEOBDS/'+filename+'.trg', 'w')

        try:
            f.write(str1)
        except UnicodeEncodeError:
            f.write(str1.encode('cp1251').decode('latin1'))

        for i, point in enumerate(self.geoobj.points):
            f.write('P' + str(i + 1) + '=' + str(list(point)) + '\n')

        try:
            f.write(str2)
        except UnicodeEncodeError:
            f.write(str2.encode('cp1251').decode('latin1'))

        for i, face in enumerate(self.geoobj.faces):
            f.write(self.facesnames[i] + ' = (' + str(list(face))[1:-1] + ')[' + str(self.thickarr[i]) +
                    ']' + '\n')

            # f.write(self.facesnames[i] + ' = (' + str(list(face))[1:-1] + ')[' + str(self.thickarr[i]) +
            #          ']; '+str(self.matarr[i].getname())+'\n')

        try:
            f.write(str3)
        except UnicodeEncodeError:
            f.write(str3.encode('cp1251').decode('latin1'))

        f.close()
