# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'move.ui'
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


class Ui_move(QtGui.QWidget):
    def __init__(self, x, y):
        super(Ui_move, self).__init__()
        self.setGeometry(x, y, 100, 100)
        # self.mainwindow = 0
        self.movestep = 0
        self.rotatestep = 0
        self.mx = 0
        self.my = 0
        self.mz = 0
        self.rx = 0
        self.ry = 0
        self.rz = 0
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(170, 410)
        Form.setMinimumSize(QtCore.QSize(170, 410))
        Form.setMaximumSize(QtCore.QSize(170, 410))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout.addWidget(self.label_11)
        self.cmb_component = QtGui.QComboBox(Form)
        self.cmb_component.setObjectName(_fromUtf8("cmb_component"))
        self.verticalLayout.addWidget(self.cmb_component)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.dsb_mz = QtGui.QDoubleSpinBox(Form)
        self.dsb_mz.setAlignment(QtCore.Qt.AlignCenter)
        self.dsb_mz.setDecimals(1)
        self.dsb_mz.setObjectName(_fromUtf8("dsb_mz"))
        self.gridLayout.addWidget(self.dsb_mz, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.dsb_my = QtGui.QDoubleSpinBox(Form)
        self.dsb_my.setAlignment(QtCore.Qt.AlignCenter)
        self.dsb_my.setDecimals(1)
        self.dsb_my.setObjectName(_fromUtf8("dsb_my"))
        self.gridLayout.addWidget(self.dsb_my, 2, 1, 1, 1)
        self.dsb_mx = QtGui.QDoubleSpinBox(Form)
        self.dsb_mx.setAlignment(QtCore.Qt.AlignCenter)
        self.dsb_mx.setDecimals(1)
        self.dsb_mx.setObjectName(_fromUtf8("dsb_mx"))
        self.gridLayout.addWidget(self.dsb_mx, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.ln_movestep = QtGui.QLineEdit(Form)
        self.ln_movestep.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_movestep.setObjectName(_fromUtf8("ln_movestep"))
        self.gridLayout.addWidget(self.ln_movestep, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.dsb_rz = QtGui.QDoubleSpinBox(Form)
        self.dsb_rz.setAlignment(QtCore.Qt.AlignCenter)
        self.dsb_rz.setDecimals(1)
        self.dsb_rz.setObjectName(_fromUtf8("dsb_rz"))
        self.gridLayout_2.addWidget(self.dsb_rz, 3, 1, 1, 1)
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.dsb_ry = QtGui.QDoubleSpinBox(Form)
        self.dsb_ry.setAlignment(QtCore.Qt.AlignCenter)
        self.dsb_ry.setDecimals(1)
        self.dsb_ry.setObjectName(_fromUtf8("dsb_ry"))
        self.gridLayout_2.addWidget(self.dsb_ry, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.dsb_rx = QtGui.QDoubleSpinBox(Form)
        self.dsb_rx.setAlignment(QtCore.Qt.AlignCenter)
        self.dsb_rx.setDecimals(1)
        self.dsb_rx.setObjectName(_fromUtf8("dsb_rx"))
        self.gridLayout_2.addWidget(self.dsb_rx, 1, 1, 1, 1)
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.ln_rotatestep = QtGui.QLineEdit(Form)
        self.ln_rotatestep.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_rotatestep.setObjectName(_fromUtf8("ln_rotatestep"))
        self.gridLayout_2.addWidget(self.ln_rotatestep, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.btn_done = QtGui.QPushButton(Form)
        self.btn_done.setAutoDefault(True)
        self.btn_done.setDefault(True)
        self.btn_done.setObjectName(_fromUtf8("btn_done"))
        self.verticalLayout.addWidget(self.btn_done)

        self.dsb_mx.valueChanged.connect(self.act_dsb_mx)
        self.dsb_my.valueChanged.connect(self.act_dsb_my)
        self.dsb_mz.valueChanged.connect(self.act_dsb_mz)
        self.dsb_rx.valueChanged.connect(self.act_dsb_rx)
        self.dsb_ry.valueChanged.connect(self.act_dsb_ry)
        self.dsb_rz.valueChanged.connect(self.act_dsb_rz)

        self.ln_movestep.textChanged.connect(self.act_ln_movestep)
        self.ln_rotatestep.textChanged.connect(self.act_ln_rotatestep)

        self.dsb_mx.setRange(-1e9, 1e9)
        self.dsb_my.setRange(-1e9, 1e9)
        self.dsb_mz.setRange(-1e9, 1e9)
        self.dsb_rx.setRange(-1e9, 1e9)
        self.dsb_ry.setRange(-1e9, 1e9)
        self.dsb_rz.setRange(-1e9, 1e9)

        self.dsb_mx.setValue(0)
        self.dsb_my.setValue(0)
        self.dsb_mz.setValue(0)
        self.dsb_rx.setValue(0)
        self.dsb_ry.setValue(0)
        self.dsb_rz.setValue(0)

        self.btn_done.clicked.connect(self.act_btn_done)
        self.cmb_component.currentIndexChanged.connect(self.act_cmb_change)

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Move component", None))
        self.label_11.setText(_translate("Form", "Select component", None))
        self.label_4.setText(_translate("Form", "Move", None))
        self.label_2.setText(_translate("Form", "Y", None))
        self.label_3.setText(_translate("Form", "Z", None))
        self.label.setText(_translate("Form", "X", None))
        self.label_9.setText(_translate("Form", "Step", None))
        self.ln_movestep.setText(_translate("Form", "10", None))
        self.label_5.setText(_translate("Form", "Rotate", None))
        self.label_8.setText(_translate("Form", "Z", None))
        self.label_7.setText(_translate("Form", "Y", None))
        self.label_6.setText(_translate("Form", "X", None))
        self.label_10.setText(_translate("Form", "Step", None))
        self.ln_rotatestep.setText(_translate("Form", "1", None))
        self.btn_done.setText(_translate("Form", "Done", None))

    def act_btn_done(self):
        comp = self.comp.getcopy()
        catname = comp.categoryname

        self.mainwindow.delcomp(self.orgcomp)
        self.mainwindow.pushcomponent(comp, catname)
        self.mainwindow.glwidget.cleartmpobjs()
        del (self.comp)
        del (self.orgcomp)
        #self.mainwindow.glwidget.dropselection()
        #self.mainwindow.glwidget.mode = "pick0"
        self.mainwindow.glwidget.cleartmpobjs()
        self.close()

    def act_dsb_mx(self, value):
        self.comp.geoobj.move((value-self.mx,0,0))
        self.mx = value
        self.mainwindow.glwidget.upmat()

    def act_dsb_my(self, value):
        self.comp.geoobj.move((0,value-self.my, 0))
        self.my = value
        self.mainwindow.glwidget.upmat()

    def act_dsb_mz(self, value):
        self.comp.geoobj.move((0,0,value-self.mz))
        self.mz = value
        self.mainwindow.glwidget.upmat()

    def act_dsb_rx(self, value):
        self.comp.geoobj.rotate((value - self.rx, 0, 0))
        self.rx = value
        self.mainwindow.glwidget.upmat()

    def act_dsb_ry(self, value):
        self.comp.geoobj.rotate((0,value-self.ry,0))
        self.ry = value
        self.mainwindow.glwidget.upmat()

    def act_dsb_rz(self, value):
        self.comp.geoobj.rotate((0,0,value - self.rz))
        self.rz = value
        self.mainwindow.glwidget.upmat()

    def act_ln_movestep(self, ev):
        self.movestep = int(ev)
        self.dsb_mx.setSingleStep(self.movestep)
        self.dsb_my.setSingleStep(self.movestep)
        self.dsb_mz.setSingleStep(self.movestep)

    def act_ln_rotatestep(self, ev):
        self.rotatestep = int(ev)
        self.dsb_rx.setSingleStep(self.rotatestep)
        self.dsb_ry.setSingleStep(self.rotatestep)
        self.dsb_rz.setSingleStep(self.rotatestep)

    def loadinit(self, mainw):
        self.mainwindow = mainw
        self.maincomponents = mainw.components
        for comp in self.maincomponents:
            self.cmb_component.addItem(comp.getname())
        self.orgcomp = self.mainwindow.components[self.cmb_component.currentIndex()-1]
        self.comp = self.orgcomp.getcopy()
        self.mainwindow.glwidget.addtmpobj(self.comp.geoobj)
        self.mainwindow.glwidget.upmat()

    def act_cmb_change(self, i):
        self.mainwindow.glwidget.cleartmpobjs()
        self.orgcomp = self.maincomponents[i - 1]
        self.comp = self.orgcomp.getcopy()
        self.mainwindow.glwidget.addtmpobj(self.comp.geoobj)
        self.mainwindow.glwidget.upmat()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_4:
            self.dsb_mx.stepDown()

        elif event.key() == QtCore.Qt.Key_6:
            self.dsb_mx.stepUp()

        elif event.key() == QtCore.Qt.Key_2:
            self.dsb_my.stepDown()

        elif event.key() == QtCore.Qt.Key_8:
            self.dsb_my.stepUp()

        elif event.key() == QtCore.Qt.Key_Minus:
            self.dsb_mz.stepDown()

        elif event.key() == QtCore.Qt.Key_Plus:
            self.dsb_mz.stepUp()

        elif event.key() == QtCore.Qt.Key_PageUp:
            self.dsb_rx.stepUp()
        elif event.key() == QtCore.Qt.Key_PageDown:
            self.dsb_rx.stepDown()
        elif event.key() == QtCore.Qt.Key_Home:
            self.dsb_ry.stepUp()
        elif event.key() == QtCore.Qt.Key_End:
            self.dsb_ry.stepDown()
        elif event.key() == QtCore.Qt.Key_Slash:
            self.dsb_rz.stepUp()
        elif event.key() == QtCore.Qt.Key_Asterisk:
            self.dsb_rz.stepDown()



        else:
            pass
            # self.proceed()

        event.accept()

    def closeEvent(self, QCloseEvent):
        #self.act_btn_cancel()
        self.mainwindow.glwidget.cleartmpobjs()
        self.close