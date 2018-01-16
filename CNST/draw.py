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
    glColor3fv((0, 1, 0))
    glPushMatrix()
    glTranslate(*cd)
    quad = gluNewQuadric()
    gluSphere(quad, 10, 20, 20)
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