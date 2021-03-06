from scipy import ndimage
import numpy as np
import pandas as pd
import math, random
import re
from PIL import Image
from PIL import ImageOps
from CNST.techs import getangle
from clShotProcessing import ShotProcessing
from shootsettings_ui import Ui_shootset
import mathutils as mth
from time import time,sleep
from PyQt4 import QtCore, QtGui
from OpenGL.GL import *
import time

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.ticker import PercentFormatter
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mcolors

np.seterr(divide='ignore', invalid='ignore')

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_wid_stats(QtGui.QWidget):
    def __init__(self):
        super(Ui_wid_stats, self).__init__()
        self.setupUi(self)
        self.meanthick = []
        self.percparam = 0,100,41
        self.probx, self.proby = 0, 0

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(564, 772)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tab_graphs = QtGui.QTabWidget(Form)
        self.tab_graphs.setObjectName(_fromUtf8("tab_graphs"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.tab_graphs.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tab_graphs.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tab_graphs.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tab_graphs)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.tbl_res = QtGui.QTableWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_res.sizePolicy().hasHeightForWidth())
        self.tbl_res.setSizePolicy(sizePolicy)
        self.tbl_res.setMinimumSize(QtCore.QSize(200, 200))
        self.tbl_res.setObjectName(_fromUtf8("tbl_res"))
        self.tbl_res.setColumnCount(8)
        self.tbl_res.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tbl_res.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_res.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_res.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_res.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_res.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_res.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_res.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_res.setHorizontalHeaderItem(7, item)
        self.verticalLayout.addWidget(self.tbl_res)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout.addWidget(self.line_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_4.addWidget(self.label_7)
        self.ln_angle1 = QtGui.QLineEdit(Form)
        self.ln_angle1.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_angle1.sizePolicy().hasHeightForWidth())
        self.ln_angle1.setSizePolicy(sizePolicy)
        self.ln_angle1.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_angle1.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_angle1.setObjectName(_fromUtf8("ln_angle1"))
        self.horizontalLayout_4.addWidget(self.ln_angle1)
        self.label_27 = QtGui.QLabel(Form)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.horizontalLayout_4.addWidget(self.label_27)
        self.ln_angle2 = QtGui.QLineEdit(Form)
        self.ln_angle2.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_angle2.sizePolicy().hasHeightForWidth())
        self.ln_angle2.setSizePolicy(sizePolicy)
        self.ln_angle2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_angle2.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_angle2.setObjectName(_fromUtf8("ln_angle2"))
        self.horizontalLayout_4.addWidget(self.ln_angle2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.line_8 = QtGui.QFrame(Form)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.verticalLayout_2.addWidget(self.line_8)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_17 = QtGui.QLabel(Form)
        self.label_17.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_4.addWidget(self.label_17, 2, 0, 1, 1)
        self.label_18 = QtGui.QLabel(Form)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_4.addWidget(self.label_18, 0, 0, 1, 1)
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_4.addWidget(self.line_2, 1, 0, 1, 1)
        self.tab_prx = QtGui.QTabWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_prx.sizePolicy().hasHeightForWidth())
        self.tab_prx.setSizePolicy(sizePolicy)
        self.tab_prx.setMaximumSize(QtCore.QSize(400, 16777215))
        self.tab_prx.setDocumentMode(True)
        self.tab_prx.setObjectName(_fromUtf8("tab_prx"))
        self.tab_normalx = QtGui.QWidget()
        self.tab_normalx.setObjectName(_fromUtf8("tab_normalx"))
        self.gridLayout = QtGui.QGridLayout(self.tab_normalx)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab_normalx)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.ln_xnrsigma = QtGui.QLineEdit(self.tab_normalx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_xnrsigma.sizePolicy().hasHeightForWidth())
        self.ln_xnrsigma.setSizePolicy(sizePolicy)
        self.ln_xnrsigma.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_xnrsigma.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_xnrsigma.setObjectName(_fromUtf8("ln_xnrsigma"))
        self.gridLayout.addWidget(self.ln_xnrsigma, 1, 2, 1, 1)
        self.ln_xnrmu = QtGui.QLineEdit(self.tab_normalx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_xnrmu.sizePolicy().hasHeightForWidth())
        self.ln_xnrmu.setSizePolicy(sizePolicy)
        self.ln_xnrmu.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_xnrmu.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_xnrmu.setObjectName(_fromUtf8("ln_xnrmu"))
        self.gridLayout.addWidget(self.ln_xnrmu, 0, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.tab_normalx)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.tab_prx.addTab(self.tab_normalx, _fromUtf8(""))
        self.tab_unix = QtGui.QWidget()
        self.tab_unix.setObjectName(_fromUtf8("tab_unix"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_unix)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.ln_unixlow = QtGui.QLineEdit(self.tab_unix)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_unixlow.sizePolicy().hasHeightForWidth())
        self.ln_unixlow.setSizePolicy(sizePolicy)
        self.ln_unixlow.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_unixlow.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_unixlow.setObjectName(_fromUtf8("ln_unixlow"))
        self.gridLayout_2.addWidget(self.ln_unixlow, 0, 2, 1, 1)
        self.ln_unixhigh = QtGui.QLineEdit(self.tab_unix)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_unixhigh.sizePolicy().hasHeightForWidth())
        self.ln_unixhigh.setSizePolicy(sizePolicy)
        self.ln_unixhigh.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_unixhigh.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_unixhigh.setObjectName(_fromUtf8("ln_unixhigh"))
        self.gridLayout_2.addWidget(self.ln_unixhigh, 1, 2, 1, 1)
        self.label_13 = QtGui.QLabel(self.tab_unix)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_2.addWidget(self.label_13, 1, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.tab_unix)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.tab_prx.addTab(self.tab_unix, _fromUtf8(""))
        self.tab_students = QtGui.QWidget()
        self.tab_students.setObjectName(_fromUtf8("tab_students"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_students)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.ln_stk = QtGui.QLineEdit(self.tab_students)
        self.ln_stk.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_stk.setObjectName(_fromUtf8("ln_stk"))
        self.gridLayout_5.addWidget(self.ln_stk, 0, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab_students)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_5.addWidget(self.label_6, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 0, 0, 1, 1)
        self.tab_prx.addTab(self.tab_students, _fromUtf8(""))
        self.tab_exp = QtGui.QWidget()
        self.tab_exp.setObjectName(_fromUtf8("tab_exp"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_exp)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.ln_explambda = QtGui.QLineEdit(self.tab_exp)
        self.ln_explambda.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_explambda.setObjectName(_fromUtf8("ln_explambda"))
        self.gridLayout_6.addWidget(self.ln_explambda, 0, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.tab_exp)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_6.addWidget(self.label_8, 0, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 0, 0, 1, 1)
        self.tab_prx.addTab(self.tab_exp, _fromUtf8(""))
        self.tab_lognorm = QtGui.QWidget()
        self.tab_lognorm.setObjectName(_fromUtf8("tab_lognorm"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_lognorm)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.ln_logsigma = QtGui.QLineEdit(self.tab_lognorm)
        self.ln_logsigma.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_logsigma.setObjectName(_fromUtf8("ln_logsigma"))
        self.gridLayout_7.addWidget(self.ln_logsigma, 1, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.tab_lognorm)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_7.addWidget(self.label_10, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.tab_lognorm)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_7.addWidget(self.label_9, 0, 1, 1, 1)
        self.ln_logmu = QtGui.QLineEdit(self.tab_lognorm)
        self.ln_logmu.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_logmu.setObjectName(_fromUtf8("ln_logmu"))
        self.gridLayout_7.addWidget(self.ln_logmu, 0, 2, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem5, 1, 0, 1, 1)
        self.tab_prx.addTab(self.tab_lognorm, _fromUtf8(""))
        self.tab_x2 = QtGui.QWidget()
        self.tab_x2.setObjectName(_fromUtf8("tab_x2"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_x2)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.label_19 = QtGui.QLabel(self.tab_x2)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_8.addWidget(self.label_19, 0, 1, 1, 1)
        self.ln_xk = QtGui.QLineEdit(self.tab_x2)
        self.ln_xk.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_xk.setObjectName(_fromUtf8("ln_xk"))
        self.gridLayout_8.addWidget(self.ln_xk, 0, 2, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem6, 0, 0, 1, 1)
        self.tab_prx.addTab(self.tab_x2, _fromUtf8(""))
        self.tab_beta = QtGui.QWidget()
        self.tab_beta.setObjectName(_fromUtf8("tab_beta"))
        self.gridLayout_9 = QtGui.QGridLayout(self.tab_beta)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_20 = QtGui.QLabel(self.tab_beta)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_9.addWidget(self.label_20, 0, 1, 1, 1)
        self.label_21 = QtGui.QLabel(self.tab_beta)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_9.addWidget(self.label_21, 1, 1, 1, 1)
        self.ln_betabeta = QtGui.QLineEdit(self.tab_beta)
        self.ln_betabeta.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_betabeta.setObjectName(_fromUtf8("ln_betabeta"))
        self.gridLayout_9.addWidget(self.ln_betabeta, 1, 2, 1, 1)
        self.ln_betaalpha = QtGui.QLineEdit(self.tab_beta)
        self.ln_betaalpha.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_betaalpha.setObjectName(_fromUtf8("ln_betaalpha"))
        self.gridLayout_9.addWidget(self.ln_betaalpha, 0, 2, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem7, 0, 0, 1, 1)
        self.tab_prx.addTab(self.tab_beta, _fromUtf8(""))
        self.tab_gamma = QtGui.QWidget()
        self.tab_gamma.setObjectName(_fromUtf8("tab_gamma"))
        self.gridLayout_10 = QtGui.QGridLayout(self.tab_gamma)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.label_22 = QtGui.QLabel(self.tab_gamma)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_10.addWidget(self.label_22, 0, 1, 1, 1)
        self.label_23 = QtGui.QLabel(self.tab_gamma)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_10.addWidget(self.label_23, 1, 1, 1, 1)
        self.ln_gammatheta = QtGui.QLineEdit(self.tab_gamma)
        self.ln_gammatheta.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_gammatheta.setObjectName(_fromUtf8("ln_gammatheta"))
        self.gridLayout_10.addWidget(self.ln_gammatheta, 0, 2, 1, 1)
        self.ln_gammak = QtGui.QLineEdit(self.tab_gamma)
        self.ln_gammak.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_gammak.setObjectName(_fromUtf8("ln_gammak"))
        self.gridLayout_10.addWidget(self.ln_gammak, 1, 2, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem8, 0, 0, 1, 1)
        self.tab_prx.addTab(self.tab_gamma, _fromUtf8(""))
        self.tab_weibull = QtGui.QWidget()
        self.tab_weibull.setObjectName(_fromUtf8("tab_weibull"))
        self.gridLayout_11 = QtGui.QGridLayout(self.tab_weibull)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.ln_weilambda = QtGui.QLineEdit(self.tab_weibull)
        self.ln_weilambda.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_weilambda.setObjectName(_fromUtf8("ln_weilambda"))
        self.gridLayout_11.addWidget(self.ln_weilambda, 0, 2, 1, 1)
        self.ln_weik = QtGui.QLineEdit(self.tab_weibull)
        self.ln_weik.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_weik.setObjectName(_fromUtf8("ln_weik"))
        self.gridLayout_11.addWidget(self.ln_weik, 1, 2, 1, 1)
        self.label_25 = QtGui.QLabel(self.tab_weibull)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_11.addWidget(self.label_25, 1, 1, 1, 1)
        self.label_24 = QtGui.QLabel(self.tab_weibull)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_11.addWidget(self.label_24, 0, 1, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem9, 0, 0, 1, 1)
        self.tab_prx.addTab(self.tab_weibull, _fromUtf8(""))
        self.tab_custom = QtGui.QWidget()
        self.tab_custom.setObjectName(_fromUtf8("tab_custom"))
        self.gridLayout_12 = QtGui.QGridLayout(self.tab_custom)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.label_26 = QtGui.QLabel(self.tab_custom)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_12.addWidget(self.label_26, 0, 1, 1, 1)
        self.btn_custom = QtGui.QToolButton(self.tab_custom)
        self.btn_custom.setObjectName(_fromUtf8("btn_custom"))
        self.gridLayout_12.addWidget(self.btn_custom, 0, 2, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem10, 0, 0, 1, 1)
        self.tab_prx.addTab(self.tab_custom, _fromUtf8(""))
        self.gridLayout_4.addWidget(self.tab_prx, 0, 1, 1, 1)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_4.addWidget(self.line, 1, 1, 1, 1)
        self.tab_pry = QtGui.QTabWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_pry.sizePolicy().hasHeightForWidth())
        self.tab_pry.setSizePolicy(sizePolicy)
        self.tab_pry.setMaximumSize(QtCore.QSize(9000, 16777215))
        self.tab_pry.setDocumentMode(True)
        self.tab_pry.setObjectName(_fromUtf8("tab_pry"))
        self.tab_normaly = QtGui.QWidget()
        self.tab_normaly.setObjectName(_fromUtf8("tab_normaly"))
        self.gridLayout_30 = QtGui.QGridLayout(self.tab_normaly)
        self.gridLayout_30.setObjectName(_fromUtf8("gridLayout_30"))
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_30.addItem(spacerItem11, 0, 0, 1, 1)
        self.label_51 = QtGui.QLabel(self.tab_normaly)
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.gridLayout_30.addWidget(self.label_51, 0, 1, 1, 1)
        self.ln_ynrsigma = QtGui.QLineEdit(self.tab_normaly)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_ynrsigma.sizePolicy().hasHeightForWidth())
        self.ln_ynrsigma.setSizePolicy(sizePolicy)
        self.ln_ynrsigma.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_ynrsigma.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_ynrsigma.setObjectName(_fromUtf8("ln_ynrsigma"))
        self.gridLayout_30.addWidget(self.ln_ynrsigma, 1, 2, 1, 1)
        self.ln_ynrmu = QtGui.QLineEdit(self.tab_normaly)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_ynrmu.sizePolicy().hasHeightForWidth())
        self.ln_ynrmu.setSizePolicy(sizePolicy)
        self.ln_ynrmu.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_ynrmu.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_ynrmu.setObjectName(_fromUtf8("ln_ynrmu"))
        self.gridLayout_30.addWidget(self.ln_ynrmu, 0, 2, 1, 1)
        self.label_52 = QtGui.QLabel(self.tab_normaly)
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.gridLayout_30.addWidget(self.label_52, 1, 1, 1, 1)
        self.tab_pry.addTab(self.tab_normaly, _fromUtf8(""))
        self.tab_uniy = QtGui.QWidget()
        self.tab_uniy.setObjectName(_fromUtf8("tab_uniy"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_uniy)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_14 = QtGui.QLabel(self.tab_uniy)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_3.addWidget(self.label_14, 0, 1, 1, 1)
        self.ln_uniylow = QtGui.QLineEdit(self.tab_uniy)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_uniylow.sizePolicy().hasHeightForWidth())
        self.ln_uniylow.setSizePolicy(sizePolicy)
        self.ln_uniylow.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_uniylow.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_uniylow.setObjectName(_fromUtf8("ln_uniylow"))
        self.gridLayout_3.addWidget(self.ln_uniylow, 0, 2, 1, 1)
        self.label_15 = QtGui.QLabel(self.tab_uniy)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 1, 1, 1, 1)
        self.ln_uniyhigh = QtGui.QLineEdit(self.tab_uniy)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_uniyhigh.sizePolicy().hasHeightForWidth())
        self.ln_uniyhigh.setSizePolicy(sizePolicy)
        self.ln_uniyhigh.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_uniyhigh.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_uniyhigh.setObjectName(_fromUtf8("ln_uniyhigh"))
        self.gridLayout_3.addWidget(self.ln_uniyhigh, 1, 2, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem12, 0, 0, 1, 1)
        self.tab_pry.addTab(self.tab_uniy, _fromUtf8(""))
        self.tab_students_4 = QtGui.QWidget()
        self.tab_students_4.setObjectName(_fromUtf8("tab_students_4"))
        self.gridLayout_31 = QtGui.QGridLayout(self.tab_students_4)
        self.gridLayout_31.setObjectName(_fromUtf8("gridLayout_31"))
        self.ln_stk_4 = QtGui.QLineEdit(self.tab_students_4)
        self.ln_stk_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_stk_4.setObjectName(_fromUtf8("ln_stk_4"))
        self.gridLayout_31.addWidget(self.ln_stk_4, 0, 2, 1, 1)
        self.label_53 = QtGui.QLabel(self.tab_students_4)
        self.label_53.setObjectName(_fromUtf8("label_53"))
        self.gridLayout_31.addWidget(self.label_53, 0, 1, 1, 1)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_31.addItem(spacerItem13, 0, 0, 1, 1)
        self.tab_pry.addTab(self.tab_students_4, _fromUtf8(""))
        self.tab_exp_4 = QtGui.QWidget()
        self.tab_exp_4.setObjectName(_fromUtf8("tab_exp_4"))
        self.gridLayout_32 = QtGui.QGridLayout(self.tab_exp_4)
        self.gridLayout_32.setObjectName(_fromUtf8("gridLayout_32"))
        self.ln_explambda_4 = QtGui.QLineEdit(self.tab_exp_4)
        self.ln_explambda_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_explambda_4.setObjectName(_fromUtf8("ln_explambda_4"))
        self.gridLayout_32.addWidget(self.ln_explambda_4, 0, 2, 1, 1)
        self.label_54 = QtGui.QLabel(self.tab_exp_4)
        self.label_54.setObjectName(_fromUtf8("label_54"))
        self.gridLayout_32.addWidget(self.label_54, 0, 1, 1, 1)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_32.addItem(spacerItem14, 0, 0, 1, 1)
        self.tab_pry.addTab(self.tab_exp_4, _fromUtf8(""))
        self.tab_lognorm_4 = QtGui.QWidget()
        self.tab_lognorm_4.setObjectName(_fromUtf8("tab_lognorm_4"))
        self.gridLayout_33 = QtGui.QGridLayout(self.tab_lognorm_4)
        self.gridLayout_33.setObjectName(_fromUtf8("gridLayout_33"))
        self.ln_logsigma_4 = QtGui.QLineEdit(self.tab_lognorm_4)
        self.ln_logsigma_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_logsigma_4.setObjectName(_fromUtf8("ln_logsigma_4"))
        self.gridLayout_33.addWidget(self.ln_logsigma_4, 1, 2, 1, 1)
        self.label_55 = QtGui.QLabel(self.tab_lognorm_4)
        self.label_55.setObjectName(_fromUtf8("label_55"))
        self.gridLayout_33.addWidget(self.label_55, 1, 1, 1, 1)
        self.label_56 = QtGui.QLabel(self.tab_lognorm_4)
        self.label_56.setObjectName(_fromUtf8("label_56"))
        self.gridLayout_33.addWidget(self.label_56, 0, 1, 1, 1)
        self.ln_logmu_4 = QtGui.QLineEdit(self.tab_lognorm_4)
        self.ln_logmu_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_logmu_4.setObjectName(_fromUtf8("ln_logmu_4"))
        self.gridLayout_33.addWidget(self.ln_logmu_4, 0, 2, 1, 1)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_33.addItem(spacerItem15, 1, 0, 1, 1)
        self.tab_pry.addTab(self.tab_lognorm_4, _fromUtf8(""))
        self.tab_x2_4 = QtGui.QWidget()
        self.tab_x2_4.setObjectName(_fromUtf8("tab_x2_4"))
        self.gridLayout_34 = QtGui.QGridLayout(self.tab_x2_4)
        self.gridLayout_34.setObjectName(_fromUtf8("gridLayout_34"))
        self.label_57 = QtGui.QLabel(self.tab_x2_4)
        self.label_57.setObjectName(_fromUtf8("label_57"))
        self.gridLayout_34.addWidget(self.label_57, 0, 1, 1, 1)
        self.ln_xk_4 = QtGui.QLineEdit(self.tab_x2_4)
        self.ln_xk_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_xk_4.setObjectName(_fromUtf8("ln_xk_4"))
        self.gridLayout_34.addWidget(self.ln_xk_4, 0, 2, 1, 1)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_34.addItem(spacerItem16, 0, 0, 1, 1)
        self.tab_pry.addTab(self.tab_x2_4, _fromUtf8(""))
        self.tab_beta_4 = QtGui.QWidget()
        self.tab_beta_4.setObjectName(_fromUtf8("tab_beta_4"))
        self.gridLayout_35 = QtGui.QGridLayout(self.tab_beta_4)
        self.gridLayout_35.setObjectName(_fromUtf8("gridLayout_35"))
        self.label_58 = QtGui.QLabel(self.tab_beta_4)
        self.label_58.setObjectName(_fromUtf8("label_58"))
        self.gridLayout_35.addWidget(self.label_58, 0, 1, 1, 1)
        self.label_59 = QtGui.QLabel(self.tab_beta_4)
        self.label_59.setObjectName(_fromUtf8("label_59"))
        self.gridLayout_35.addWidget(self.label_59, 1, 1, 1, 1)
        self.ln_betabeta_4 = QtGui.QLineEdit(self.tab_beta_4)
        self.ln_betabeta_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_betabeta_4.setObjectName(_fromUtf8("ln_betabeta_4"))
        self.gridLayout_35.addWidget(self.ln_betabeta_4, 1, 2, 1, 1)
        self.ln_betaalpha_4 = QtGui.QLineEdit(self.tab_beta_4)
        self.ln_betaalpha_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_betaalpha_4.setObjectName(_fromUtf8("ln_betaalpha_4"))
        self.gridLayout_35.addWidget(self.ln_betaalpha_4, 0, 2, 1, 1)
        spacerItem17 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_35.addItem(spacerItem17, 0, 0, 1, 1)
        self.tab_pry.addTab(self.tab_beta_4, _fromUtf8(""))
        self.tab_gamma_4 = QtGui.QWidget()
        self.tab_gamma_4.setObjectName(_fromUtf8("tab_gamma_4"))
        self.gridLayout_36 = QtGui.QGridLayout(self.tab_gamma_4)
        self.gridLayout_36.setObjectName(_fromUtf8("gridLayout_36"))
        self.label_60 = QtGui.QLabel(self.tab_gamma_4)
        self.label_60.setObjectName(_fromUtf8("label_60"))
        self.gridLayout_36.addWidget(self.label_60, 0, 1, 1, 1)
        self.label_61 = QtGui.QLabel(self.tab_gamma_4)
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.gridLayout_36.addWidget(self.label_61, 1, 1, 1, 1)
        self.ln_gammatheta_4 = QtGui.QLineEdit(self.tab_gamma_4)
        self.ln_gammatheta_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_gammatheta_4.setObjectName(_fromUtf8("ln_gammatheta_4"))
        self.gridLayout_36.addWidget(self.ln_gammatheta_4, 0, 2, 1, 1)
        self.ln_gammak_4 = QtGui.QLineEdit(self.tab_gamma_4)
        self.ln_gammak_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_gammak_4.setObjectName(_fromUtf8("ln_gammak_4"))
        self.gridLayout_36.addWidget(self.ln_gammak_4, 1, 2, 1, 1)
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_36.addItem(spacerItem18, 0, 0, 1, 1)
        self.tab_pry.addTab(self.tab_gamma_4, _fromUtf8(""))
        self.tab_weibull_4 = QtGui.QWidget()
        self.tab_weibull_4.setObjectName(_fromUtf8("tab_weibull_4"))
        self.gridLayout_37 = QtGui.QGridLayout(self.tab_weibull_4)
        self.gridLayout_37.setObjectName(_fromUtf8("gridLayout_37"))
        self.ln_weilambda_4 = QtGui.QLineEdit(self.tab_weibull_4)
        self.ln_weilambda_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_weilambda_4.setObjectName(_fromUtf8("ln_weilambda_4"))
        self.gridLayout_37.addWidget(self.ln_weilambda_4, 0, 2, 1, 1)
        self.ln_weik_4 = QtGui.QLineEdit(self.tab_weibull_4)
        self.ln_weik_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_weik_4.setObjectName(_fromUtf8("ln_weik_4"))
        self.gridLayout_37.addWidget(self.ln_weik_4, 1, 2, 1, 1)
        self.label_62 = QtGui.QLabel(self.tab_weibull_4)
        self.label_62.setObjectName(_fromUtf8("label_62"))
        self.gridLayout_37.addWidget(self.label_62, 1, 1, 1, 1)
        self.label_63 = QtGui.QLabel(self.tab_weibull_4)
        self.label_63.setObjectName(_fromUtf8("label_63"))
        self.gridLayout_37.addWidget(self.label_63, 0, 1, 1, 1)
        spacerItem19 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_37.addItem(spacerItem19, 0, 0, 1, 1)
        self.tab_pry.addTab(self.tab_weibull_4, _fromUtf8(""))
        self.tab_custom_4 = QtGui.QWidget()
        self.tab_custom_4.setObjectName(_fromUtf8("tab_custom_4"))
        self.gridLayout_38 = QtGui.QGridLayout(self.tab_custom_4)
        self.gridLayout_38.setObjectName(_fromUtf8("gridLayout_38"))
        self.label_64 = QtGui.QLabel(self.tab_custom_4)
        self.label_64.setObjectName(_fromUtf8("label_64"))
        self.gridLayout_38.addWidget(self.label_64, 0, 1, 1, 1)
        self.btn_custom_4 = QtGui.QToolButton(self.tab_custom_4)
        self.btn_custom_4.setObjectName(_fromUtf8("btn_custom_4"))
        self.gridLayout_38.addWidget(self.btn_custom_4, 0, 2, 1, 1)
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_38.addItem(spacerItem20, 0, 0, 1, 1)
        self.tab_pry.addTab(self.tab_custom_4, _fromUtf8(""))
        self.gridLayout_4.addWidget(self.tab_pry, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        self.line_4 = QtGui.QFrame(Form)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_2.addWidget(self.line_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_31 = QtGui.QLabel(Form)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.horizontalLayout_6.addWidget(self.label_31)
        self.ln_convcheck = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_convcheck.sizePolicy().hasHeightForWidth())
        self.ln_convcheck.setSizePolicy(sizePolicy)
        self.ln_convcheck.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ln_convcheck.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_convcheck.setObjectName(_fromUtf8("ln_convcheck"))
        self.horizontalLayout_6.addWidget(self.ln_convcheck)
        self.label_28 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.horizontalLayout_6.addWidget(self.label_28)
        self.ln_partition = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_partition.sizePolicy().hasHeightForWidth())
        self.ln_partition.setSizePolicy(sizePolicy)
        self.ln_partition.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ln_partition.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_partition.setObjectName(_fromUtf8("ln_partition"))
        self.horizontalLayout_6.addWidget(self.ln_partition)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_16 = QtGui.QLabel(Form)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_3.addWidget(self.label_16)
        self.ln_reps = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_reps.sizePolicy().hasHeightForWidth())
        self.ln_reps.setSizePolicy(sizePolicy)
        self.ln_reps.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ln_reps.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_reps.setObjectName(_fromUtf8("ln_reps"))
        self.horizontalLayout_3.addWidget(self.ln_reps)
        self.btn_convcheck = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_convcheck.sizePolicy().hasHeightForWidth())
        self.btn_convcheck.setSizePolicy(sizePolicy)
        self.btn_convcheck.setMinimumSize(QtCore.QSize(130, 0))
        self.btn_convcheck.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btn_convcheck.setObjectName(_fromUtf8("btn_convcheck"))
        self.horizontalLayout_3.addWidget(self.btn_convcheck)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line_6 = QtGui.QFrame(Form)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout_2.addWidget(self.line_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.chb_interpolation = QtGui.QCheckBox(Form)
        self.chb_interpolation.setChecked(True)
        self.chb_interpolation.setObjectName(_fromUtf8("chb_interpolation"))
        self.horizontalLayout_7.addWidget(self.chb_interpolation)
        self.ln_interpolation = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_interpolation.sizePolicy().hasHeightForWidth())
        self.ln_interpolation.setSizePolicy(sizePolicy)
        self.ln_interpolation.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_interpolation.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_interpolation.setObjectName(_fromUtf8("ln_interpolation"))
        self.horizontalLayout_7.addWidget(self.ln_interpolation)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.chb_rico = QtGui.QCheckBox(Form)
        self.chb_rico.setChecked(True)
        self.chb_rico.setObjectName(_fromUtf8("chb_rico"))
        self.horizontalLayout_9.addWidget(self.chb_rico)
        self.label_32 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.horizontalLayout_9.addWidget(self.label_32)
        self.ln_rico = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_rico.sizePolicy().hasHeightForWidth())
        self.ln_rico.setSizePolicy(sizePolicy)
        self.ln_rico.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_rico.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_rico.setObjectName(_fromUtf8("ln_rico"))
        self.horizontalLayout_9.addWidget(self.ln_rico)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.gridLayout_13 = QtGui.QGridLayout()
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.ln_rangelow = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_rangelow.sizePolicy().hasHeightForWidth())
        self.ln_rangelow.setSizePolicy(sizePolicy)
        self.ln_rangelow.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_rangelow.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_rangelow.setObjectName(_fromUtf8("ln_rangelow"))
        self.gridLayout_13.addWidget(self.ln_rangelow, 1, 1, 1, 1)
        self.ln_rangehigh = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_rangehigh.sizePolicy().hasHeightForWidth())
        self.ln_rangehigh.setSizePolicy(sizePolicy)
        self.ln_rangehigh.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_rangehigh.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_rangehigh.setObjectName(_fromUtf8("ln_rangehigh"))
        self.gridLayout_13.addWidget(self.ln_rangehigh, 2, 1, 1, 1)
        self.chb_range = QtGui.QCheckBox(Form)
        self.chb_range.setObjectName(_fromUtf8("chb_range"))
        self.gridLayout_13.addWidget(self.chb_range, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_13.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_13.addWidget(self.label_11, 2, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_13)
        self.line_7 = QtGui.QFrame(Form)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.verticalLayout_2.addWidget(self.line_7)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.chb_export = QtGui.QCheckBox(Form)
        self.chb_export.setObjectName(_fromUtf8("chb_export"))
        self.horizontalLayout_5.addWidget(self.chb_export)
        self.ln_savefile = QtGui.QLineEdit(Form)
        self.ln_savefile.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_savefile.sizePolicy().hasHeightForWidth())
        self.ln_savefile.setSizePolicy(sizePolicy)
        self.ln_savefile.setObjectName(_fromUtf8("ln_savefile"))
        self.horizontalLayout_5.addWidget(self.ln_savefile)
        self.tbtn_filepath = QtGui.QToolButton(Form)
        self.tbtn_filepath.setObjectName(_fromUtf8("tbtn_filepath"))
        self.horizontalLayout_5.addWidget(self.tbtn_filepath)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.chb_results = QtGui.QCheckBox(Form)
        self.chb_results.setObjectName(_fromUtf8("chb_results"))
        self.horizontalLayout_8.addWidget(self.chb_results)
        self.ln_resultsn = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_resultsn.sizePolicy().hasHeightForWidth())
        self.ln_resultsn.setSizePolicy(sizePolicy)
        self.ln_resultsn.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_resultsn.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_resultsn.setObjectName(_fromUtf8("ln_resultsn"))
        self.horizontalLayout_8.addWidget(self.ln_resultsn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.line_5 = QtGui.QFrame(Form)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout_2.addWidget(self.line_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.ln_n = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_n.sizePolicy().hasHeightForWidth())
        self.ln_n.setSizePolicy(sizePolicy)
        self.ln_n.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_n.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_n.setObjectName(_fromUtf8("ln_n"))
        self.horizontalLayout_2.addWidget(self.ln_n)
        self.btn_start = QtGui.QPushButton(Form)
        self.btn_start.setAutoDefault(True)
        self.btn_start.setDefault(True)
        self.btn_start.setObjectName(_fromUtf8("btn_start"))
        self.horizontalLayout_2.addWidget(self.btn_start)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tbl_tot = QtGui.QTableWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_tot.sizePolicy().hasHeightForWidth())
        self.tbl_tot.setSizePolicy(sizePolicy)
        self.tbl_tot.setObjectName(_fromUtf8("tbl_tot"))
        self.tbl_tot.setColumnCount(2)
        self.tbl_tot.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tbl_tot.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_tot.setHorizontalHeaderItem(1, item)
        self.tbl_tot.horizontalHeader().setDefaultSectionSize(130)
        self.verticalLayout_2.addWidget(self.tbl_tot)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.btn_start.clicked.connect(self.act_btn_start)

        self.btn_convcheck.clicked.connect(self.testconv)

        self.tbl_res.itemSelectionChanged.connect(self.tblresselect)

        self.tbtn_filepath.clicked.connect(self.act_savefile)

        self.tbl_res.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(4, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(5, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(6, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(7, QtGui.QHeaderView.ResizeToContents)
        # self.tbl_res.horizontalHeader().setResizeMode(8, QtGui.QHeaderView.ResizeToContents)
        # self.tbl_res.horizontalHeader().setResizeMode(9, QtGui.QHeaderView.ResizeToContents)

        self.tbl_res.hideColumn(7)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.tab_1.setLayout(layout)

        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.toolbar2 = NavigationToolbar(self.canvas2, self)
        layout2 = QtGui.QVBoxLayout()
        layout2.addWidget(self.toolbar2)
        layout2.addWidget(self.canvas2)
        self.tab_2.setLayout(layout2)

        self.figure3 = Figure()
        self.canvas3 = FigureCanvas(self.figure3)
        self.toolbar3 = NavigationToolbar(self.canvas3, self)
        layout3 = QtGui.QVBoxLayout()
        layout3.addWidget(self.toolbar3)
        layout3.addWidget(self.canvas3)
        self.tab_3.setLayout(layout3)


        self.retranslateUi(Form)
        self.tab_graphs.setCurrentIndex(2)
        self.tab_prx.setCurrentIndex(0)
        self.tab_pry.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Directional shooting: Armor analysis", None))
        self.tab_graphs.setTabText(self.tab_graphs.indexOf(self.tab_1), _translate("Form", "Plot 1", None))
        self.tab_graphs.setTabText(self.tab_graphs.indexOf(self.tab_2), _translate("Form", "Plot 2", None))
        self.tab_graphs.setTabText(self.tab_graphs.indexOf(self.tab_3), _translate("Form", "Plot 3", None))
        self.label_2.setText(_translate("Form", "Shooting results", None))
        item = self.tbl_res.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Shot #", None))
        item = self.tbl_res.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Component", None))
        item = self.tbl_res.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Face", None))
        item = self.tbl_res.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Material", None))
        item = self.tbl_res.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Thickness", None))
        item = self.tbl_res.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Angle", None))
        item = self.tbl_res.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Eq. Thickness", None))
        item = self.tbl_res.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Point", None))
        self.label_7.setText(_translate("Form", "A:", None))
        self.label_27.setText(_translate("Form", "B:", None))
        self.label_17.setText(_translate("Form", "Y axis:", None))
        self.label_18.setText(_translate("Form", "X axis:", None))
        self.label_4.setText(_translate("Form", "Mu", None))
        self.ln_xnrsigma.setText(_translate("Form", "100", None))
        self.ln_xnrmu.setText(_translate("Form", "0", None))
        self.label_5.setText(_translate("Form", "Sigma", None))
        self.tab_prx.setTabText(self.tab_prx.indexOf(self.tab_normalx), _translate("Form", "Normal", None))
        self.ln_unixlow.setText(_translate("Form", "-300", None))
        self.ln_unixhigh.setText(_translate("Form", "300", None))
        self.label_13.setText(_translate("Form", "High", None))
        self.label_12.setText(_translate("Form", "Low", None))
        self.tab_prx.setTabText(self.tab_prx.indexOf(self.tab_unix), _translate("Form", "Uniform", None))
        self.label_6.setText(_translate("Form", "k", None))
        self.tab_prx.setTabText(self.tab_prx.indexOf(self.tab_students), _translate("Form", "Student\'s", None))
        self.label_8.setText(_translate("Form", "Lambda", None))
        self.tab_prx.setTabText(self.tab_prx.indexOf(self.tab_exp), _translate("Form", "Exponential", None))
        self.label_10.setText(_translate("Form", "Sigma", None))
        self.label_9.setText(_translate("Form", "Mu", None))
        self.tab_prx.setTabText(self.tab_prx.indexOf(self.tab_lognorm), _translate("Form", "Log Normal", None))
        self.label_19.setText(_translate("Form", "k", None))
        self.tab_prx.setTabText(self.tab_prx.indexOf(self.tab_x2), _translate("Form", "Chi-squared", None))
        self.label_20.setText(_translate("Form", "Alpha", None))
        self.label_21.setText(_translate("Form", "Beta", None))
        self.tab_prx.setTabText(self.tab_prx.indexOf(self.tab_beta), _translate("Form", "Beta", None))
        self.label_22.setText(_translate("Form", "Theta", None))
        self.label_23.setText(_translate("Form", "k", None))
        self.tab_prx.setTabText(self.tab_prx.indexOf(self.tab_gamma), _translate("Form", "Gamma", None))
        self.label_25.setText(_translate("Form", "k", None))
        self.label_24.setText(_translate("Form", "Lambda", None))
        self.tab_prx.setTabText(self.tab_prx.indexOf(self.tab_weibull), _translate("Form", "Weibull", None))
        self.label_26.setText(_translate("Form", "Load", None))
        self.btn_custom.setText(_translate("Form", "...", None))
        self.tab_prx.setTabText(self.tab_prx.indexOf(self.tab_custom), _translate("Form", "Custom", None))
        self.label_51.setText(_translate("Form", "Mu", None))
        self.ln_ynrsigma.setText(_translate("Form", "100", None))
        self.ln_ynrmu.setText(_translate("Form", "0", None))
        self.label_52.setText(_translate("Form", "Sigma", None))
        self.tab_pry.setTabText(self.tab_pry.indexOf(self.tab_normaly), _translate("Form", "Normal", None))
        self.label_14.setText(_translate("Form", "Low", None))
        self.ln_uniylow.setText(_translate("Form", "-250", None))
        self.label_15.setText(_translate("Form", "High", None))
        self.ln_uniyhigh.setText(_translate("Form", "250", None))
        self.tab_pry.setTabText(self.tab_pry.indexOf(self.tab_uniy), _translate("Form", "Uniform", None))
        self.label_53.setText(_translate("Form", "k", None))
        self.tab_pry.setTabText(self.tab_pry.indexOf(self.tab_students_4), _translate("Form", "Student\'s", None))
        self.label_54.setText(_translate("Form", "Lambda", None))
        self.tab_pry.setTabText(self.tab_pry.indexOf(self.tab_exp_4), _translate("Form", "Exponential", None))
        self.label_55.setText(_translate("Form", "Sigma", None))
        self.label_56.setText(_translate("Form", "Mu", None))
        self.tab_pry.setTabText(self.tab_pry.indexOf(self.tab_lognorm_4), _translate("Form", "Log Normal", None))
        self.label_57.setText(_translate("Form", "k", None))
        self.tab_pry.setTabText(self.tab_pry.indexOf(self.tab_x2_4), _translate("Form", "Chi-squared", None))
        self.label_58.setText(_translate("Form", "Alpha", None))
        self.label_59.setText(_translate("Form", "Beta", None))
        self.tab_pry.setTabText(self.tab_pry.indexOf(self.tab_beta_4), _translate("Form", "Beta", None))
        self.label_60.setText(_translate("Form", "Theta", None))
        self.label_61.setText(_translate("Form", "k", None))
        self.tab_pry.setTabText(self.tab_pry.indexOf(self.tab_gamma_4), _translate("Form", "Gamma", None))
        self.label_62.setText(_translate("Form", "k", None))
        self.label_63.setText(_translate("Form", "Lambda", None))
        self.tab_pry.setTabText(self.tab_pry.indexOf(self.tab_weibull_4), _translate("Form", "Weibull", None))
        self.label_64.setText(_translate("Form", "Load", None))
        self.btn_custom_4.setText(_translate("Form", "...", None))
        self.tab_pry.setTabText(self.tab_pry.indexOf(self.tab_custom_4), _translate("Form", "Custom", None))
        self.label_31.setText(_translate("Form", "Convergence:", None))
        self.ln_convcheck.setText(_translate("Form", "30000", None))
        self.label_28.setText(_translate("Form", "Partition:", None))
        self.ln_partition.setText(_translate("Form", "10", None))
        self.label_16.setText(_translate("Form", "Repetitions:", None))
        self.ln_reps.setText(_translate("Form", "20", None))
        self.btn_convcheck.setText(_translate("Form", "Check", None))
        self.chb_interpolation.setText(_translate("Form", "Enable filter interpolation", None))
        self.ln_interpolation.setText(_translate("Form", "20", None))
        self.chb_rico.setText(_translate("Form", "Enable ricochet", None))
        self.label_32.setText(_translate("Form", "angle, deg:", None))
        self.ln_rico.setText(_translate("Form", "81", None))
        self.ln_rangelow.setText(_translate("Form", "0.01", None))
        self.ln_rangehigh.setText(_translate("Form", "1000", None))
        self.chb_range.setText(_translate("Form", "Custom plot range:", None))
        self.label_3.setText(_translate("Form", "Bar min. value (mm):", None))
        self.label_11.setText(_translate("Form", "Bar max. value (mm):", None))
        self.chb_export.setText(_translate("Form", "Export results", None))
        self.tbtn_filepath.setText(_translate("Form", "...", None))
        self.chb_results.setText(_translate("Form", "Show Intersections; results", None))
        self.ln_resultsn.setText(_translate("Form", "1000", None))
        self.label.setText(_translate("Form", "Shots:", None))
        self.ln_n.setText(_translate("Form", "50000", None))
        self.btn_start.setText(_translate("Form", "Start", None))
        item = self.tbl_tot.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Stat", None))
        item = self.tbl_tot.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Res", None))

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
            if isinstance(chx, QtGui.QLineEdit):
                xparams.append(float(chx.text()))
            if isinstance(chy, QtGui.QLineEdit):
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

        for oind, comp in enumerate(comps):
            self.mainwindow.glwidget.writepic(0, comp.geoobj)
            data = self.mainwindow.glwidget.readpic(0)
            SP = ShotProcessing(data,shotpoints,self.gennorms(comp),m,(w,h),self.percparam)
            planeids,eqthicks,ang,*r = SP.getmaindata(ricochet)
            psi,multpsi = SP.getintersections()
            depths = np.zeros((n))
            self.genheatmap(eqthicks, shotpoints, (h, w))
            self.drawperc(SP.percentiles)
            t = eqthicks[~np.isnan(eqthicks)]
            t = t[np.nonzero(t)]
            self.drawhist(t)

            inters[oind] = multpsi
            results[oind] = np.transpose((np.full((n), oind), planeids, ang, eqthicks))
            arrinter[oind] = np.transpose(
                (np.array(range(n)), np.full((n), oind), np.round(psi[:, -1], 2), eqthicks, depths))



        print(n, ': ', time.time() - start)


        if self.chb_results.isChecked():
            t1 = inters.flatten()
            t1 = inters[~np.isnan(inters)]
            t = list(t1.reshape((-1, 3)))
            self.mainwindow.glwidget.sphcdlist = t[:int(self.ln_resultsn.text())]
            self.mainwindow.glwidget.sphinit(r=3)
            self.mainwindow.glwidget.upmat()

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
                    mat = comp.matarr[faceid - 1]
                    nthick = comp.thickarr[faceid - 1]
                    thick = str(nthick)
                    eqthick = str(round(eqthick, 1))
                    ang = str(round(ang * 180 / np.pi, 1))

                    ci = str(list(inters[objid, ind]))
                    if ind in shotdict.keys():
                        shotdict[ind].append([cname, face, mat.getname(), thick, ang, eqthick, ci])
                    else:
                        shotdict[ind] = [[cname, face, mat.getname(), thick, ang, eqthick, ci]]
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
        item1 = QtGui.QTableWidgetItem(n)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item2 = QtGui.QTableWidgetItem(obj)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item3 = QtGui.QTableWidgetItem(face)
        item3.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item3.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item4 = QtGui.QTableWidgetItem(mat)
        item4.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item4.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item5 = QtGui.QTableWidgetItem(thick)
        item5.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item5.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item6 = QtGui.QTableWidgetItem(angle)
        item6.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item6.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item7 = QtGui.QTableWidgetItem(eqthick)
        item7.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item7.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item8 = QtGui.QTableWidgetItem(ci)
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
        item1 = QtGui.QTableWidgetItem(stn)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        strarr = str(arr)
        item2 = QtGui.QTableWidgetItem(strarr)
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

    def tblresselect(self):
        if self.tbl_res.item(self.tbl_res.currentRow() + 1, -1):
            cistr = self.tbl_res.item(self.tbl_res.currentRow() + 1, -1).text()
            ci1, ci2 = self.lookp1 - self.lookp2 + eval(cistr), eval(cistr) + self.lookp2 - self.lookp1
            self.mainwindow.glwidget.droplines()
            self.mainwindow.glwidget.linecdlist.append([ci1, ci2])
            self.mainwindow.glwidget.lineinit()
            self.mainwindow.glwidget.upmat()

    def act_savefile(self):
        filedialog = QtGui.QFileDialog(self)
        file = filedialog.getSaveFileName(self, "Save resulting file as", "RESULTS\\results.csv",
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
        # hedge = {}
        # totthick = 0
        # mathick = []
        # mawthick = []
        # mawind = []
        # wind = 3

        # for i in range(num):
        #     currthick = self.shoottest(prx, pry, xparams, yparams, num)
        #     hedge[num] = currthick
        #     totthick += currthick
        #     mathick.append((totthick / (i + 1)))
        #     if len(mawind) > wind:
        #         mawind.pop(0)
        #     mawind.append(currthick)
        #     mawthick.append(np.mean(mawind))
        #
        #     num += limnum / 50
        #     num = int(num)
        #     if num > limnum:
        #         break

        #self.mainwindow.glwidget.upmat()
        if self.chb_export.isChecked():
            savefile = self.ln_savefile.text()
            with open(savefile, 'w') as f:
                for k, v in hedge.items():
                    f.write(str(k) + ',' + str(v) + '\n')
            self.mainwindow.glwidget.addtoconsole('Results saved to ' + savefile)
            self.mainwindow.glwidget.upmat()

        print(hedge.values())
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.set_title('Convergence of eq. thicknesses for number of shots, mm')
        ax.plot(hedge.keys(), hedge.values(), '*-',label='Thickness: Mean')
        ax.plot(hedge.keys(), mathick, '^-',label='Th.: Expanding moving average')
        ax.plot(hedge.keys(), mawthick, 'o-',label='Th.: MA, window = 3')
        ax.grid(True)
        ax.legend()
        self.canvas.draw()

        dataser = pd.Series(list(hedge.values()))
        #stds = pd.expanding_std(dataser, min_periods=1)
        stds = dataser.expanding(min_periods=3).std()
        stdr = dataser.rolling(10).std()
        self.figure2.clear()
        ax = self.figure2.add_subplot(111)
        ax.clear()
        ax.set_title('Standart deviations, mm')
        ax.plot(hedge.keys(), stds, '*-',label='Expanding STD')
        ax.plot(hedge.keys(), stdr, 'o-',label='Rolling STD, window = 3')
        ax.grid(True)
        ax.legend()
        # ax.plot(hedge.keys(), mawthick, 'o-')

        self.canvas2.draw()


    # def gettype(self, arrinter):
    #     shotsuni = np.swapaxes(arrinter, 0, 1)
    #     shotsind = (-shotsuni)[:, :, 2].argsort()
    #     shotsrecomb = np.array([shotsuni[i, t] for i, t in enumerate(shotsind)])
    #     res = {}
    #
    #     for i, shot in enumerate(shotsrecomb):
    #         cumvec = []
    #         cumth = 0
    #         shotres = 'NONE'
    #         print(shot)
    #         for n, o, z, t, d in shot:
    #             if t != 0 and t != np.nan:
    #                 cumvec.append(int(o))
    #                 cumth += t
    #                 # print(cumvec)
    #                 if self.mainwindow.fsvact(cumvec):  # self.getevalfsv(cumvec):
    #                     shotres = (str(round(cumth, 2)) + ' mm')
    #                     res[int(n)] = shotres
    #                     break
    #
    #             res[n] = shotres
    #
    #             # print('Shot #',i,': ',shotres)
    #     # print(res)
    #     return res

    def closeEvent(self, event):
        self.mainwindow.glwidget.dropsphs()
        self.mainwindow.glwidget.droplines()
        self.mainwindow.glwidget.dropcross()
        self.mainwindow.glwidget.crossinit()
        self.mainwindow.glwidget.lineinit()
        self.mainwindow.glwidget.sphinit()

        event.accept()
