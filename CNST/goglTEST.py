import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import mathutils as mth
from stereo import stlredo
from draw import *
from techs import *



def initi(dw, dh):
    pygame.init()
    pygame.display.set_mode((dw, dh), DOUBLEBUF | OPENGL)
    pygame.display.gl_set_attribute(GL_DEPTH_SIZE, 32)
    #glClearColor(0.529, 0.529, 0.529, 0.0)
    #gluPerspective(90, (display[0] / display[1]), 0.01, 50.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-dw / 2, dw / 2, -dh / 2, dh / 2, -500, 500)
    #gluPerspective(90,1,1,400)
    glMatrixMode(GL_MODELVIEW)
    #glEnable(GL_CULL_FACE)


def main():

    points, faces = stlredo("cube100.stl", 1)

    verticies,faces,edges = pfredo(points,faces)

    modelgeo = verticies,faces,edges
    modelg = verticies,faces

    wwi, whei = (400, 400)
    dflag = 0
    adx,ady=0,0
    cpos, ppos = (0, 0), (0, 0)
    mpos=(0,0)
    nspd = .2
    mv = np.identity(4)

    initi(wwi, whei)


    while True:
        glClearColor(0.529, 0.529, 0.529, 0.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        mouse = pygame.mouse.get_pos()
        mou = mouse[0], whei - mouse[1]
        #drawselected(modelgeo, mou)
        #[modelgeo, mou]
        pars = [[(0,0,0)]]
        mv = mrot(modelgeo, nspd, adx, ady, mv, pars,sph)
        sph((0,0,0))




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    dflag = 1

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    dflag = 0
                    adx,ady=0,0
                    mpos = pygame.mouse.get_pos()
                    #mpos = (mpos[0] - wwi / 2, -mpos[1] + whei / 2)

        cpos = pygame.mouse.get_pos()

        if dflag == 1:
            adx = cpos[0] - ppos[0]
            ady = cpos[1] - ppos[1]

        ppos = pygame.mouse.get_pos()
        pygame.display.flip()
        pygame.time.wait(100)


if __name__ == '__main__':
    main()
