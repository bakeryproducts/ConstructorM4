# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creconstrained.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_creconstrained(QtGui.QWidget):
    def __init__(self,x,y):
        super(Ui_creconstrained, self).__init__()
        self.setGeometry(x, y, 100, 100)
        #self.mainwindow=0

        self.fbase,self.fmove = False,False
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(317, 448)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(317, 448))
        Form.setMaximumSize(QtCore.QSize(317, 448))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbl_base = QtGui.QLabel(Form)
        self.lbl_base.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_base.setObjectName(_fromUtf8("lbl_base"))
        self.verticalLayout.addWidget(self.lbl_base)
        self.lay_basepick = QtGui.QHBoxLayout()
        self.lay_basepick.setObjectName(_fromUtf8("lay_basepick"))
        self.lbl_basepick = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_basepick.sizePolicy().hasHeightForWidth())
        self.lbl_basepick.setSizePolicy(sizePolicy)
        self.lbl_basepick.setObjectName(_fromUtf8("lbl_basepick"))
        self.lay_basepick.addWidget(self.lbl_basepick)
        self.btn_basepick = QtGui.QPushButton(Form)
        self.btn_basepick.setMaximumSize(QtCore.QSize(100000, 16777215))
        self.btn_basepick.setObjectName(_fromUtf8("btn_basepick"))
        self.lay_basepick.addWidget(self.btn_basepick)
        self.verticalLayout.addLayout(self.lay_basepick)
        self.lay_basecomp = QtGui.QHBoxLayout()
        self.lay_basecomp.setObjectName(_fromUtf8("lay_basecomp"))
        self.lbl_basecomp = QtGui.QLabel(Form)
        self.lbl_basecomp.setObjectName(_fromUtf8("lbl_basecomp"))
        self.lay_basecomp.addWidget(self.lbl_basecomp)
        self.ln_basecomp = QtGui.QLineEdit(Form)
        self.ln_basecomp.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_basecomp.sizePolicy().hasHeightForWidth())
        self.ln_basecomp.setSizePolicy(sizePolicy)
        self.ln_basecomp.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_basecomp.setObjectName(_fromUtf8("ln_basecomp"))
        self.lay_basecomp.addWidget(self.ln_basecomp)
        self.verticalLayout.addLayout(self.lay_basecomp)
        self.lay_baseplane = QtGui.QHBoxLayout()
        self.lay_baseplane.setObjectName(_fromUtf8("lay_baseplane"))
        self.lbl_baseplane = QtGui.QLabel(Form)
        self.lbl_baseplane.setObjectName(_fromUtf8("lbl_baseplane"))
        self.lay_baseplane.addWidget(self.lbl_baseplane)
        self.ln_baseplane = QtGui.QLineEdit(Form)
        self.ln_baseplane.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_baseplane.sizePolicy().hasHeightForWidth())
        self.ln_baseplane.setSizePolicy(sizePolicy)
        self.ln_baseplane.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_baseplane.setObjectName(_fromUtf8("ln_baseplane"))
        self.lay_baseplane.addWidget(self.ln_baseplane)
        self.verticalLayout.addLayout(self.lay_baseplane)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.lbl_move = QtGui.QLabel(Form)
        self.lbl_move.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_move.setObjectName(_fromUtf8("lbl_move"))
        self.verticalLayout.addWidget(self.lbl_move)
        self.lay_movepick = QtGui.QHBoxLayout()
        self.lay_movepick.setObjectName(_fromUtf8("lay_movepick"))
        self.lbl_movepick = QtGui.QLabel(Form)
        self.lbl_movepick.setObjectName(_fromUtf8("lbl_movepick"))
        self.lay_movepick.addWidget(self.lbl_movepick)
        self.btn_movepick = QtGui.QPushButton(Form)
        self.btn_movepick.setObjectName(_fromUtf8("btn_movepick"))
        self.lay_movepick.addWidget(self.btn_movepick)
        self.verticalLayout.addLayout(self.lay_movepick)
        self.lay_movecomp = QtGui.QHBoxLayout()
        self.lay_movecomp.setObjectName(_fromUtf8("lay_movecomp"))
        self.lbl_movecomp = QtGui.QLabel(Form)
        self.lbl_movecomp.setObjectName(_fromUtf8("lbl_movecomp"))
        self.lay_movecomp.addWidget(self.lbl_movecomp)
        self.ln_movecomp = QtGui.QLineEdit(Form)
        self.ln_movecomp.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_movecomp.sizePolicy().hasHeightForWidth())
        self.ln_movecomp.setSizePolicy(sizePolicy)
        self.ln_movecomp.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_movecomp.setObjectName(_fromUtf8("ln_movecomp"))
        self.lay_movecomp.addWidget(self.ln_movecomp)
        self.verticalLayout.addLayout(self.lay_movecomp)
        self.lay_moveplane = QtGui.QHBoxLayout()
        self.lay_moveplane.setObjectName(_fromUtf8("lay_moveplane"))
        self.lbl_moveplane = QtGui.QLabel(Form)
        self.lbl_moveplane.setObjectName(_fromUtf8("lbl_moveplane"))
        self.lay_moveplane.addWidget(self.lbl_moveplane)
        self.ln_moveplane = QtGui.QLineEdit(Form)
        self.ln_moveplane.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_moveplane.sizePolicy().hasHeightForWidth())
        self.ln_moveplane.setSizePolicy(sizePolicy)
        self.ln_moveplane.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_moveplane.setObjectName(_fromUtf8("ln_moveplane"))
        self.lay_moveplane.addWidget(self.ln_moveplane)
        self.verticalLayout.addLayout(self.lay_moveplane)
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.lbl_position = QtGui.QLabel(Form)
        self.lbl_position.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_position.setObjectName(_fromUtf8("lbl_position"))
        self.verticalLayout.addWidget(self.lbl_position)
        self.lay_offset = QtGui.QHBoxLayout()
        self.lay_offset.setObjectName(_fromUtf8("lay_offset"))
        self.lbl_offset = QtGui.QLabel(Form)
        self.lbl_offset.setObjectName(_fromUtf8("lbl_offset"))
        self.lay_offset.addWidget(self.lbl_offset)
        self.ln_offset = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_offset.sizePolicy().hasHeightForWidth())
        self.ln_offset.setSizePolicy(sizePolicy)
        self.ln_offset.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ln_offset.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_offset.setObjectName(_fromUtf8("ln_offset"))
        self.lay_offset.addWidget(self.ln_offset)
        self.verticalLayout.addLayout(self.lay_offset)
        self.lay_angle = QtGui.QHBoxLayout()
        self.lay_angle.setObjectName(_fromUtf8("lay_angle"))
        self.lbl_angle = QtGui.QLabel(Form)
        self.lbl_angle.setObjectName(_fromUtf8("lbl_angle"))
        self.lay_angle.addWidget(self.lbl_angle)
        self.ln_angle = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_angle.sizePolicy().hasHeightForWidth())
        self.ln_angle.setSizePolicy(sizePolicy)
        self.ln_angle.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ln_angle.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_angle.setObjectName(_fromUtf8("ln_angle"))
        self.lay_angle.addWidget(self.ln_angle)
        self.verticalLayout.addLayout(self.lay_angle)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.lay_btns = QtGui.QHBoxLayout()
        self.lay_btns.setObjectName(_fromUtf8("lay_btns"))
        self.btn_btnsshow = QtGui.QPushButton(Form)
        self.btn_btnsshow.setObjectName(_fromUtf8("btn_btnsshow"))
        self.lay_btns.addWidget(self.btn_btnsshow)
        self.btn_btnssave = QtGui.QPushButton(Form)
        self.btn_btnssave.setObjectName(_fromUtf8("btn_btnssave"))
        self.lay_btns.addWidget(self.btn_btnssave)
        self.btn_btnscancel = QtGui.QPushButton(Form)
        self.btn_btnscancel.setObjectName(_fromUtf8("btn_btnscancel"))
        self.lay_btns.addWidget(self.btn_btnscancel)
        self.verticalLayout.addLayout(self.lay_btns)

        self.btn_basepick.clicked.connect(self.act_btn_basepick)
        self.btn_movepick.clicked.connect(self.act_btn_movepick)
        self.btn_btnsshow.clicked.connect(self.act_btn_btnsshow)
        self.btn_btnssave.clicked.connect(self.act_btn_btnssave)
        self.btn_btnscancel.clicked.connect(self.act_btn_btnscancel)
        self.btn_basepick.setCheckable(True)
        self.btn_movepick.setCheckable(True)

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Constrain component", None))
        self.lbl_base.setText(_translate("Form", "Base component", None))
        self.lbl_basepick.setText(_translate("Form", "Point in plane", None))
        self.btn_basepick.setText(_translate("Form", "Pick", None))
        self.lbl_basecomp.setText(_translate("Form", "Component name:", None))
        self.ln_basecomp.setText(_translate("Form", "Picked component", None))
        self.lbl_baseplane.setText(_translate("Form", "Selected plane #:", None))
        self.ln_baseplane.setText(_translate("Form", "Picked plane", None))
        self.lbl_move.setText(_translate("Form", "Move component", None))
        self.lbl_movepick.setText(_translate("Form", "Point in plane to connect", None))
        self.btn_movepick.setText(_translate("Form", "Pick", None))
        self.lbl_movecomp.setText(_translate("Form", "Component name:", None))
        self.ln_movecomp.setText(_translate("Form", "Picked component", None))
        self.lbl_moveplane.setText(_translate("Form", "Selected plane #:", None))
        self.ln_moveplane.setText(_translate("Form", "Picked plane", None))
        self.lbl_position.setText(_translate("Form", "Position in place", None))
        self.lbl_offset.setText(_translate("Form", "Offset from base component", None))
        self.ln_offset.setText(_translate("Form", "0,0,0", None))
        self.lbl_angle.setText(_translate("Form", "Rotation from base normal", None))
        self.ln_angle.setText(_translate("Form", "0", None))
        self.btn_btnsshow.setText(_translate("Form", "Show changes", None))
        self.btn_btnssave.setText(_translate("Form", "Save", None))
        self.btn_btnscancel.setText(_translate("Form", "Cancel", None))


    def loadinit(self,mainw):
        self.mainwindow = mainw
        self.mainwindow.glwidget.ObjSelected.connect(self.select)

    def select(self,arg):
        if self.fbase:
            self.ln_basecomp.setText(str(arg[0][0]))
            self.ln_baseplane.setText(str(arg[0][1]))
            self.basec = arg[0]
            self.basepoint = arg[1]
        elif self.fmove:
            self.ln_movecomp.setText(str(arg[0][0]))
            self.ln_moveplane.setText(str(arg[0][1]))
            self.movec = arg[0]
            self.movepoint = arg[1]

    def act_btn_basepick(self):
        self.mainwindow.glwidget.dropselection()
        self.mainwindow.glwidget.mode = "pickone"
        self.fbase=True
        self.fmove=False
        self.btn_movepick.setChecked(False)

    def act_btn_movepick(self):
        self.mainwindow.glwidget.dropselection()
        self.mainwindow.glwidget.mode = "pickone"
        self.fbase = False
        self.fmove = True
        self.btn_basepick.setChecked(False)

    def act_btn_btnsshow(self):
        offset = [int(ch) for ch in (self.ln_offset.text()).split(",")]
        angle = int(self.ln_angle.text())
        self.tcomp = self.constrain(offset,angle)
        self.mainwindow.glwidget.cleartmpobjs()
        self.mainwindow.glwidget.addtmpobj(self.tcomp.getgeo())
        self.btn_movepick.setChecked(False)
        self.btn_basepick.setChecked(False)
        self.mainwindow.glwidget.upmat()

    def act_btn_btnssave(self):
        categoryname = self.tcomp.category.text(0)
        self.mainwindow.delcomp(self.orgcomp)
        self.mainwindow.pushcomponent(self.tcomp.getcopy(), categoryname)
        self.mainwindow.glwidget.cleartmpobjs()
        self.mainwindow.glwidget.dropselection()
        self.mainwindow.glwidget.mode = "pick0"
        self.close()

    def act_btn_btnscancel(self):
        self.mainwindow.glwidget.cleartmpobjs()
        self.mainwindow.glwidget.dropselection()
        self.mainwindow.glwidget.mode = "pick0"
        self.close()

    def closeEvent(self, QCloseEvent):
        self.act_btn_btnscancel()

    def constrain(self, offset=(0, 0, 0), angle=0, grid=None, angbasis=0):
        ''' at the time there are two components represented by
            geo objects from picking: base comp, move(able) comp
            on each comp there are point of constraining:
            base- move- points.
                if there is no grid when constrain() called
            lets just  get those components together with
            offset in local basis and rotate angle from local normal
                But active grid= array sends us to
            component 2d flat rect array creator
            damn
        '''

        baseid = self.mainwindow.glwidget.getobjbyid(self.basec[0])
        baseplane = self.basec[1]
        baseobj = self.mainwindow.glwidget.objects[baseid]

        moveid = self.mainwindow.glwidget.getobjbyid(self.movec[0])
        moveplane = self.movec[1]
        moveobj = self.mainwindow.glwidget.objects[moveid]

        normalbase = baseobj.getnormaltoface(baseplane) * (-1)
        pointend = self.basepoint
        pointstart = self.movepoint

        self.orgcomp = self.mainwindow.getcompbygeoid(moveobj.getid())
        tcomp = self.orgcomp.getcopy()
        #print(moveid,tcomp)
        tcomp.geoobj.setup(normalbase, moveplane, pointstart, pointend, offset, angle)
        #moveobj.setup(normalbase, moveplane, pointstart, pointend, offset, angle)
        #self.movepoint = self.basepoint
        return tcomp
        #self.glwidget.upmat()

