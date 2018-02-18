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

class Ui_shootset(QtGui.QWidget):
    def __init__(self):
        super(Ui_shootset, self).__init__()
        self.setupUi(self)
        #self.mainwindow = 0

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(338, 436)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 4, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 5, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.radioButton_2 = QtGui.QRadioButton(Form)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.gridLayout.addWidget(self.radioButton_2, 1, 1, 1, 1)
        self.radioButton = QtGui.QRadioButton(Form)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.gridLayout.addWidget(self.radioButton, 2, 1, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout.addWidget(self.widget)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Shooting settings", None))
        self.lineEdit.setText(_translate("Form", "1000", None))
        self.lineEdit_2.setText(_translate("Form", "0", None))
        self.label_3.setText(_translate("Form", "1 Angle", None))
        self.label_2.setText(_translate("Form", "Velocity", None))
        self.lineEdit_3.setText(_translate("Form", "0", None))
        self.label_4.setText(_translate("Form", "2 Angle", None))
        self.label_5.setText(_translate("Form", "Projectile", None))
        self.radioButton_2.setText(_translate("Form", "Shaped-charge", None))
        self.radioButton.setText(_translate("Form", "Armor-Piercing", None))
        self.label.setText(_translate("Form", "Projectile type:", None))

