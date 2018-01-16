from PyQt4 import QtGui
import sys

from glwidget import *


class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        # self.glWidget = GLWidget()
        # mainLayout = QtGui.QHBoxLayout()
        # mainLayout.addWidget(self.glWidget)
        # self.setLayout(mainLayout)
        #

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
