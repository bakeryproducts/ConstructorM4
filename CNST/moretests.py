
import ctypes
import numpy
from OpenGL.GL import *
#from OpenGL.GL import shaders
from PyQt4 import QtGui, QtOpenGL


class MyWidget(QtOpenGL.QGLWidget):


    def initializeGL(self):
        glViewport(0, 0, self.width(), self.height())
        self.data = numpy.array([0.0, 0.5, 0.0, 1.0,
                                  0.5, -0.366, 0.0, 1.0,
                                  -0.5, -0.366, 0.0, 1.0,
                                  ],
                                 dtype=numpy.float32)

        # triangle position and color
        vertexData  = self.data
        # create VAO
        self.VAO = glGenVertexArrays(1)
        glBindVertexArray(self.VAO)

        # create VBO  
        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, vertexData.nbytes, self.data, GL_DYNAMIC_DRAW)

        # enable array and set up data  
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 4, GL_FLOAT, GL_FALSE, 0, None)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

    def paintGL(self):
        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glBindVertexArray(self.VAO)

        # draw triangle  
        glDrawArrays(GL_TRIANGLES, 0, 3)

        glBindVertexArray(0)



def main():
    import sys

    app = QtGui.QApplication(sys.argv)

    glformat = QtOpenGL.QGLFormat()
    glformat.setVersion(3, 3)
    glformat.setProfile(QtOpenGL.QGLFormat.CoreProfile)
    w = MyWidget(glformat)
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()  