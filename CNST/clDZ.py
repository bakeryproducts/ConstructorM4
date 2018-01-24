import numpy as np
from CNST.clELEM import *


class DZcreator:
    def __init__(self, w, d, h, angle):
        self.p, self.f, self.e = self.createdz(w, d, h, angle)

    def box(self, w, h, d):
        p0 = 0, 0, 0
        p1 = w, 0, 0
        p2 = w, d, 0
        p3 = 0, d, 0
        p4 = 0, 0, h
        p5 = w, 0, h
        p6 = w, d, h
        p7 = 0, d, h
        points = [p0, p1, p2, p3, p4, p5, p6, p7]

        # faces = [(0,1,2),(1,2,4),(4,5,6),(5,6,7),(0,1,4),(1,4,5),(1,5,2),(5,6,2),
        #          (6,3,2),(7,3,6),(7,0,3),(7,4,0)]

        faces = [[3, 2, 1, 0], [4, 5, 6, 7], [1, 5, 4, 0], [4, 7, 3, 0], [7, 6, 2, 3], [2, 6, 5, 1]]
        resfaces = []
        for face in faces:
            iface = []
            for p in face:
                iface.append(p + 1)
            resfaces.append(iface)
        return points, resfaces

    def activeplane(self, angle, points, w):
        p0, p1, p4, p5 = points[0], points[1], points[4], points[5]
        y = w * np.tan(np.pi * angle / 180)
        p4z = p0[0], y, p0[2]
        p5z = p1[0], y, p1[2]
        addpoints = p4z, p5z
        # face = p0,p1z,p2z,p3
        return addpoints

    def createdz(self, w, d, h, angle):
        bpoints, bfaces = self.box(w, d, h)
        ppoints = self.activeplane(angle, bpoints, w)
        bpoints.append(ppoints[0])
        bpoints.append(ppoints[1])
        bfaces.append([10,9,5,6])

        edges = []
        for face in bfaces:
            iface = face[:]
            iface.append(face[0])
            for i in range(len(iface) - 1):
                edge = [iface[i], iface[i + 1]]
                if (edge not in edges) and (list(reversed(edge)) not in edges):
                    edges.append(edge)

        return bpoints, bfaces, edges

    def getpointsfaces(self):
        return self.p, self.f, self.e


class DZ(ELEM):
    def __init__(self, geoobj):
        super(DZ, self).__init__(geoobj)
        self.categoryname = 0

    def getcopy(self):
        copy = DZ(self.geoobj.getcp())
        copy.facesnames = self.facesnames[:]
        copy.defthick = self.defthick
        copy.defmat = self.defmat
        copy.thickarr = self.thickarr[:]
        copy.matarr = self.matarr[:]
        copy.categoryname = self.categoryname
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
            poistr = '('+str(point[0])+', '+str(point[1])+', '+str(point[2])+')'
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
