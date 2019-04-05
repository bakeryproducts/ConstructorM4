import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from stl import mesh
from sys import exit

from PyQt5 import QtCore, QtGui, QtWidgets



def fbufinit(wwi, whei):
    pick_texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, pick_texture)

    depth_buff = glGenRenderbuffers(1)
    glBindRenderbuffer(GL_RENDERBUFFER, depth_buff)
    glRenderbufferStorage(GL_RENDERBUFFER, GL_DEPTH_COMPONENT, wwi, whei)

    FBO = glGenFramebuffers(1)
    glBindFramebuffer(GL_FRAMEBUFFER, FBO)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, wwi, whei, 0, GL_RGB, GL_FLOAT, None)
    glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, pick_texture, 0)
    glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_RENDERBUFFER, depth_buff)

    glBindFramebuffer(GL_FRAMEBUFFER, 0)
    glBindTexture(GL_TEXTURE_2D, 0)

    return FBO

def pbosinit(w,h):
    pbos = glGenBuffers(3)
    nbytes = w*h*4
    for pbo in pbos:
        glBindBuffer(GL_PIXEL_PACK_BUFFER,pbo)
        glBufferData(GL_PIXEL_PACK_BUFFER,nbytes,None,GL_STREAM_READ)
    glBindBuffer(GL_PIXEL_PACK_BUFFER,0)
    return pbos,nbytes

def setcolors(id, n):
    ind = np.arange(n) + 1
    colors = []
    for i in ind:
        r = (i & 0x000000FF) >> 0
        g = (i & 0x0000FF00) >> 8
        b = id  # (i & 0x00FF0000) >> 16
        colors.append((r, g, b))
    return colors


def georedo(filename, scale):
    try:

        mymesh = mesh.Mesh.from_file(filename)
    except FileNotFoundError as e:
        print("No such file in \GEO\ : " + filename)
        print(e)
        exit(0)
    except:
        print("Error opening .stl geometry")
        exit(0)
    points = []
    a = mymesh.v0
    b = mymesh.v1
    c = mymesh.v2
    abc = []

    for t in [a, b, c]:
        allmeshp = []
        for point in t:
            ipoint = []
            for cd in point:
                t = round(scale * float(cd), 2)
                ipoint.append(t)
            allmeshp.append(ipoint)
        abc.append(allmeshp)

    numpoints = []
    for t in abc:
        for point in t:
            if repr(list(point)) not in points:
                points.append(repr(list(point)))
                #numpoints.append(list(point))
                numpoints.append(np.array(list(point)))

    values = range(1, 1 + len(points))
    keys = [point for point in points]
    rules = dict(zip(keys, values))

    faces = []

    for i in range(len(a)):
        p1 = rules[repr(list(abc[0][i]))]
        p2 = rules[repr(list(abc[1][i]))]
        p3 = rules[repr(list(abc[2][i]))]
        #faces.append([p1, p2, p3])
        faces.append(np.array([p1, p2, p3]))


    edges = getedges(faces)

    return numpoints, faces, edges

def getedges(faces):
    edges = []
    for face in faces:
        iface = face[:]
        #iface.append(face[0])
        iface = np.append(iface,face[0])
        for i in range(len(iface) - 1):
            edge = [iface[i], iface[i + 1]]
            #if (edge not in edges) and (list(reversed(edge)) not in edges):
            edges.append(edge)
    return edges


def selectplane(mpos):
    color = glReadPixels(*mpos, 1, 1, GL_RGB, GL_UNSIGNED_BYTE)
    plid = color[0] + color[1] * 256  # + color[2] * 256 * 256
    oid = color[2]
    print(oid,plid)
    return oid, plid


def getscale(points):
    numpoints = np.array(points)
    x, y, z = [numpoints[:, i] for i in (0, 1, 2)]
    deltas = [i.max() - i.min() for i in (x, y, z)]
    maxd = max(deltas)
    axis = [i for i, d in enumerate(deltas) if d == maxd][0]
    return axis, maxd


def getortangles(n):
    if n == (0, 0, 0):
        return (0, 0, 0)
    orts = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    if np.linalg.norm(n) != 1:
        n = n / np.linalg.norm(n)
    angles = np.array([getangle(n, ort) for ort in orts])

    return angles


def getangle(a, b):
    if np.linalg.norm(a) != 1:
        a = a/np.linalg.norm(a)
    if np.linalg.norm(b) != 1:
        b =b/ np.linalg.norm(b)
    angle = np.arccos(np.clip(np.dot(a, b), -1, 1)) * 180 / np.pi
    return angle



class Signal():
    class Emitter(QtCore.QObject):
        registered = QtCore.pyqtSignal(tuple)

        def __init__(self):
            super(Signal.Emitter, self).__init__()


    def __init__(self):
        self.emitter = Signal.Emitter()

    def register(self,arg):
        self.emitter.registered.emit(arg)

    def connect(self, slot):
        self.emitter.registered.connect(slot)

