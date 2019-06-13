from PyQt5 import QtCore, QtGui, QtWidgets
from UI.pys.dir_shoot import Ui_Form
from clShotProcessing import ShotProcessing

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.ticker import PercentFormatter
from matplotlib.figure import Figure
#from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mcolors

from scipy import ndimage
import numpy as np
import time


class dir_shoot(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(dir_shoot, self).__init__(parent)
        self.setupUi(self)

        self.meanthick = []
        self.percparam = 0, 100, 41
        self.probx, self.proby = 0, 0

        self.btn_start.clicked.connect(self.act_btn_start)

        self.btn_convcheck.clicked.connect(self.testconv)

        self.tbl_res.itemSelectionChanged.connect(self.tblresselect)

        self.tbtn_filepath.clicked.connect(self.act_savefile)

        # self.tbl_res.horizontalHeader().setResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        # self.tbl_res.horizontalHeader().setResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        # self.tbl_res.horizontalHeader().setResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        # self.tbl_res.horizontalHeader().setResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        # self.tbl_res.horizontalHeader().setResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        # self.tbl_res.horizontalHeader().setResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        # self.tbl_res.horizontalHeader().setResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        # self.tbl_res.horizontalHeader().setResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        # self.tbl_res.horizontalHeader().setResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
        # self.tbl_res.horizontalHeader().setResizeMode(9, QtWidgets.QHeaderView.ResizeToContents)

        self.tbl_res.hideColumn(7)

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
        layout2 = QtWidgets.QVBoxLayout()
        layout2.addWidget(self.toolbar2)
        layout2.addWidget(self.canvas2)
        self.tab_2.setLayout(layout2)

        self.figure3 = Figure()
        self.canvas3 = FigureCanvas(self.figure3)
        self.toolbar3 = NavigationToolbar(self.canvas3, self)
        layout3 = QtWidgets.QVBoxLayout()
        layout3.addWidget(self.toolbar3)
        layout3.addWidget(self.canvas3)
        self.tab_3.setLayout(layout3)



    def loadinit(self, mainw):
        self.probdict = {0: np.random.normal, 1: np.random.uniform,
                         2: np.random.standard_t,
                         3: np.random.exponential, 4: np.random.lognormal,
                         5: np.random.chisquare}

        self.ln_savefile.setText('RESULTS\\results.csv')
        self.mainwindow = mainw
        self.mainwindow.glwidget.crosscdinit()
        self.mainwindow.glwidget.crossinit()

        self.mainwindow.glwidget.AngleChange.connect(self.anglesignal)

    def act_btn_start(self):
        self.mainwindow.glwidget.dropsphs()
        self.mainwindow.glwidget.droplines()
        self.mainwindow.glwidget.sphinit()
        self.mainwindow.glwidget.lineinit()

        num = int(self.ln_n.text())
        prx, pry, xparams, yparams = self.probdet()
        res = self.shoots(prx, pry, xparams, yparams, num)

        self.lookp1 = np.matmul(self.mainwindow.glwidget.mvMatrix, (0, 0, -25000, 1))[:3]
        self.lookp2 = np.matmul(self.mainwindow.glwidget.mvMatrix, (0, 0, 25000, 1))[:3]
        self.mainwindow.glwidget.addtoconsole('Single direction shooting: taking ' + str(num)+' shots via:')
        self.mainwindow.glwidget.upmat()

        if self.chb_results.isChecked():
            self.results = res
            self.resultsconvert()

    def act_savefile(self):
        filedialog = QtWidgets.QFileDialog(self)
        file,_ = filedialog.getSaveFileName(self, "Save resulting file as", "RESULTS/results.csv",
                                          filter="csv (*.csv *.)")
        if file:
            self.ln_savefile.setText(file)

    def testconv(self):
        self.mainwindow.glwidget.dropsphs()
        self.mainwindow.glwidget.droplines()
        self.mainwindow.glwidget.sphinit()
        self.mainwindow.glwidget.lineinit()

        n0 = 1000  # int(self.ln_n.text())
        n1 = int(self.ln_convcheck.text())
        num = int(self.ln_partition.text())#15
        reps = int(self.ln_reps.text())#20
        vars = np.linspace(n0,n1,num,dtype=int)
        prx, pry, xparams, yparams = self.probdet()
        thicks = np.zeros((num,reps))
        for i,var in enumerate(vars):
            for j in range(reps):
                thicks[i,j] = self.shoottest(prx, pry, xparams, yparams, var)
        print(thicks)
        mean = np.mean(thicks)
        vs = np.mean(np.abs(thicks-mean)**2,axis=1)
        vmeans = np.mean(thicks,axis=1)
        stds = np.sqrt(vs)
        vhi = vmeans+2*stds
        vlo = vmeans-2*stds
        print(vs)

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.set_title('Convergence of eq. thicknesses for number of shots, mm')
        ax.plot(vars, vhi, '^-',label='Higher')
        ax.plot(vars, vlo, 'o-',label='Lower')
        ax.fill_between(vars,vhi,vlo,alpha=.3,color='g')
        ax.plot(vars, vmeans, '*-',label='Mean',color='b')
        [ax.scatter(reps*[v],thicks[i],s=2,color='k') for i,v in enumerate(vars)]
        ax.grid(True)
        ax.legend()
        self.canvas.draw()

        self.figure2.clear()
        ax = self.figure2.add_subplot(111)
        ax.clear()
        ax.set_title('Standart deviations, mm')
        ax.plot(vars, np.sqrt(vs), '*-', label='Expanding STD')
        #ax.plot(vars, stdr, 'o-', label='Rolling STD, window = 3')
        ax.grid(True)
        ax.legend()
        # ax.plot(hedge.keys(), mawthick, 'o-')

        self.canvas2.draw()

        return

    def tblresselect(self):
        if self.tbl_res.item(self.tbl_res.currentRow() + 1, -1):
            cistr = self.tbl_res.item(self.tbl_res.currentRow() + 1, -1).text()
            ci1, ci2 = self.lookp1 - self.lookp2 + eval(cistr), eval(cistr) + self.lookp2 - self.lookp1
            self.mainwindow.glwidget.droplines()
            self.mainwindow.glwidget.linecdlist.append([ci1, ci2])
            self.mainwindow.glwidget.lineinit()
            self.mainwindow.glwidget.upmat()

    def anglesignal(self, arg):
        self.ln_angle1.setText(str(round(arg[0])))
        self.ln_angle2.setText(str(round(arg[1])))



    def probdet(self):
        # self.probx,self.proby
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

        xst,yst = '',''

        if i == 0:
            mu = self.ln_xnrmu.text()
            sig = self.ln_xnrsigma.text()
            xparams = [w / 2 + float(mu), float(sig)]
            xst = 'X-axis distribution: Normal('+mu+', '+sig+')'
        if j == 0:
            mu = self.ln_ynrmu.text()
            sig = self.ln_ynrsigma.text()
            yparams = [h / 2 - float(mu), float(sig)]
            yst = 'Y-axis distribution: Normal(' + mu + ', ' + sig + ')'

        if i == 1:
            low = self.ln_unixlow.text()
            high = self.ln_unixhigh.text()
            xparams = [w / 2 + float(low), w / 2 + float(high)]
            xst = 'X-axis distribution: Uniform(' + low + ', ' + high + ')'
        if j == 1:
            low = self.ln_uniylow.text()
            high = self.ln_uniyhigh.text()
            yparams = [h / 2 - float(low), h / 2 - float(high)]
            yst = 'Y-axis distribution: Uniform(' + low + ', ' + high + ')'

        self.mainwindow.glwidget.addtoconsole('\t'+xst+'; '+yst)

        return prx, pry, xparams, yparams

    def getdist(self, t):
        try:
            dist = self.probdict[t]
        except:
            print('NOT AVAILABLE')
            dist = self.probdict[0]
        return dist

    def shoots(self, prx, pry, xparams, yparams, n):
        w = self.mainwindow.glwidget.wi
        h = self.mainwindow.glwidget.he

        start = time.time()
        sx = prx(*xparams, n)
        sy = pry(*yparams, n)
        condx = abs(sx - w / 2) < w / 2 - 1
        condy = abs(sy - h / 2) < h / 2 - 1
        cond = condx * condy
        sx = (sx[cond]).astype(int)
        sy = (sy[cond]).astype(int)
        shotpoints = np.transpose([sy, sx])
        shotpoints = np.unique(shotpoints, axis=0)

        n = shotpoints.shape[0]
        print('SHP generated:', shotpoints.shape)
        comps = self.mainwindow.components
        m = self.mainwindow.glwidget.mvMatrix
        arrinter = np.zeros((len(comps), n, 5))
        inters = np.zeros((len(comps), n, 3))
        results = np.zeros((len(comps), n, 4))

        if self.chb_rico.isChecked():
            ricochet = float(self.ln_rico.text())
        else:
            ricochet=False

        sps = []
        for oind, comp in enumerate(comps):
            self.mainwindow.glwidget.writepic(0, comp.geoobj)
            data = self.mainwindow.glwidget.readpic(0)
            SP = ShotProcessing(data,shotpoints,self.gennorms(comp),m,(w,h),self.percparam)
            sps.append(SP)
            #planeids,eqthicks,ang,*r = SP.getmaindata(ricochet)
        eqthicks = np.zeros((n))
        for sp in sps:
            sp.getmaindata(ricochet)
            eqthicks+=sp.eqthicks

        hits = eqthicks[np.where(eqthicks > 0)]
        #hitper = len(hits) / n
        #meanthick = np.mean(hits)

        p0, p1, pn = self.percparam
        percarr = np.linspace(p0, p1, num=pn)

        perc = [np.percentile(hits, per) for per in percarr]
        self.genheatmap(eqthicks, shotpoints, (h, w))
        self.drawperc(perc)
        t = eqthicks[~np.isnan(eqthicks)]
        t = t[np.nonzero(t)]
        self.drawhist(t)

        # for oind, comp in enumerate(comps):
        #     self.mainwindow.glwidget.writepic(0, comp.geoobj)
        #     data = self.mainwindow.glwidget.readpic(0)
        #     SP = ShotProcessing(data,shotpoints,self.gennorms(comp),m,(w,h),self.percparam)
        #     planeids,eqthicks,ang,*r = SP.getmaindata(ricochet)
        #     psi,multpsi = SP.getintersections()
        #     depths = np.zeros((n))
        #     self.genheatmap(eqthicks, shotpoints, (h, w))
        #     self.drawperc(SP.percentiles)
        #     t = eqthicks[~np.isnan(eqthicks)]
        #     t = t[np.nonzero(t)]
        #     self.drawhist(t)
        #
        #     inters[oind] = multpsi
        #     results[oind] = np.transpose((np.full((n), oind), planeids, ang, eqthicks))
        #     arrinter[oind] = np.transpose(
        #         (np.array(range(n)), np.full((n), oind), np.round(psi[:, -1], 2), eqthicks, depths))



        print(n, ': ', time.time() - start)


        # if self.chb_results.isChecked():
        #     t1 = inters.flatten()
        #     t1 = inters[~np.isnan(inters)]
        #     t = list(t1.reshape((-1, 3)))
        #     self.mainwindow.glwidget.sphcdlist = t[:int(self.ln_resultsn.text())]
        #     self.mainwindow.glwidget.sphinit(r=3)
        #     self.mainwindow.glwidget.upmat()

        return [results, inters, arrinter]

    def genheatmap(self,eqthicks,shotpoints,shape):

        thicks = eqthicks
        heatmap = np.zeros(shape)
        alpha = np.nan_to_num(thicks)
        heatmap[shotpoints[:, 0], shotpoints[:, 1]] = alpha
        if self.chb_interpolation.isChecked():
            size = int(self.ln_interpolation.text())
            heatmap = ndimage.uniform_filter(heatmap, size=size, mode='constant')

        self.figure.clear()
        ax = self.figure.add_axes([0., 0., 1., .95, ])
        ax.clear()
        ax.set_title('Equivalent thickness, mm')
        if self.chb_range.isChecked():
            vmin, vmax = float(self.ln_rangelow.text()), float(self.ln_rangehigh.text())
        else:
            vmin, vmax = heatmap.min(), .5 * heatmap.max()

        im = ax.imshow(heatmap, cmap='CMRmap', interpolation='bicubic', norm=mcolors.Normalize(vmin=vmin, vmax=vmax))
        # ‘none’, ‘nearest’, ‘bilinear’, ‘bicubic’, ‘spline16’, ‘spline36’, ‘hanning’, ‘hamming’, ‘hermite’, ‘kaiser’, ‘quadric’, ‘catrom’, ‘gaussian’, ‘bessel’, ‘mitchell’, ‘sinc’, ‘lanczos’
        ax.axis('off')
        self.figure.colorbar(im)
        self.figure.tight_layout()
        self.canvas.draw()
        # img = Image.fromarray(np.uint8(ds), 'RGBA')
        # img.save('RESULTS\\heatmap.png', 'PNG')

    def drawhist(self,data):
        self.figure3.clear()
        ax = self.figure3.add_subplot(111)
        ax.clear()
        ax.grid(True)
        ax.set_title('Resulting cumulative histograms')
        ax.set_xlabel('Thickness, mm')
        ax.set_ylabel('Directions, %')
        #leg = 10 * np.array([5, 5.5, 6, 6.5, 7,7.5, 8,8.5, 9,9.5])
        ax.hist(data,80)
        ax.yaxis.set_major_formatter(PercentFormatter(xmax=len(data)))
        ax.legend()
        self.canvas3.draw()

    def gennorms(self, comp):
        n = len(comp.geoobj.faces)
        ns = np.zeros((n, 3))
        #ths = np.zeros(n)
        orgs = np.zeros((n, 3))
        for plid in range(n):
            ns[plid] = comp.geoobj.normals[3 * (plid)]
            orgs[plid] = comp.geoobj.points[comp.geoobj.faces[plid][0] - 1]
        ths = np.array(comp.thickarr)
        return ns, ths, orgs

    def drawperc(self,perc):
        self.figure2.clear()
        ax = self.figure2.add_subplot(121)
        ax2 = self.figure2.add_subplot(122)
        ax.clear()
        ax2.clear()

        ax.grid(True)
        ax.set_title('Thickness percentiles, mm')
        perctext = np.linspace(self.percparam[0],self.percparam[1],num=self.percparam[2])
        #perctext = [str(round(i, 0)) + '%' for i in perctext]
        ax.plot(perctext,perc, 'o-')

        # w,h,eqthicks = surfparam
        # x = np.arange(w)
        # y = np.arange(h)
        # x, y, = np.meshgrid(x, y)
        # surf = ax2.plot_surface(x, y, eqthicks.reshape((w,h)))

        self.canvas2.draw()

    def shoottest(self, prx, pry, xparams, yparams, n):
        w = self.mainwindow.glwidget.wi
        h = self.mainwindow.glwidget.he

        start = time.time()
        sx = prx(*xparams, n)
        sy = pry(*yparams, n)
        condx = abs(sx - w / 2) < w / 2 - 1
        condy = abs(sy - h / 2) < h / 2 - 1
        cond = condx * condy
        sx = (sx[cond]).astype(int)
        sy = (sy[cond]).astype(int)
        shotpoints = np.transpose([sy, sx])
        # shotpoints = np.unique(shotpoints, axis=0)
        n = shotpoints.shape[0]

        print('SHP generated:', shotpoints.shape)
        comps = self.mainwindow.components
        m = self.mainwindow.glwidget.mvMatrix

        if self.chb_rico.isChecked():
            ricochet = float(self.ln_rico.text())
        else:
            ricochet = False

        for oind, comp in enumerate(comps):
            self.mainwindow.glwidget.writepic(0, comp.geoobj)
            data = self.mainwindow.glwidget.readpic(0)
            SP = ShotProcessing(data, shotpoints, self.gennorms(comp), m, (w, h),self.percparam)
            planeids, eqthicks, ang, *r = SP.getmaindata(ricochet)

        hits = eqthicks[np.where(eqthicks > 0)]
        meanthick = np.mean(hits)
        return meanthick

    def resultsconvert(self):

        res, inters, arrinter = self.results

        shotdict = {}
        self.tbl_res.setRowCount(0)
        riccnt = 0
        th = []
        for r in res:
            for ind, shot in enumerate(r):
                objid, faceid, ang, eqthick = shot
                objid, faceid = int(objid), int(faceid)

                if faceid != 0:

                    if np.isnan(ang):
                        riccnt += 1
                    else:
                        th.append(eqthick)
                    comp = self.mainwindow.components[objid]
                    cname = comp.getname()
                    face = comp.getfacesnames()[faceid - 1]
                    #mat = comp.matarr[faceid - 1]
                    nthick = comp.thickarr[faceid - 1]
                    thick = str(nthick)
                    eqthick = str(round(eqthick, 1))
                    ang = str(round(ang * 180 / np.pi, 1))

                    ci = 'err'#str(list(inters[objid, ind]))
                    if ind in shotdict.keys():
                        shotdict[ind].append([cname, face, 'DEF_MAT', thick, ang, eqthick, ci])
                    else:
                        shotdict[ind] = [[cname, face, 'DEF_MAT', thick, ang, eqthick, ci]]
        self.settbltot(shotdict)

        self.tbl_tot.setRowCount(0)
        self.newrowtot('Hits:', len(shotdict.keys()))
        self.newrowtot('Hit perc:', round(len(shotdict.keys()) / int(self.ln_n.text()), 2))
        self.newrowtot('Mean eq.th:', round(np.mean(th), 2))
        self.newrowtot('Ricochet:', riccnt)
        self.newrowtot('Ric. prcnt:', round(riccnt / len(shotdict.keys()), 2))

    def newrow(self, n, obj, face, mat, thick, angle, eqthick, ci):
        rowPosition = self.tbl_res.rowCount()
        self.tbl_res.insertRow(rowPosition)
        item1 = QtWidgets.QTableWidgetItem(n)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item2 = QtWidgets.QTableWidgetItem(obj)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item3 = QtWidgets.QTableWidgetItem(face)
        item3.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item3.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item4 = QtWidgets.QTableWidgetItem(mat)
        item4.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item4.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item5 = QtWidgets.QTableWidgetItem(thick)
        item5.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item5.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item6 = QtWidgets.QTableWidgetItem(angle)
        item6.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item6.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item7 = QtWidgets.QTableWidgetItem(eqthick)
        item7.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item7.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item8 = QtWidgets.QTableWidgetItem(ci)
        item8.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item8.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        self.tbl_res.setItem(rowPosition, 0, item1)
        self.tbl_res.setItem(rowPosition, 1, item2)
        self.tbl_res.setItem(rowPosition, 2, item3)
        self.tbl_res.setItem(rowPosition, 3, item4)
        self.tbl_res.setItem(rowPosition, 4, item5)
        self.tbl_res.setItem(rowPosition, 5, item6)
        self.tbl_res.setItem(rowPosition, 6, item7)
        self.tbl_res.setItem(rowPosition, 7, item8)

    def newrowtot(self, n, arr):
        rowPosition = self.tbl_tot.rowCount()
        self.tbl_tot.insertRow(rowPosition)
        stn = str(n)
        item1 = QtWidgets.QTableWidgetItem(stn)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        strarr = str(arr)
        item2 = QtWidgets.QTableWidgetItem(strarr)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        self.tbl_tot.setItem(rowPosition, 0, item1)
        self.tbl_tot.setItem(rowPosition, 1, item2)

    def settbltot(self, shotdict):
        cnt = 0

        if self.chb_results.isChecked():
            savefile = self.ln_savefile.text()
            with open(savefile, 'w') as f:
                for k, v in shotdict.items():
                    f.write(v[-1][-1][1:-1] + ',' + str(v[-1][-2]) + '\n')

        for k, vs in shotdict.items():
            cnt += 1
            for i, v in enumerate(vs):
                if i == 0:
                    self.newrow(str(k), *v)
                else:
                    self.newrow('', *v)
            if cnt > 10000:
                break

    def closeEvent(self, event):
        self.mainwindow.glwidget.dropsphs()
        self.mainwindow.glwidget.droplines()
        self.mainwindow.glwidget.dropcross()
        self.mainwindow.glwidget.crossinit()
        self.mainwindow.glwidget.lineinit()
        self.mainwindow.glwidget.sphinit()

        event.accept()
