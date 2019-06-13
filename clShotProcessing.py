import numpy as np

class ShotProcessing:
    def __init__(self,picdata,shotpoints,componentdata,mvMat,size,percparam):
        self.picdata = picdata
        self.shotpoints = shotpoints
        self.n = len(self.shotpoints)
        #self.component = component
        self.mvMat = mvMat
        self.w,self.h = size
        p0,p1,pn = percparam
        self.percarr = np.linspace(p0,p1,num=pn)
        raystart = np.transpose([shotpoints[:, 1] - self.w / 2, self.h / 2 - shotpoints[:, 0]])
        self.raystart = np.pad(raystart, (0, 1), 'constant', constant_values=(0))[:-1]
        self.lookvec = np.array([0, 0, 1])

        self.normals,self.thickness,self.planeorigins = componentdata#self.compinit()
        self.shotnormals, self.shotorgs = np.zeros((self.n, 3)), np.zeros((self.n, 3))
        self.shotthicks, self.shotplaneids, self.shotdepths = np.zeros((self.n)), np.zeros((self.n)), np.zeros((self.n))

    def initparams(self):
        self.shotnormals.fill(0)
        self.shotorgs.fill(0)
        self.shotthicks.fill(np.nan)
        self.shotplaneids.fill(0)
        self.shotdepths.fill(0)

    def getmaindata(self,ricochet=False):
        n = self.n
        self.initparams()
        shotnormals, shotorgs = self.shotnormals,self.shotorgs#np.zeros((n, 3)), np.zeros((n, 3))
        shotthicks, shotplaneids, shotdepths = self.shotthicks,self.shotplaneids,self.shotdepths #np.zeros((n)), np.zeros((n)), np.zeros((n))
        #depth = np.zeros((n))

        shotdata = self.picdata[self.shotpoints[:, 0], self.shotpoints[:, 1]]
        shotfull = np.zeros((n))
        shothit = shotdata[:, 0] != 255
        shotobjclr = shotdata[shothit]
        shotplclr = np.transpose(shotobjclr)[1:3]
        plids = 256 * shotplclr[0] + shotplclr[1]
        shotfull[np.where(shothit)] = 1
        ind = np.where(shotfull > 0)

        planeids = shotfull.copy()
        planeids[ind] = plids

        totalhits = np.sum(shotfull)

        if totalhits > 0:
            shotnormals[ind] = self.normals[plids - 1]
            shotthicks[ind] = self.thickness[plids - 1]
            shotorgs[ind] = self.planeorigins[plids - 1]
            self.shotNTO = shotnormals,shotthicks,shotorgs

            extnorms = np.pad(shotnormals, (0, 1), 'constant')[:-1]
            multnorms = (np.matmul(extnorms, self.mvMat))[:, :-1]

            res1 = np.linalg.norm(np.cross(multnorms, self.lookvec), axis=1)
            nd = np.dot(multnorms, self.lookvec)
            ang = np.arctan2(res1, nd)
            if ricochet:
                val = ricochet
                cond = np.where(ang > val * np.pi / 180.)
                ang[cond] = np.nan
            eqthicks = shotthicks / np.cos(ang)


            hits = eqthicks[np.where(eqthicks > 0)]
            hitper = len(hits) / n
            meanthick = np.mean(hits)
            try:
                perc = [np.percentile(hits, per) for per in self.percarr]
            except Exception as e:
                #print(hits,len(hits))
                perc = [np.percentile([0], per) for per in self.percarr]

            result = planeids, eqthicks, ang, meanthick, perc, hitper
            self.eqthicks = eqthicks
            self.angles = ang
            self.meanthick = meanthick
            self.percentiles = perc
            self.hitpercentage = hitper
        else:
            result = ["NONE"]
            self.eqthicks = shotthicks#"None"
            self.angles = "None"
            self.meanthick = "None"
            self.percentiles= "None"
            self.hitpercentage = "None"

        self.eqthicks[np.isnan(self.eqthicks)]=0

        return result

    def getintersections(self):
        shotnormals,shotthickness,orgs = self.shotNTO
        extorgs = np.pad(orgs, (0, 1), 'constant', constant_values=(1))[:-1]
        multorg = (np.matmul(extorgs, self.mvMat))[:, :-1]

        extnorms = np.pad(shotnormals, (0, 1), 'constant')[:-1]
        multnorms = (np.matmul(extnorms, self.mvMat))[:, :-1]

        nd = np.dot(multnorms, self.lookvec)
        ww = self.raystart - multorg
        si = -np.einsum('ij,ij->i', multnorms, ww) / nd
        psi = np.multiply(self.lookvec, si[:, np.newaxis]) + multorg + ww
        extpsi = np.pad(psi, (0, 1), 'constant', constant_values=(1))[:-1]
        multpsi = np.matmul(extpsi, np.linalg.inv(self.mvMat))[:, :-1]
        return psi,multpsi

    def getheatmapdata(self):
        heatmap = np.zeros(self.picdata.shape[:2])
        eqthicksclean = np.nan_to_num(self.eqthicks)
        heatmap[self.shotpoints[:, 0], self.shotpoints[:, 1]] = eqthicksclean
        return heatmap
