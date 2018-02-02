import numpy as np
from CNST.clELEM import *
import CNST.FC.boxmaker
import CNST.clGEOOBJ


class SLAT(ELEM):
    def __init__(self, params):
        self.categoryname = 0

        name, self.points, self.slatthick, self.slatdepth, \
        self.nx, self.ny, self.dx, self.dy, self.ix, self.iy = params

        pie = CNST.FC.boxmaker.Slatarmor(self.points, self.slatthick, self.slatdepth,
                                         self.nx, self.ny, self.dx, self.dy, self.ix, self.iy)
        geos = pie.getgeo()
        #geos = pie.getremshgeo()
        geoobj = CNST.clGEOOBJ.GEOOBJ(geos, name)
        super(SLAT, self).__init__(geoobj)

    def setx(self, n, x):
        self.points[n][0] = x

    def sety(self, n, y):
        self.points[n][1] = y

    def getcopy(self):
        params = self.geoobj.getname(), self.points, self.slatthick, self.slatdepth, \
                 self.nx, self.ny, self.dx, self.dy, self.ix, self.iy
        copy = SLAT(params)

        copy.facesnames = self.facesnames[:]
        copy.defthick = self.defthick
        copy.defmat = self.defmat
        copy.thickarr = self.thickarr[:]
        copy.matarr = self.matarr[:]
        copy.categoryname = self.categoryname
        # copy.points = self.points
        # copy.slatthick = self.slatthick
        # copy.slatdepth = self.slatdepth
        # copy.nx = self.nx
        # copy.ny = self.ny
        # copy.dx = self.dx
        # copy.dy = self.dy
        # copy.ix = self.ix
        # copy.iy = self.iy
        return copy

    def export(self, f, index):
        # str1 = ':Цель агрегатная ' + filename + '\n:броня ' + self.getname() + '\n:точки\n'
        # str2 = ':грани 0\n'
        # str3 = ':end'
        #
        # f = open(path + filename + '.trg', 'w')
        # f = open('C:/Users/User/Desktop/OOEF2017/InGEOBDS/'+filename+'.trg', 'w')

        poi = ':точки\n'
        br = ':броня ' + self.getname().split('.')[0] + str(index) + '\n' + poi
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

    def exportmat(self, f):
        f.write('\n' + 10 * '_' + "Materials\n")
        i = 0
        d = {}
        res = []
        for mat in self.matarr:
            if mat not in d.keys():
                d[mat] = 'Mat' + str(i)
                i += 1
            res.append(d[mat])
            f.write(str(d[mat]) + '; ')

        f.write('\nLegend:\n')
        for k, v in d.items():
            st = v + ' = ' + k.getname() + '\n'
            try:
                f.write(st)
            except UnicodeEncodeError:
                f.write(st.encode('cp1251').decode('latin1'))
            if k.category == 'HETERO':
                for kh, vh in k.getprops().items():
                    st = '\t\t' + kh + ' for ' + vh + ' mm\n'
                    try:
                        f.write(st)
                    except UnicodeEncodeError:
                        f.write(st.encode('cp1251').decode('latin1'))
