from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import mathutils as mth
from CNST.techs import *


def pick(mpos):
    RED = (1, 0, 0)
    glColor3fv(RED)
    radius = 50
    sph((*mpos, 0))
    glPushMatrix()
    glLoadIdentity()
    glBegin(GL_LINES)
    glVertex3fv((*mpos, -500))
    glVertex3fv((*mpos, 500))
    glEnd()

    glPopMatrix()


def seg(p1, p2):
    p1 = list(p1)
    p2 = list(p2)
    glColor3fv((1, 0, 0))
    # glPushMatrix()
    # glLoadIdentity()
    thickness = GLfloat(4)
    glLineWidth(thickness)

    glBegin(GL_LINES)
    glVertex3fv(p1[:3])
    glVertex3fv(p2[:3])
    glEnd()
    # glPopMatrix()


def model(modelgeo):
    verticies, faces = modelgeo[:2]

    glBegin(GL_TRIANGLES)
    # colors = setcolors(len(faces))
    for i, face in enumerate(faces):
        glColor3fv((.5, .3, .1))
        for point in face:
            glVertex3fv(verticies[point - 1])
    glEnd()

    try:
        edges = modelgeo[2]
        thickness = GLfloat(2)
        glLineWidth(thickness)
        glBegin(GL_LINES)
        glColor3fv((1, 1, 1))
        for edge in edges:
            for point in edge:
                glVertex3fv(verticies[point - 1])
        glEnd()
    except:
        pass


def getmv(sc,tr,ax,ay,mv):
    k=.1
    glPushMatrix()
    glLoadIdentity()
    glRotatef(ax * k, 0, 1, 0)
    glRotatef(ay * k, 1, 0, 0)
    glTranslatef(5*k*tr[0],-5*k*tr[1],0)
    glScalef(sc,sc,sc)
    glMultMatrixf(mv)
    mv = glGetDoublev(GL_MODELVIEW_MATRIX)
    glPopMatrix()
    return mv

def showgeo(mv, args, *drawfuncs):
    glPushMatrix()
    glLoadIdentity()
    glMultMatrixf(mv)

    if args == 0:
        pass
    elif len(args) == 1:
        drawfuncs[0](*args[0])
    else:
        for ai, func in enumerate(drawfuncs):
            func(*args[ai])

    glPopMatrix()


def sph(cd):
    #glColor3fv((0, 1, 0))
    glPushMatrix()
    glTranslate(*cd)
    quad = gluNewQuadric()
    gluSphere(quad, 10, 4, 4)
    glPopMatrix()


def sph2(*cds):
    glColor3fv((1, 0, 0))

    for cd in cds:
        glPushMatrix()
        glTranslate(*cd)
        quad = gluNewQuadric()
        gluSphere(quad, 80, 20, 20)
        glPopMatrix()


def getline(mpos):
    return ((*mpos, 100), (*mpos, 80))

def objcolors(obj):
    points= obj.getpoints()
    faces = obj.getfaces()
    colors = obj.getcolors()
    glBegin(GL_TRIANGLES)
    #colors = setcolors(1,len(faces))
    for i, face in enumerate(faces):
        glColor3ub(*colors[i])
        for point in face:
            glVertex3fv(points[point - 1])
    glEnd()

def drawobjplane(obj,planeid):
    points = obj.getpoints()
    faces = obj.getfaces()
    if planeid <= len(faces) and planeid > 0:
        glColor3fv((0.4, 1, 0.2))
        glBegin(GL_TRIANGLES)
        for point in faces[planeid - 1]:
            glVertex3fv(points[point - 1])
        glEnd()


def drawinbuf(objs,buf,mouse_pos,invislist):
    glBindFramebuffer(GL_FRAMEBUFFER, buf)
    r,g,b = 153/255,202/255,255/255
    glClearColor(r,g,b, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    for i,obj in enumerate(objs):
        if i not in invislist:
            obj.showcolors()
    objid, planeid = selectplane(mouse_pos)
    glBindFramebuffer(GL_FRAMEBUFFER, 0)
    return objid,planeid

def drawpic(obj,buf,w,h):
    # glDisable(GL_COLOR_MATERIAL)
    # glDisable(GL_LIGHT0)

    glBindFramebuffer(GL_FRAMEBUFFER, buf)
    r, g, b = 153 / 255, 202 / 255, 255 / 255
    glClearColor(r, g, b, 1.0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    obj.showcolors()
    clrmatr = glReadPixels(0, 0, w, h, GL_RGBA, GL_UNSIGNED_BYTE)
    depmatr = (GLfloat * (w*h))(0)
    #glReadPixels(0, 0, w, h, GL_DEPTH_COMPONENT, GL_FLOAT,depmatr)

    glBindFramebuffer(GL_FRAMEBUFFER, 0)

    # glEnable(GL_COLOR_MATERIAL)
    # glEnable(GL_LIGHT0)

    return clrmatr,depmatr

from ctypes import sizeof, c_float, c_void_p, c_uint, string_at
from PIL import Image

def newpic(obj,buf,w,h,size,ind):
    # glDisable(GL_COLOR_MATERIAL)
    # glDisable(GL_LIGHT0)
    # r, g, b = 153 / 255, 202 / 255, 255 / 255
    # glClearColor(r, g, b, 1.0)
    #print('starting ',buf)
    glBindBuffer(GL_PIXEL_PACK_BUFFER, buf)
    #data = 0
    #if ind<3:
    # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # obj.showcolors()
    # glReadPixels(0, 0, w, h, GL_BGRA, GL_UNSIGNED_BYTE,0)#, c_void_p(0))

    data = string_at(glMapBuffer(GL_PIXEL_PACK_BUFFER, GL_READ_ONLY), size)
    glUnmapBuffer(GL_PIXEL_PACK_BUFFER)


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    obj.showcolors()
    glReadPixels(0, 0, w, h, GL_BGRA, GL_UNSIGNED_BYTE,0)
    #depmatr = (GLfloat * (w*h))(0)
    #glReadPixels(0, 0, w, h, GL_DEPTH_COMPONENT, GL_FLOAT,depmatr)

    glBindBuffer(GL_PIXEL_PACK_BUFFER, 0)
    # glEnable(GL_COLOR_MATERIAL)
    # glEnable(GL_LIGHT0)

    return data

def multiset(obj, buf, w, h):
    glBindBuffer(GL_PIXEL_PACK_BUFFER, buf)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    obj.showcolors()
    glReadPixels(0, 0, w, h, GL_BGRA, GL_UNSIGNED_BYTE, 0)
    glBindBuffer(GL_PIXEL_PACK_BUFFER, 0)


def multiget(buf,size):
    glBindBuffer(GL_PIXEL_PACK_BUFFER, buf)

    data = string_at(glMapBuffer(GL_PIXEL_PACK_BUFFER, GL_READ_ONLY), size)
    glUnmapBuffer(GL_PIXEL_PACK_BUFFER)

    glBindBuffer(GL_PIXEL_PACK_BUFFER, 0)

    return data