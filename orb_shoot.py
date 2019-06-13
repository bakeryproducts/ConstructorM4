from PyQt5 import QtCore, QtGui, QtWidgets
from UI.pys.orb_shoot import Ui_Form
from clShotProcessing import ShotProcessing
from clArmorSurface import ArmorSurface

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.ticker import PercentFormatter
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

import matplotlib.colors as mcolors


import numpy as np
np.seterr(divide='ignore', invalid='ignore')
import time
import math, random

class orb_shoot(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(orb_shoot, self).__init__(parent)
        self.setupUi(self)
        self.meanthick = []
        self.percparam = 0, 100, 101
        self.probx, self.proby = 0, 0

        self.btn_start.clicked.connect(self.act_btn_start)
        self.btn_grid.clicked.connect(self.act_btn_grid)
        self.btn_power.clicked.connect(self.act_btn_power)

        # self.tbl_res.itemSelectionChanged.connect(self.tblresselect)

        self.tbtn_filepath.clicked.connect(self.act_savefile)

        # self.tbl_res.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        # self.tbl_res.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        # self.tbl_res.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        # self.tbl_res.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
        # self.tbl_res.horizontalHeader().setResizeMode(4, QtGui.QHeaderView.ResizeToContents)
        # self.tbl_res.horizontalHeader().setResizeMode(5, QtGui.QHeaderView.ResizeToContents)
        # self.tbl_res.horizontalHeader().setResizeMode(6, QtGui.QHeaderView.ResizeToContents)
        # self.tbl_res.horizontalHeader().setResizeMode(7, QtGui.QHeaderView.ResizeToContents)
        # self.tbl_res.horizontalHeader().setResizeMode(8, QtGui.QHeaderView.ResizeToContents)
        # self.tbl_res.horizontalHeader().setResizeMode(9, QtGui.QHeaderView.ResizeToContents)

        self.tbl_res.hideColumn(9)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.tab_1.setLayout(layout)

        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.toolbar2 = NavigationToolbar(self.canvas2, self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar2)
        layout.addWidget(self.canvas2)
        self.tab_2.setLayout(layout)

        self.figure3 = Figure()
        self.canvas3 = FigureCanvas(self.figure3)
        self.toolbar3 = NavigationToolbar(self.canvas3, self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar3)
        layout.addWidget(self.canvas3)
        # self.tab_3.setLayout(layout)
        self.widget.setLayout(layout)

    def loadinit(self, mainw):
        self.probdict = {0: np.random.normal, 1: np.random.uniform,
                         2: np.random.standard_t,
                         3: np.random.exponential, 4: np.random.lognormal,
                         5: np.random.chisquare}

        self.ln_savefile.setText('RESULTS/orb_results.csv')

        self.mainwindow = mainw
        self.mainwindow.glwidget.crosscdinit()
        self.mainwindow.glwidget.crossinit()

        self.mainwindow.glwidget.AngleChange.connect(self.anglesignal)

    def anglesignal(self,arg):
        self.ln_angle1.setText(str(round(arg[0])))
        self.ln_angle2.setText(str(round(arg[1])))

    def probdet(self):
        i, j = self.tab_prx.currentIndex(), self.tab_pry.currentIndex()
        xparams, yparams = [], []
        wx, wy = self.tab_prx.widget(i), self.tab_pry.widget(j)
        chsx, chsy = wx.children(), wy.children()

        for chx, chy in zip(chsx, chsy):
            if isinstance(chx, QtWidgets.QLineEdit):
                xparams.append(float(chx.text()))
            if isinstance(chy, QtWidgets.QLineEdit):
                yparams.append(float(chy.text()))
        prx, pry = self.getdist(i), self.getdist(j)

        w = self.mainwindow.glwidget.wi
        h = self.mainwindow.glwidget.he

        if i == 0:
            xparams = [w / 2 + float(self.ln_xnrmu.text()), float(self.ln_xnrsigma.text())]
        if j == 0:
            yparams = [h / 2 - float(self.ln_ynrmu.text()), float(self.ln_ynrsigma.text())]

        if i == 1:
            xparams = [w / 2 + float(self.ln_unixlow.text()), w / 2 + float(self.ln_unixhigh.text())]
        if j == 1:
            yparams = [h / 2 - float(self.ln_uniylow.text()), h / 2 - float(self.ln_uniyhigh.text())]

        return prx, pry, xparams, yparams

    def getdist(self, t):
        try:
            dist = self.probdict[t]
        except:
            print('NOT AVAILABLE')
            dist = self.probdict[0]
        return dist

    def act_btn_start(self):
        self.mainwindow.glwidget.dropsphs()
        self.mainwindow.glwidget.droplines()
        self.mainwindow.glwidget.sphinit()
        self.mainwindow.glwidget.lineinit()

        #self.checkedplanes = self.genplanesdict()

        if self.rdb_degorbit.isChecked():
            self.startshow()
            return
        elif self.rdb_regorbit.isChecked():
            self.regularshow()
            return

            # self.results = res
            # self.resultsconvert()

    def startshow(self):
        timestart = time.time()

        hedge = {}
        a, b = int(self.ln_gastep.text()), int(self.ln_nastep.text())  # 2, 2
        x0, y0 = int(self.ln_grang0.text()), int(self.ln_norang0.text())
        fxang1, fyang1 = int(self.ln_grang1.text()), int(self.ln_norang1.text())  # 360, 90
        xang, yang = int( (fxang1-x0) / a), int( (fyang1-y0) / b)
        xi, yi = a , b
        mv = self.mainwindow.glwidget.mvMatrix
        #for comp in self.mainwindow.components:
        meanth,hits,perc,al,be = self.generatedata(x0,y0,xang,xi,yang,yi,mv)

        #print(meanth,'\n',be)

        # x, y, z = [], [], []
        # for a, b, r in zip(al, be, meanth):
        #     ix,iy,iz = r * np.cos(b) * np.sin(a),r * np.cos(b) * np.cos(a),r * np.sin(b)
        #     x.append(ix)
        #     y.append(iy)
        #     z.append(iz)

        pe = [[] for i in range(self.percparam[2])]
        for p in perc:
            [pe[i].append(p[i]) for i in range(len(p))]
            # pe[0].append(p[0])
            # pe[1].append(p[len(p)//2])
            # pe[2].append(p[-5])

        #self.surfaceinit((al,be,meanth),xi,yi,'TMT')
        # [self.surfaceinit((al,be,p),xi,yi,str(i)+'PERC') for i,p in enumerate(pe)]

        self.perc = perc
        self.shape = (xang,yang+1)
        self.genheatmap(perc,self.shape)
        self.genangleprob(perc,self.shape)

        self.tbl_res.setRowCount(0)
        for i, currthick, hitperc in zip(range(len(meanth)),meanth,hits):
            currthick, hitperc = round(currthick, 1), round(hitperc, 2)
            self.newrow(str(i), str(hitperc), str(currthick), '-', '-', '-', '-', '-', '-', '-')

        # self.figure.clear()
        # ax = Axes3D(self.figure)
        # ax.set_xlabel('Thickness, mm')
        # ax.set_ylabel('Thickness, mm')
        # ax.set_title('Surface of mean thickness')
        # ax.clear()
        # ax.scatter(x, y, z, '*-')
        # self.canvas.draw()

        self.drawhist(pe)

        savefile = self.ln_savefile.text()

        with open(savefile, 'w') as f:
            for a,b,t in zip(al,be,meanth):
                f.write(str(a) + ','+ str(b) + ',' + str(t) + '\n')
                # print(k,' -> ',v)

        n = int(self.ln_n.text())
        self.mainwindow.glwidget.addtoconsole('Results saved to ' + savefile)
        self.mainwindow.glwidget.addtoconsole(
            'Took ' + str(n * xang * yang) + ' shots in ' + str(round(time.time() - timestart, 2)) + ' seconds.')

        self.mainwindow.glwidget.upmat()

        print(time.time() - timestart)
        print(xang * yang)

    def surfaceinit(self,points,a,b,name):
        AS = ArmorSurface(points,(a,b),name)
        AS.crecomp()
        #AS.comp.defmatinit(list(self.mainwindow.materials)[0])
        self.mainwindow.pushcomponent(AS.comp, 'SURFACE')
        self.mainwindow.glwidget.upmat()

    def gendistpoints(self):
        num = int(self.ln_n.text())
        prx, pry, xparams, yparams = self.probdet()
        w = self.mainwindow.glwidget.wi
        h = self.mainwindow.glwidget.he
        sx = prx(*xparams, num)
        sy = pry(*yparams, num)
        # condx = abs(sx - w / 2) < w / 2 - 1
        # condy = abs(sy - h / 2) < h / 2 - 1
        # cond = condx*condy
        cond = (sx < w / 2) & (sx > -w / 2) & (sy < h / 2) & (sy > -h / 2)
        # sx = (sx[cond]).astype(int)
        # sy = (sy[cond]).astype(int)
        shotpoints = np.transpose([sy, sx])[cond].astype(np.int)
        #shotpoints = np.unique(shotpoints, axis=0)
        return num,shotpoints#[sx,sy]

    def generatedata(self,x0,y0,xang,xi,yang,yi,mv):
        nbuf=3
        w = self.mainwindow.glwidget.wi
        h = self.mainwindow.glwidget.he
        ycum,cnt = y0,0
        n,shotpoints = self.gendistpoints()
        NTO = []
        allperc = []
        comps = self.mainwindow.components
        eqthicks,eqthick_model = [],[]
        p0, p1, pn = self.percparam
        percarr = np.linspace(p0, p1, num=pn)

        for comp in comps:
            cnorms,ceqthicks,corgs = self.gennorms(comp)
            #print(cnorms.shape,ceqthicks.shape,corgs.shape)
            NTO.append((cnorms,ceqthicks,corgs))
        # print(NTO[0].shape)

        meanth,mehits,al,be = [],[],[],[]
        cn = len(comps)
        st = time.time()
        sps = []
        buf_count=0
        print(x0,y0)
        for j in range(yang + 1):
            xcum = x0
            for i in range(xang):
                self.mainwindow.glwidget.mvMatrix = mv
                xcum += xi

                self.mainwindow.glwidget.rot(xcum, ycum)
                m = self.mainwindow.glwidget.mvMatrix
                self.mainwindow.glwidget.updateGL()


                for indbuf,comp,nto in zip(range(cn),comps,NTO):
                    print(f'COMP_{comp}')
                    self.mainwindow.glwidget.writepic(buf_count, comp.geoobj)
                    # self.mainwindow.glwidget.writepic(0, comp.geoobj)
                    data = self.mainwindow.glwidget.readpic(buf_count)
                    # print(data.shape)
                    # print(data[0])
                    # break
                    # if buf_count == 2:
                    #     for b_c in range(2):
                    #         # rot_time = time.time()
                    #         data = self.mainwindow.glwidget.readpic(b_c)
                    #         # sps.append(time.time() - rot_time)
                    #         SP = ShotProcessing(data, shotpoints, nto, m, (w, h), self.percparam)
                    #         SP.getmaindata(80.0)
                    #         meanthick = SP.meanthick
                    #         hitper = SP.hitpercentage
                    #         perc = SP.percentiles
                    #
                    #         al.append(xcum * np.pi / 180)
                    #         be.append(ycum * np.pi / 180)
                    #         meanth.append(meanthick)
                    #         mehits.append(hitper)
                    #         allperc.append(perc)
                    #         cnt += 1
                    #     buf_count = 0
                    # else:
                    #     buf_count+=1

                    SP = ShotProcessing(data, shotpoints, nto, m, (w, h),self.percparam)
                    SP.getmaindata(80.0)
                    # meanthick = SP.meanthick
                    # hitper = SP.hitpercentage
                    # perc = SP.percentiles
                    print(SP.eqthicks)
                    eqthick_model.append(SP.eqthicks)



                al.append(xcum * np.pi / 180)
                be.append(ycum * np.pi / 180)

                eqthick_model = np.array(eqthick_model).sum(axis=0)
                eqthicks.append(eqthick_model)

                hits = eqthick_model[np.where(eqthick_model > 0)]
                hitper = len(hits) / n
                print(f'HITPERC_{hitper}s')
                meanthick = np.mean(hits)
                try:
                    perc = [np.percentile(hits, per) for per in percarr]
                except Exception as e:
                    perc = [np.percentile([0], per) for per in self.percarr]
                # result = planeids, eqthicks, ang, meanthick, perc, hitper

                eqthick_model = []

                meanth.append(meanthick)
                mehits.append(hitper)
                allperc.append(perc)
                print(f'{cnt} ######### ',end='')
                print(hits,hitper,meanthick)
                cnt+=1


            ycum += yi

        print(time.time()-st,(time.time()-st)/cnt)
        print(cnt)
        print(np.array(eqthicks).shape)
        #print(allperc)
        return meanth,mehits,allperc,al,be

    def newrow(self, n, perc, thick, tap, tat, tbp, tbt, tcp, tct, ci):
        rowPosition = self.tbl_res.rowCount()
        self.tbl_res.insertRow(rowPosition)
        item1 = QtWidgets.QTableWidgetItem(n)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item2 = QtWidgets.QTableWidgetItem(perc)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item3 = QtWidgets.QTableWidgetItem(thick)
        item3.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item3.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item4 = QtWidgets.QTableWidgetItem(tap)
        item4.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item4.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item5 = QtWidgets.QTableWidgetItem(tat)
        item5.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item5.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item6 = QtWidgets.QTableWidgetItem(tbp)
        item6.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item6.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item7 = QtWidgets.QTableWidgetItem(tbt)
        item7.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item7.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item8 = QtWidgets.QTableWidgetItem(tcp)
        item8.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item8.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item9 = QtWidgets.QTableWidgetItem(tct)
        item9.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item9.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item10 = QtWidgets.QTableWidgetItem(ci)
        item10.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item10.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        self.tbl_res.setItem(rowPosition, 0, item1)
        self.tbl_res.setItem(rowPosition, 1, item2)
        self.tbl_res.setItem(rowPosition, 2, item3)
        self.tbl_res.setItem(rowPosition, 3, item4)
        self.tbl_res.setItem(rowPosition, 4, item5)
        self.tbl_res.setItem(rowPosition, 5, item6)
        self.tbl_res.setItem(rowPosition, 6, item7)
        self.tbl_res.setItem(rowPosition, 7, item8)
        self.tbl_res.setItem(rowPosition, 8, item9)
        self.tbl_res.setItem(rowPosition, 9, item10)

    def newrowtot(self, n, arr):
        rowPosition = self.tbl_tot.rowCount()
        self.tbl_tot.insertRow(rowPosition)
        item1 = QtWidgets.QTableWidgetItem(n)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        strarr = str(arr)
        item2 = QtWidgets.QTableWidgetItem(strarr)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        self.tbl_tot.setItem(rowPosition, 0, item1)
        self.tbl_tot.setItem(rowPosition, 1, item2)

    def resultsconvert(self):

        shotdict = {}
        self.tbl_res.setRowCount(0)
        res, inters, arrinter = self.results
        types = self.gettype(arrinter)
        # return
        for r in res:
            for ind, shot in enumerate(r):
                objid, faceid, ang, eqthick = shot
                objid, faceid = int(objid), int(faceid)

                if faceid != 0:
                    comp = self.mainwindow.components[objid]
                    cname = comp.getname()
                    face = comp.getfacesnames()[faceid - 1]
                    mat = comp.matarr[faceid - 1]
                    nthick = comp.thickarr[faceid - 1]
                    thick = str(nthick)
                    eqthick = str(round(eqthick, 1))
                    ang = str(round(ang * 180 / np.pi, 1))
                    res = 'None'
                    typep = 'T'  # types[ind]
                    ci = str(list(inters[objid, ind]))
                    if ind in shotdict.keys():
                        shotdict[ind].append([cname, face, mat.getname(), thick, ang, eqthick, res, '--', ci])
                    else:
                        shotdict[ind] = [[cname, face, mat.getname(), thick, ang, eqthick, res, typep, ci]]
        self.settbltot(shotdict)

    def settbltot(self, shotdict):
        for k, vs in shotdict.items():
            for i, v in enumerate(vs):
                if i == 0:
                    self.newrow(str(k), *v)
                else:
                    self.newrow('', *v)

                    # self.newrowtot(str(k), v)

    def tblresselect(self):
        if self.tbl_res.item(self.tbl_res.currentRow() + 1, -1):
            cistr = self.tbl_res.item(self.tbl_res.currentRow() + 1, -1).text()
            ci1, ci2 = self.lookp1 - self.lookp2 + eval(cistr), eval(cistr) + self.lookp2 - self.lookp1
            self.mainwindow.glwidget.droplines()
            self.mainwindow.glwidget.linecdlist.append([ci1, ci2])
            self.mainwindow.glwidget.lineinit()
            self.mainwindow.glwidget.upmat()

    def pointsgen(self, samples, randomize=True):
        rnd = 1.
        if randomize:
            rnd = random.random() * samples

        points = []
        offset = 2. / samples
        increment = math.pi * (3. - math.sqrt(5.))

        for i in range(samples):

            y = ((i * offset) - 1) + (offset / 2)
            r = math.sqrt(1 - pow(y, 2))

            phi = ((i + rnd) % samples) * increment

            x = math.cos(phi) * r
            z = math.sin(phi) * r

            scale = 5000
            if y >= 0:
                points.append(scale * np.array([x, y, z]))

        return points

    def gennorms(self,comp):
        n = len(comp.geoobj.faces)
        ns = np.zeros((n, 3))
        #ths = np.zeros(n)
        orgs = np.zeros((n, 3))
        for plid in range(n):
            ns[plid] = comp.geoobj.normals[3 * (plid)]
            orgs[plid] = comp.geoobj.points[comp.geoobj.faces[plid][0] - 1]
        ths = np.array(comp.thickarr)
        return ns, ths, orgs

    def act_savefile(self):
        filedialog = QtWidgets.QFileDialog(self)
        file,_ = filedialog.getSaveFileName(self, "Save resulting file as", "RESULTS\\results.csv",
                                          filter="csv (*.csv *.)")
        if file:
            self.lineEdit_5.setText(file)

    def gettype(self, arrinter):
        shotsuni = np.swapaxes(arrinter, 0, 1)
        # fsv = self.fsv
        # print('GOT FSV: ',fsv)
        shotsind = (-shotsuni)[:, :, 2].argsort()
        shotsrecomb = np.array([shotsuni[i, t] for i, t in enumerate(shotsind)])
        res = {}

        for i, shot in enumerate(shotsrecomb):
            cumvec = []
            cumth = 0
            shotres = 'none'
            sharr = 'NONE'
            print(shot)
            continue
            for n, o, z, t, d in shot:
                if t != 0 and t != np.nan:
                    cumvec.append(int(o))
                    cumth += t
                    # print(cumvec)
                    if self.mainwindow.fsvact(cumvec):  # self.getevalfsv(cumvec):
                        shotres = 'TYPE A: ' + str(cumth) + ' mm.'
                        sharr = (str(cumth) + ' mm')
                        res[int(n)] = sharr
                        break

                res[n] = sharr

                # print('Shot #',i,': ',shotres)
        # print(res)
        return res

    def closeEvent(self, event):
        self.mainwindow.glwidget.dropsphs()
        self.mainwindow.glwidget.droplines()
        self.mainwindow.glwidget.dropcross()
        self.mainwindow.glwidget.crossinit()
        self.mainwindow.glwidget.lineinit()
        self.mainwindow.glwidget.sphinit()

        event.accept()

    def act_btn_grid(self):
        self.btn_grid.blockSignals(True)
        if self.btn_grid.isChecked():
            if self.rdb_regorbit.isChecked():
                pnum = 2 * int(self.ln_regpoints.text())
                points = list(reversed(self.pointsgen(pnum)))
                lcds = [[(0,0,0),p] for p in points]
                self.mainwindow.glwidget.sphcdlist = points
                self.mainwindow.glwidget.sphinit()
                self.mainwindow.glwidget.linecdlist = lcds
                self.mainwindow.glwidget.lineinit(thick=1)
                self.mainwindow.glwidget.upmat()

            elif self.rdb_degorbit.isChecked():
                a, b = int(self.ln_gastep.text()), int(self.ln_nastep.text())  # 2, 2
                x0, y0 = int(self.ln_grang0.text()), int(self.ln_norang0.text())  # 360, 90
                fxang1, fyang1 = int(self.ln_grang1.text()), int(self.ln_norang1.text())  # 360, 90
                #xang, yang = int((fxang1 - x0) / a), int((fyang1 - y0) / b)
                points=[]
                r = 5000
                for j in range(fxang1-x0)[::a]:
                    for i in range(fyang1-y0+1)[::b]:
                        points.append([r*np.cos((y0+i)*np.pi/180)*np.sin((j+x0)*np.pi/180),
                                       r * np.sin((y0+i) * np.pi / 180),
                                       r * np.cos((y0+i) * np.pi / 180) * np.cos( (j+x0) * np.pi / 180)
                                       ])
                lcds = [[(0, 0, 0), p] for p in points]
                self.mainwindow.glwidget.sphcdlist = points
                self.mainwindow.glwidget.sphinit()
                self.mainwindow.glwidget.linecdlist = lcds
                self.mainwindow.glwidget.lineinit(thick=1)
                self.mainwindow.glwidget.upmat()


        else:
            self.mainwindow.glwidget.linecdlist = []
            self.mainwindow.glwidget.lineinit(thick=1)
            self.mainwindow.glwidget.sphcdlist=[]
            self.mainwindow.glwidget.sphinit()
            self.mainwindow.glwidget.upmat()
        self.btn_grid.blockSignals(False)

    def drawhist(self,data):
        self.figure2.clear()
        ax = self.figure2.add_subplot(111)
        ax.clear()
        ax.grid(True)
        ax.set_title('Resulting cumulative histograms')
        ax.set_xlabel('Thickness, mm')
        ax.set_ylabel('Directions, %')
        #leg = 10 * np.array([5, 5.5, 6, 6.5, 7,7.5, 8,8.5, 9,9.5])
        leg = np.linspace(*self.percparam)
        leg = ['Perc.: '+str(round(i,0))+'%' for i in leg]
        start = int(self.percparam[2]*.75)
        for ptext,dat in zip(leg[start::2],data[start::2]):
            ax.hist(dat,200,density=True,cumulative=True,alpha = .95,label=ptext)
        ax.yaxis.set_major_formatter(PercentFormatter(xmax=1))
        ax.legend()
        self.canvas2.draw()


        # objdepths = np.array(list(reversed(deparr[objind]))).reshape((-1, w))
            # objdepths = np.flip(objdepths, 1)
            # print(datad.shape,objdepths.shape)
            # with open('RESULTS\\depthtest.txt', 'w') as f:
            #     for i, row in enumerate(objdepths[0]):
            #         f.write(str(row) + ','+str(datad[0,i])+'\n')
            #         # for j,col in enumerate(row):
            #         #     f.write(str(j)+','+str(i)+','+str(col)+'\n')

    def genangleprob(self,perc,shape):
        pc = np.linspace(*self.percparam)
        heatmap = np.zeros((len(perc)))
        val = int(self.ln_power.text())
        for i, ps in enumerate(perc):
            for j, p in zip(pc, ps):
                if val < p:
                    heatmap[i] = j
                    break
            else:
                heatmap[i] = 100

        heatmap = np.flipud(heatmap.reshape(shape[::-1]))

        self.figure.clear()
        ax = self.figure.add_subplot(1, 1, 1)
        ax.clear()
        ax.set_title('Penetration probability for set SP, %')
        ax.set_xlabel('Ground angle, deg.')
        ax.set_ylabel('Normal angle, deg.')

        vmin, vmax = heatmap.min(), heatmap.max()
        extent = [int(s) for s in
                  [self.ln_grang0.text(), self.ln_grang1.text(), self.ln_norang0.text(), self.ln_norang1.text()]]
        im = ax.imshow(heatmap, cmap='jet', interpolation='gaussian', norm=mcolors.Normalize(vmin=vmin, vmax=vmax),extent = extent)

        # ‘none’, ‘nearest’, ‘bilinear’, ‘bicubic’, ‘spline16’, ‘spline36’, ‘hanning’, ‘hamming’, ‘hermite’, ‘kaiser’, ‘quadric’, ‘catrom’, ‘gaussian’, ‘bessel’, ‘mitchell’, ‘sinc’, ‘lanczos’
        self.tbl_tot.setRowCount(0)
        self.newrowtot(self.ln_power.text(), heatmap.mean())

        self.figure.colorbar(im)
        self.figure.tight_layout()
        self.canvas.draw()
        # img = Image.fromarray(np.uint8(ds), 'RGBA')
        # img.save('RESULTS\\heatmap.png', 'PNG')

    def genheatmap(self,perc,shape):
        pc = np.linspace(*self.percparam)
        heatmap = np.zeros((len(perc)))
        val = int(self.ln_power.text())
        for i,ps in enumerate(perc):
            for j,p in zip(pc,ps):
                #print(val,p)
                if val<p:
                    heatmap[i] = j
                    break
            else:
                heatmap[i] = 100


        heatmap = np.flipud(heatmap.reshape(shape[::-1]))

        self.figure3.clear()
        ax = self.figure3.add_subplot(1,2,1,projection='3d')#add_axes([0., 0., 1., .92, ])
        ax2 = self.figure3.add_subplot(1, 2, 2,projection='polar')
        ax2.clear()
        ax.clear()
        ax.set_title('Penetration probability for set SP, %')
        ax.set_xlabel('Ground angle, deg.')
        ax.set_ylabel('Normal angle, deg.')

        vmin, vmax = heatmap.min(), heatmap.max()
        # extent = [int(s) for s in [self.ln_grang0.text(),self.ln_grang1.text(),self.ln_norang0.text(),self.ln_norang1.text(),vmin,vmax]]
        # # im = ax.imshow(heatmap, cmap='jet', interpolation='gaussian', norm=mcolors.Normalize(vmin=vmin, vmax=vmax),extent = extent)
        x = np.linspace(0,360,heatmap.shape[0])#list(range(heatmap.shape[0]))
        y = np.linspace(0,90,heatmap.shape[1])#list(range(heatmap.shape[1]))

        xi,yi = int(self.ln_gastep.text()), int(self.ln_nastep.text())
        xt,yt = xi*list(x*np.pi/180),np.array([np.full((yi,),j) for j in y*np.pi/180]).flatten()
        #self.surfaceinit((xt,yt,heatmap.flatten()),xi,yi,'Mean')

        x,y, = np.meshgrid(x,y)
        surf = ax.plot_surface(x,y,np.transpose(heatmap),cmap=cm.jet,
                       linewidth=0, antialiased=True)

        cset = ax.contourf(x,y,np.transpose(heatmap), zdir='z', offset=vmin-10, cmap=cm.coolwarm)
        cset = ax.contourf(x,y,np.transpose(heatmap), zdir='x', offset=-140, cmap=cm.coolwarm)
        cset = ax.contourf(x,y,np.transpose(heatmap), zdir='y', offset=-40, cmap=cm.coolwarm)
        ax.set_xlim(-140, 360)
        ax.set_ylim(-40, 90)
        ax.set_zlim(vmin-10, vmax)

        pitch0,pitch1 = int(self.ln_norang0.text()),int(self.ln_norang1.text())
        pitchlen = heatmap.shape[0]
        pitchangs = np.linspace(pitch0,pitch1,pitchlen)
        grang0,grang1 = int(self.ln_grang0.text()),int(self.ln_grang1.text())
        for i,ang in enumerate(pitchangs):
            if i%7==0 and i<pitchlen/2:
                r = heatmap[-i-1]
                r = np.insert(r,0,r[0])
                theta = np.linspace(grang0*np.pi/180,grang1*np.pi/180,len(r))#2*np.pi*np.arange(len(r))/(len(r)-1)
                ax2.plot(theta,r,lw=3,label='Pitch angle = '+str(round(ang))+'deg.')
                ax2.fill(theta,r,alpha=.3)
        ax2.set_rmax(100)
        ax2.set_rlabel_position(180)
        ax2.set_title('Penetration probability, %')
        ax2.set_rticks(list(np.arange(0,100,10)))
        ax2.grid(color='k')
        ax2.legend(loc = 'lower right',
          fancybox=True, shadow=True)

        self.tbl_tot.setRowCount(0)
        self.newrowtot(self.ln_power.text(),heatmap.mean())

        # self.figure3.colorbar(im)
        # self.figure3.tight_layout()
        self.canvas3.draw()
        # img = Image.fromarray(np.uint8(ds), 'RGBA')
        # img.save('RESULTS\\heatmap.png', 'PNG')

    def act_btn_power(self):
        self.genheatmap(self.perc,self.shape)
