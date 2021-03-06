import numpy as np
np.seterr(divide='ignore', invalid='ignore')
import math, random
import re
from PIL import Image
from PIL import ImageOps
from CNST.techs import getangle
from shootsettings_ui import Ui_shootset
from clShotProcessing import ShotProcessing
from clArmorSurface import ArmorSurface
import mathutils as mth
from time import time,sleep
from PyQt4 import QtCore, QtGui
from OpenGL.GL import *


from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.ticker import PercentFormatter
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.colors as mcolors
from matplotlib.pyplot import colorbar

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


class Ui_wid_statsshow(QtGui.QWidget):
    def __init__(self):
        super(Ui_wid_statsshow, self).__init__()
        self.setupUi(self)
        # self.mainwindow = 0
        self.meanthick = []
        self.percparam = 0, 100, 101
        self.probx, self.proby = 0, 0

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(663, 772)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tab_graph = QtGui.QTabWidget(Form)
        self.tab_graph.setObjectName(_fromUtf8("tab_graph"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.tab_graph.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tab_graph.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.widget = QtGui.QWidget(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_3.addWidget(self.widget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.ln_power = QtGui.QLineEdit(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_power.sizePolicy().hasHeightForWidth())
        self.ln_power.setSizePolicy(sizePolicy)
        self.ln_power.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_power.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_power.setObjectName(_fromUtf8("ln_power"))
        self.horizontalLayout_3.addWidget(self.ln_power)
        self.btn_power = QtGui.QPushButton(self.tab_3)
        self.btn_power.setObjectName(_fromUtf8("btn_power"))
        self.horizontalLayout_3.addWidget(self.btn_power)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.tab_graph.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tab_graph)
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
        self.tbl_res.setMinimumSize(QtCore.QSize(200, 150))
        self.tbl_res.setObjectName(_fromUtf8("tbl_res"))
        self.tbl_res.setColumnCount(10)
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
        item = QtGui.QTableWidgetItem()
        self.tbl_res.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_res.setHorizontalHeaderItem(9, item)
        self.verticalLayout.addWidget(self.tbl_res)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout.addWidget(self.line_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_14 = QtGui.QGridLayout()
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.ln_angle2 = QtGui.QLineEdit(Form)
        self.ln_angle2.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_angle2.sizePolicy().hasHeightForWidth())
        self.ln_angle2.setSizePolicy(sizePolicy)
        self.ln_angle2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ln_angle2.setObjectName(_fromUtf8("ln_angle2"))
        self.gridLayout_14.addWidget(self.ln_angle2, 0, 4, 1, 1)
        self.label_30 = QtGui.QLabel(Form)
        self.label_30.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_14.addWidget(self.label_30, 0, 1, 1, 1)
        self.label_31 = QtGui.QLabel(Form)
        self.label_31.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout_14.addWidget(self.label_31, 0, 3, 1, 1)
        self.ln_angle1 = QtGui.QLineEdit(Form)
        self.ln_angle1.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_angle1.sizePolicy().hasHeightForWidth())
        self.ln_angle1.setSizePolicy(sizePolicy)
        self.ln_angle1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ln_angle1.setObjectName(_fromUtf8("ln_angle1"))
        self.gridLayout_14.addWidget(self.ln_angle1, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_14)
        self.line_8 = QtGui.QFrame(Form)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.verticalLayout_2.addWidget(self.line_8)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_18 = QtGui.QLabel(Form)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_4.addWidget(self.label_18, 0, 0, 1, 1)
        self.label_17 = QtGui.QLabel(Form)
        self.label_17.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_4.addWidget(self.label_17, 2, 0, 1, 1)
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_4.addWidget(self.line_2, 1, 0, 1, 1)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_4.addWidget(self.line, 1, 1, 1, 1)
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
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
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
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
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
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 0, 0, 1, 1)
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
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem5, 0, 0, 1, 1)
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
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem6, 1, 0, 1, 1)
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
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem7, 0, 0, 1, 1)
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
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem8, 0, 0, 1, 1)
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
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem9, 0, 0, 1, 1)
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
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem10, 0, 0, 1, 1)
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
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem11, 0, 0, 1, 1)
        self.tab_prx.addTab(self.tab_custom, _fromUtf8(""))
        self.gridLayout_4.addWidget(self.tab_prx, 0, 1, 1, 1)
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
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_30.addItem(spacerItem12, 0, 0, 1, 1)
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
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem13, 0, 0, 1, 1)
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
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_31.addItem(spacerItem14, 0, 0, 1, 1)
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
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_32.addItem(spacerItem15, 0, 0, 1, 1)
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
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_33.addItem(spacerItem16, 1, 0, 1, 1)
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
        spacerItem17 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_34.addItem(spacerItem17, 0, 0, 1, 1)
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
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_35.addItem(spacerItem18, 0, 0, 1, 1)
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
        spacerItem19 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_36.addItem(spacerItem19, 0, 0, 1, 1)
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
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_37.addItem(spacerItem20, 0, 0, 1, 1)
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
        spacerItem21 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_38.addItem(spacerItem21, 0, 0, 1, 1)
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
        self.chb_fsv = QtGui.QCheckBox(Form)
        self.chb_fsv.setObjectName(_fromUtf8("chb_fsv"))
        self.horizontalLayout_6.addWidget(self.chb_fsv)
        self.cmb_fcv = QtGui.QComboBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_fcv.sizePolicy().hasHeightForWidth())
        self.cmb_fcv.setSizePolicy(sizePolicy)
        self.cmb_fcv.setObjectName(_fromUtf8("cmb_fcv"))
        self.horizontalLayout_6.addWidget(self.cmb_fcv)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.line_6 = QtGui.QFrame(Form)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout_2.addWidget(self.line_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.rdb_regorbit = QtGui.QRadioButton(Form)
        self.rdb_regorbit.setObjectName(_fromUtf8("rdb_regorbit"))
        self.horizontalLayout_7.addWidget(self.rdb_regorbit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_32 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.horizontalLayout_9.addWidget(self.label_32)
        self.ln_regpoints = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_regpoints.sizePolicy().hasHeightForWidth())
        self.ln_regpoints.setSizePolicy(sizePolicy)
        self.ln_regpoints.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_regpoints.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_regpoints.setObjectName(_fromUtf8("ln_regpoints"))
        self.horizontalLayout_9.addWidget(self.ln_regpoints)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.line_7 = QtGui.QFrame(Form)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.verticalLayout_2.addWidget(self.line_7)
        self.rdb_degorbit = QtGui.QRadioButton(Form)
        self.rdb_degorbit.setChecked(True)
        self.rdb_degorbit.setObjectName(_fromUtf8("rdb_degorbit"))
        self.verticalLayout_2.addWidget(self.rdb_degorbit)
        self.gridLayout_13 = QtGui.QGridLayout()
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.label_3 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_13.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_27 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_13.addWidget(self.label_27, 0, 3, 1, 1)
        self.ln_nastep = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_nastep.sizePolicy().hasHeightForWidth())
        self.ln_nastep.setSizePolicy(sizePolicy)
        self.ln_nastep.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ln_nastep.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_nastep.setObjectName(_fromUtf8("ln_nastep"))
        self.gridLayout_13.addWidget(self.ln_nastep, 1, 4, 1, 1)
        self.label_16 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_13.addWidget(self.label_16, 1, 0, 1, 1)
        self.ln_grang0 = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_grang0.sizePolicy().hasHeightForWidth())
        self.ln_grang0.setSizePolicy(sizePolicy)
        self.ln_grang0.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ln_grang0.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_grang0.setObjectName(_fromUtf8("ln_grang0"))
        self.gridLayout_13.addWidget(self.ln_grang0, 0, 1, 1, 1)
        self.ln_gastep = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_gastep.sizePolicy().hasHeightForWidth())
        self.ln_gastep.setSizePolicy(sizePolicy)
        self.ln_gastep.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ln_gastep.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_gastep.setObjectName(_fromUtf8("ln_gastep"))
        self.gridLayout_13.addWidget(self.ln_gastep, 0, 4, 1, 1)
        self.label_28 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_13.addWidget(self.label_28, 1, 3, 1, 1)
        self.ln_norang0 = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_norang0.sizePolicy().hasHeightForWidth())
        self.ln_norang0.setSizePolicy(sizePolicy)
        self.ln_norang0.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ln_norang0.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_norang0.setObjectName(_fromUtf8("ln_norang0"))
        self.gridLayout_13.addWidget(self.ln_norang0, 1, 1, 1, 1)
        self.ln_grang1 = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_grang1.sizePolicy().hasHeightForWidth())
        self.ln_grang1.setSizePolicy(sizePolicy)
        self.ln_grang1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ln_grang1.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_grang1.setObjectName(_fromUtf8("ln_grang1"))
        self.gridLayout_13.addWidget(self.ln_grang1, 0, 2, 1, 1)
        self.ln_norang1 = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_norang1.sizePolicy().hasHeightForWidth())
        self.ln_norang1.setSizePolicy(sizePolicy)
        self.ln_norang1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ln_norang1.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_norang1.setObjectName(_fromUtf8("ln_norang1"))
        self.gridLayout_13.addWidget(self.ln_norang1, 1, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_13)
        self.line_5 = QtGui.QFrame(Form)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout_2.addWidget(self.line_5)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_5.addWidget(self.checkBox)
        self.ln_savefile = QtGui.QLineEdit(Form)
        self.ln_savefile.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_savefile.sizePolicy().hasHeightForWidth())
        self.ln_savefile.setSizePolicy(sizePolicy)
        self.ln_savefile.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ln_savefile.setObjectName(_fromUtf8("ln_savefile"))
        self.horizontalLayout_5.addWidget(self.ln_savefile)
        self.tbtn_filepath = QtGui.QToolButton(Form)
        self.tbtn_filepath.setObjectName(_fromUtf8("tbtn_filepath"))
        self.horizontalLayout_5.addWidget(self.tbtn_filepath)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.btn_grid = QtGui.QPushButton(Form)
        self.btn_grid.setCheckable(True)
        self.btn_grid.setObjectName(_fromUtf8("btn_grid"))
        self.verticalLayout_2.addWidget(self.btn_grid)
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
        self.btn_grid.clicked.connect(self.act_btn_grid)
        self.btn_power.clicked.connect(self.act_btn_power)

        #self.tbl_res.itemSelectionChanged.connect(self.tblresselect)

        self.tbtn_filepath.clicked.connect(self.act_savefile)

        self.tbl_res.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(4, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(5, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(6, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(7, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(8, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(9, QtGui.QHeaderView.ResizeToContents)

        self.tbl_res.hideColumn(9)

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
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar2)
        layout.addWidget(self.canvas2)
        self.tab_2.setLayout(layout)

        self.figure3 = Figure()
        self.canvas3 = FigureCanvas(self.figure3)
        self.toolbar3 = NavigationToolbar(self.canvas3, self)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar3)
        layout.addWidget(self.canvas3)
        #self.tab_3.setLayout(layout)
        self.widget.setLayout(layout)

        self.retranslateUi(Form)
        self.tab_graph.setCurrentIndex(0)
        self.tab_prx.setCurrentIndex(0)
        self.tab_pry.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Orbital shooting", None))
        self.tab_graph.setTabText(self.tab_graph.indexOf(self.tab_1), _translate("Form", "Eq. Thickness", None))
        self.tab_graph.setTabText(self.tab_graph.indexOf(self.tab_2), _translate("Form", "Plot 1", None))
        self.ln_power.setText(_translate("Form", "500", None))
        self.btn_power.setText(_translate("Form", "Power, mm", None))
        self.tab_graph.setTabText(self.tab_graph.indexOf(self.tab_3), _translate("Form", "Plot 2", None))
        self.label_2.setText(_translate("Form", "Shooting results", None))
        item = self.tbl_res.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Direction #", None))
        item = self.tbl_res.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Hit, %", None))
        item = self.tbl_res.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Mean armor th.", None))
        item = self.tbl_res.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Type A, %", None))
        item = self.tbl_res.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Type A, th", None))
        item = self.tbl_res.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Type B, %", None))
        item = self.tbl_res.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Type B, th", None))
        item = self.tbl_res.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Type C, %", None))
        item = self.tbl_res.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Type C, th", None))
        item = self.tbl_res.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Point", None))
        self.label_30.setText(_translate("Form", "Y angle", None))
        self.label_31.setText(_translate("Form", "ZX angle", None))
        self.label_18.setText(_translate("Form", "X axis:", None))
        self.label_17.setText(_translate("Form", "Y axis:", None))
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
        self.chb_fsv.setText(_translate("Form", "Enable FSV analysis", None))
        self.rdb_regorbit.setText(_translate("Form", "Orbit shootout, Fib. grid", None))
        self.label_32.setText(_translate("Form", "Number of points :", None))
        self.ln_regpoints.setText(_translate("Form", "5000", None))
        self.rdb_degorbit.setText(_translate("Form", "Orbit shootout with angle-based grid", None))
        self.label_3.setText(_translate("Form", "G. angle", None))
        self.label_27.setText(_translate("Form", "Step", None))
        self.ln_nastep.setText(_translate("Form", "5", None))
        self.label_16.setText(_translate("Form", "N. angle", None))
        self.ln_grang0.setText(_translate("Form", "0", None))
        self.ln_gastep.setText(_translate("Form", "6", None))
        self.label_28.setText(_translate("Form", "Step", None))
        self.ln_norang0.setText(_translate("Form", "0", None))
        self.ln_grang1.setText(_translate("Form", "360", None))
        self.ln_norang1.setText(_translate("Form", "90", None))
        self.checkBox.setText(_translate("Form", "Save results to", None))
        self.tbtn_filepath.setText(_translate("Form", "...", None))
        self.btn_grid.setText(_translate("Form", "Show grid", None))
        self.label.setText(_translate("Form", "Shots:", None))
        self.ln_n.setText(_translate("Form", "500", None))
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

    def anglesignal(self,arg):
        self.ln_angle1.setText(str(round(arg[0])))
        self.ln_angle2.setText(str(round(arg[1])))

    def probdet(self):
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

    # def startshowold(self):
    #     timestart = time()
    #
    #     num = int(self.ln_n.text())
    #     prx, pry, xparams, yparams = self.probdet()
    #     shootparam = prx, pry, xparams, yparams, num
    #
    #     hedge = {}
    #     a, b = int(self.ln_gastep.text()), int(self.ln_nastep.text())  # 2, 2
    #     fxang, fyang = int(self.ln_grang.text()), int(self.ln_norang.text())  # 360, 90
    #     xoffset, yoffset = 0, 0
    #     xang, yang = int(fxang / a), int(fyang / b)
    #     xi, yi = a , b
    #     xcum, ycum = xoffset, 0
    #     mv = self.mainwindow.glwidget.mvMatrix  # [:]
    #     rs = []
    #     al, be = [], []
    #     cnt = 0
    #     tt = []
    #     for j in range(yang + 1):
    #         xcum = xoffset
    #         for i in range(xang):
    #             self.mainwindow.glwidget.mvMatrix = mv
    #             xcum += xi
    #             self.mainwindow.glwidget.rot(xcum, ycum)
    #             st = time()
    #             currthick,hitperc = self.shootshedge(shootparam)
    #             #print('full ',time()-st)
    #             tt.append(time()-st)
    #             cnt += 1
    #             print('Mean thickness: ',currthick)
    #             hedge[str(xcum ) + ',' + str(ycum )] = currthick
    #             al.append(xcum  * np.pi / 180)
    #             be.append(ycum  * np.pi / 180)
    #             rs.append([currthick, hitperc])
    #         ycum += yi
    #         break
    #     print(np.mean(np.array(tt)))
    #     self.mainwindow.glwidget.mvMatrix = mv
    #
    #     x, y, z = [], [], []
    #     for a, b, r in zip(al, be, hedge.values()):
    #         x.append(r * np.cos(b) * np.sin(a))
    #         y.append(r * np.cos(b) * np.cos(a))
    #         z.append(r * np.sin(b))
    #
    #     self.tbl_res.setRowCount(0)
    #     for i, r in enumerate(rs):
    #         currthick, hitperc = r
    #         currthick, hitperc = round(currthick, 1), round(hitperc, 2)
    #         self.newrow(str(i), str(hitperc), str(currthick), '-', '-', '-', '-', '-', '-', '-')
    #
    #     self.figure.clear()
    #     ax = Axes3D(self.figure)
    #     ax.clear()
    #     ax.scatter(x, y, z, '*-')
    #     self.canvas.draw()
    #
    #     savefile = self.ln_savefile.text()
    #
    #     with open(savefile, 'w') as f:
    #         for k, v in hedge.items():
    #             f.write(k + ',' + str(v) + '\n')
    #             # print(k,' -> ',v)
    #
    #     n = int(self.ln_n.text())
    #     self.mainwindow.glwidget.addtoconsole('Results saved to ' + savefile)
    #     self.mainwindow.glwidget.addtoconsole(
    #         'Took ' + str(n * xang * yang) + ' shots in ' + str(round(time() - timestart, 2)) + ' seconds.')
    #
    #     self.mainwindow.glwidget.upmat()
    #
    #     print(time() - timestart)
    #     print(xang * yang)

    def startshow(self):
        timestart = time()

        hedge = {}
        a, b = int(self.ln_gastep.text()), int(self.ln_nastep.text())  # 2, 2
        x0, y0 = int(self.ln_grang0.text()), int(self.ln_norang0.text())
        fxang1, fyang1 = int(self.ln_grang1.text()), int(self.ln_norang1.text())  # 360, 90
        xang, yang = int( (fxang1-x0) / a), int( (fyang1-y0) / b)
        xi, yi = a , b
        mv = self.mainwindow.glwidget.mvMatrix
        #for comp in self.mainwindow.components:
        meanth,hits,perc,al,be = self.generatedata(x0,y0,xang,xi,yang,yi,mv)

        print(meanth,'\n',be)

        x, y, z = [], [], []
        for a, b, r in zip(al, be, meanth):
            ix,iy,iz = r * np.cos(b) * np.sin(a),r * np.cos(b) * np.cos(a),r * np.sin(b)
            x.append(ix)
            y.append(iy)
            z.append(iz)

        pe = [[] for i in range(self.percparam[2])]
        for p in perc:
            [pe[i].append(p[i]) for i in range(len(p))]
            # pe[0].append(p[0])
            # pe[1].append(p[len(p)//2])
            # pe[2].append(p[-5])

        self.surfaceinit((al,be,meanth),xi,yi,'TMT')
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
            'Took ' + str(n * xang * yang) + ' shots in ' + str(round(time() - timestart, 2)) + ' seconds.')

        self.mainwindow.glwidget.upmat()

        print(time() - timestart)
        print(xang * yang)

    def surfaceinit(self,points,a,b,name):
        AS = ArmorSurface(points,(a,b),name)
        AS.crecomp()
        AS.comp.defmatinit(list(self.mainwindow.materials)[0])
        self.mainwindow.pushcomponent(AS.comp, 'SURFACE')
        self.mainwindow.glwidget.upmat()

    def gendistpoints(self):
        num = int(self.ln_n.text())
        prx, pry, xparams, yparams = self.probdet()
        w = self.mainwindow.glwidget.wi
        h = self.mainwindow.glwidget.he
        sx = prx(*xparams, num)
        sy = pry(*yparams, num)
        condx = abs(sx - w / 2) < w / 2 - 1
        condy = abs(sy - h / 2) < h / 2 - 1
        cond = condx*condy
        sx = (sx[cond]).astype(int)
        sy = (sy[cond]).astype(int)
        shotpoints = np.transpose([sy, sx])
        shotpoints = np.unique(shotpoints, axis=0)
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
        for comp in comps:
            cnorms,ceqthicks,corgs = self.gennorms(comp)
            NTO.append((cnorms,ceqthicks,corgs))

        meanth,mehits,al,be = [],[],[],[]
        # from multiprocessing.dummy import Pool as ThreadPool
        # pool = ThreadPool(8)
        cn = len(comps)
        st = time()
        sps = []
        print(x0,y0)
        for j in range(yang + 1):
            xcum = x0
            for i in range(xang):
                self.mainwindow.glwidget.mvMatrix = mv
                xcum += xi
                self.mainwindow.glwidget.rot(xcum, ycum)
                m = self.mainwindow.glwidget.mvMatrix
                #n, shotpoints = self.gendistpoints()

                for indbuf,comp,nto in zip(range(cn),comps,NTO):
                    #tt = time()
                    self.mainwindow.glwidget.writepic(0, comp.geoobj)
                    data = self.mainwindow.glwidget.readpic(0)
                    #sps.append((time()-tt))
                    SP = ShotProcessing(data, shotpoints, nto, m, (w, h),self.percparam)
                    #sps.append(SP)
                    SP.getmaindata(80.0)
                    #SP.getintersections()
                    meanthick = SP.meanthick
                    hitper = SP.hitpercentage
                    perc = SP.percentiles
                    #argarr.append((dat,shotpoints,n,cnorms,ceqthicks,lookvec))

                #results = pool.map(self.shotanalysis, argarr)
                # pool.close()
                # pool.join()
                #print(results)
                #meanthick, hitper = results[0]
                #argarr.append([dat,shotpoints, n, indbuf,cnorms, ceqthicks, lookvec])

                al.append(xcum * np.pi / 180)
                be.append(ycum * np.pi / 180)
                meanth.append(meanthick)
                mehits.append(hitper)
                allperc.append(perc)
                cnt+=1
                # break
            #break
            ycum += yi
        #pool.close()
        print(time()-st,(time()-st)/cnt)

        return meanth,mehits,allperc,al,be

    # def shotanalysis(self,pars):
    #     dat,shotpoints, n, norms, eqthicks, lookvec = pars
    #     # img = Image.fromarray(dat,'RGBA')
    #     # img.save('RESULTS\\PBOTEST' + str(cnt) + '.png', 'PNG')
    #
    #     # shotplace = dat[shotpoints[0], shotpoints[1]]
    #     shotplace = dat[shotpoints[1], shotpoints[0]]
    #     objclr = shotplace[shotplace[:, 0] != 255]
    #     plclr = np.transpose(objclr)[1:3]
    #     plids = 256 * plclr[0] + plclr[1]
    #     if np.sum(plids) > 0:
    #         shotnorms = norms[plids - 1]
    #         shoteqthicks = eqthicks[plids - 1]
    #
    #         res1 = np.linalg.norm(np.cross(shotnorms, lookvec), axis=1)
    #         nd = np.dot(shotnorms, lookvec)
    #         ang = np.arctan2(res1, nd)
    #         ang[np.where(ang > 81 * np.pi / 180)] = np.nan
    #         eqthicks1 = shoteqthicks / np.cos(ang)
    #         hits = eqthicks1[np.where(eqthicks1 > 0)]
    #         hitper = len(hits) / n
    #         meanthick = np.mean(hits)
    #         perc = [np.percentile(hits,per) for per in 10*np.array([5,6,7,8,9])]
    #     else:
    #         meanthick = 0
    #         hitper = 0
    #     return meanthick,hitper,perc

    # def regularshow(self):
    #     num = int(self.ln_n.text())
    #     prx, pry, xparams, yparams = self.probdet()
    #     shootparam = prx, pry, xparams, yparams, num
    #
    #     timestart = time()
    #     hedge = {}
    #     rs = []
    #     pnum = 2 * int(self.ln_regpoints.text())
    #     points = list(reversed(self.pointsgen(pnum)))
    #     angsx = [self.specang((p[0], p[2]), (1, 0)) for p in points]
    #     angsy = [getangle(p, (0, 1, 0)) for p in points]
    #
    #     mv = self.mainwindow.glwidget.mvMatrix  # [:]
    #     dataa, datab, datar = [], [], []
    #     for i, p, ax, ay in zip(range(len(points)), points, angsx, angsy):
    #         self.mainwindow.glwidget.mvMatrix = mv
    #         self.mainwindow.glwidget.rot(ax, ay)
    #         currthick, hitperc = self.shootshedge(shootparam)
    #         rs.append([currthick, hitperc])
    #         hedge[str(p[0]) + ',' + str(p[1]) + ',' + str(p[2]) + ',' + str(ax) + ',' + str(ay)] = currthick
    #         dataa.append(ax * np.pi / 180)
    #         datab.append(ay * np.pi / 180)
    #         datar.append(currthick)
    #
    #     self.mainwindow.glwidget.mvMatrix = mv
    #     # self.mainwindow.glwidget.upmat()
    #
    #     x, y, z = [], [], []
    #     for a, b, r in zip(dataa, datab, datar):
    #         x.append(r * np.cos(b) * np.sin(a))
    #         y.append(r * np.cos(b) * np.cos(a))
    #         z.append(r * np.sin(b))
    #
    #     self.tbl_res.setRowCount(0)
    #     for i, r in enumerate(rs):
    #         currthick, hitperc = r
    #         currthick, hitperc = round(currthick, 1), round(hitperc, 2)
    #         self.newrow(str(i), str(hitperc), str(currthick), '-', '-', '-', '-', '-', '-', '-')
    #
    #     self.figure.clear()
    #     ax = Axes3D(self.figure)
    #     ax.clear()
    #     ax.scatter(x, y, z, '*-')
    #     # ax.plot_trisurf(x, y, z)
    #     # refresh canvas
    #     self.canvas.draw()
    #
    #     savefile = self.ln_savefile.text()
    #
    #     with open(savefile, 'w') as f:
    #         for k, v in hedge.items():
    #             f.write(k + ',' + str(v) + '\n')
    #             # print(k,' -> ',v)
    #
    #     n = int(self.ln_n.text()) / 2
    #     self.mainwindow.glwidget.addtoconsole('Results saved to ' + savefile)
    #     self.mainwindow.glwidget.addtoconsole(
    #         'Took ' + str(n * pnum) + ' shots in ' + str(round(time() - timestart, 2)) + ' seconds.')
    #     self.mainwindow.glwidget.upmat()
    #     # print(time() - timestart)

    # def shootshedge(self, params):
    #     prx, pry, xparams, yparams, n = params
    #     start = time()
    #     picarr, deparr, w, h = self.mainwindow.glwidget.getpic()
    #
    #     sx = prx(*xparams, n)
    #     sy = pry(*yparams, n)
    #     sx = (sx[np.where(abs(sx - w / 2) < w / 2 - 1)])
    #     sy = (sy[np.where(abs(sy - h / 2) < h / 2 - 1)])
    #     sx = list(map(int, np.rint(sx).astype(int)))
    #     sy = list(map(int, np.rint(sy).astype(int)))
    #
    #     arrinter = np.zeros((len(picarr), n, 5))
    #     inters = np.zeros((len(picarr), n, 3))
    #     m = self.mainwindow.glwidget.mvMatrix
    #     lookvec = np.matmul(m, (0, 0, 1, 1))[:3]
    #     results = np.zeros((len(picarr), n, 4))
    #     norms, orgs, raystart = np.zeros((n, 3)), np.zeros((n, 3)), np.zeros((n, 3))
    #     eqthicks, planeids, depths = np.zeros((n)), np.zeros((n)), np.zeros((n))
    #
    #     for objind, picdata in enumerate(picarr):
    #         startt = time()
    #         norms.fill(0)
    #         orgs.fill(0)
    #         raystart.fill(0)
    #         eqthicks.fill(0)
    #         planeids.fill(0)
    #         depths.fill(0)
    #         imgc = Image.frombytes("RGBA", (w, h), picdata)
    #         imgc = ImageOps.flip(imgc)
    #         # imgc.save('RESULTS\\norm'+str(i)+'.png', 'PNG')
    #         datac = imgc.load()
    #         objdepths = np.array(deparr[objind])[::-1]
    #         objdepths = np.flip(objdepths.reshape((-1, w)), 1)
    #
    #         for row, x, y in zip(range(n), sx, sy):
    #             # x,y = int(x),int(y)
    #             clr = datac[x, y]
    #             #print(clr)
    #             #print(clr)
    #             # t = datad[y,x]
    #             oid = clr[0]
    #             if oid != 255:
    #                 plid = clr[2] + clr[1] * 256
    #                 px, py = (x - w / 2), (h / 2 - y)
    #                 norm, org, thick = self.checkedplanes[oid][plid - 1]
    #                 planeids[row] = plid
    #                 norms[row] = norm
    #                 orgs[row] = org
    #                 depths[row] = objdepths[y, x]
    #                 eqthicks[row] = thick
    #                 raystart[row] = [px, py, 0]
    #         medt = time()
    #         res1 = np.linalg.norm(np.cross(norms, lookvec), axis=1)
    #         nd = np.dot(norms, lookvec)
    #         ang = np.arctan2(res1, nd)
    #         cond = np.where(ang > 80 * np.pi / 180)
    #         ang[cond] = np.nan
    #         eqthicks = eqthicks / np.cos(ang)
    #         hits = eqthicks[np.where(eqthicks > 0)]
    #         hitper = len(hits) / n
    #         # print(hits)
    #         meanthick = np.mean(hits)
    #         print(len(hits),np.mean(ang[np.where(ang>0)])*180/np.pi)
    #         # results[objind] = np.transpose((np.full((n), objind), planeids, ang, eqthicks))
    #         #print(time()-medt)
    #
    #     return meanthick, hitper  # [results, inters, arrinter]

    def newrow(self, n, perc, thick, tap, tat, tbp, tbt, tcp, tct, ci):
        rowPosition = self.tbl_res.rowCount()
        self.tbl_res.insertRow(rowPosition)
        item1 = QtGui.QTableWidgetItem(n)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item2 = QtGui.QTableWidgetItem(perc)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item3 = QtGui.QTableWidgetItem(thick)
        item3.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item3.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item4 = QtGui.QTableWidgetItem(tap)
        item4.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item4.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item5 = QtGui.QTableWidgetItem(tat)
        item5.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item5.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item6 = QtGui.QTableWidgetItem(tbp)
        item6.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item6.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item7 = QtGui.QTableWidgetItem(tbt)
        item7.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item7.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item8 = QtGui.QTableWidgetItem(tcp)
        item8.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item8.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item9 = QtGui.QTableWidgetItem(tct)
        item9.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item9.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item10 = QtGui.QTableWidgetItem(ci)
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
        item1 = QtGui.QTableWidgetItem(n)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        strarr = str(arr)
        item2 = QtGui.QTableWidgetItem(strarr)
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

    # def specang(self, v1, v2):
    #     x1, y1 = v1
    #     x2, y2 = v2
    #     dot = x1 * x2 + y1 * y2  # dot product
    #     det = x1 * y2 - y1 * x2  # determinant
    #     angle = math.atan2(det, dot)  # atan2(y, x) or atan2(sin, cos)
    #     return angle * 180 / np.pi

    # def genplanesdict(self):
    #     planesd = {}
    #     for comp in self.mainwindow.components:
    #         compdict = {}
    #         for plid in range(len(comp.geoobj.faces)):
    #             compdict[plid] = (comp.geoobj.normals[3 * (plid)],
    #                               comp.geoobj.points[comp.geoobj.faces[plid][0] - 1],
    #                               comp.thickarr[plid])
    #         planesd[comp.geoobj.getid()] = compdict
    #
    #     return planesd

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
        filedialog = QtGui.QFileDialog(self)
        file = filedialog.getSaveFileName(self, "Save resulting file as", "RESULTS\\results.csv",
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
        self.surfaceinit((xt,yt,heatmap.flatten()),xi,yi,'Mean')

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
