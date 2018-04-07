import numpy as np
from scipy import interpolate
from scipy.signal import savgol_filter
from CNST.clGEOOBJ import GEOOBJ
from CNST.clTARGETMAIN import TARGETMAIN

class ArmorSurface:
    def __init__(self,ABR,divisions,name):

        self.groundangle=360
        self.vertangle=90
        self.m,self.n = divisions
        self.istep, self.jstep = round(self.groundangle / self.m), round(self.vertangle / self.n)

        self.al, self.be, self.r = ABR
        self.genpoints()
        self.name = name
        self.gengeo()

    def genpoints(self):
        points = []
        r = self.smooth(self.r)
        for a, b, r in zip(self.al, self.be, r):
            #r*=50
            ix,iy,iz = r * np.cos(b) * np.sin(a),r * np.cos(b) * np.cos(a),r * np.sin(b)
            points.append([ix,iz,iy])
        self.points = points

    def gengeo(self):

        self.faces,self.edges=[],[]
        indpoints = range(len(self.points))
        istep,jstep = round(self.groundangle/self.m),round(self.vertangle/self.n)
        for i in indpoints[:-istep-1]:
            if i%(istep)!=0:
                ind1,ind2 = i,i+1
                ind3,ind4 = i+istep,i+istep+1
            else:
                ind1,ind2=i+1-istep,i+1
                ind3,ind4 = i-istep,i

            # p1,p2 = self.points[ind1],self.points[ind2]
            # p3,p4 = self.points[ind3],self.points[ind4]
            self.faces.append([indpoints[j] for j in [ind2,ind4,ind1]])
            self.faces.append([indpoints[j] for j in [ind1,ind4,ind3]])

        # print(self.points[:5])
        # print(self.faces[:5])
        # print(indpoints[:5])

        self.geoobj = GEOOBJ((self.points,self.faces,self.edges),self.name)

    def crecomp(self):
        self.comp = TARGETMAIN(self.geoobj)
        self.comp.comptype = 'SURFACE'
        self.comp.setname(self.name)

    def smooth(self,rs):
        smoothr = []
        st = self.istep
        for i in range(round(len(rs)/st)):
            t = savgol_filter(np.array(rs[i*st:st*(i+1)]),11,2)
            smoothr.append(t)

        return [i for si in smoothr for i in si]

    def smoothr(self,rs):
        smoothr = []
        st = self.istep
        for i in range(round(len(rs) / st)):
            t = savgol_filter(np.array(rs[i * st:st * (i + 1)]), 11, 2)
            smoothr.append(t)

        return [i for si in smoothr for i in si]
