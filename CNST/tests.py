import numpy as np
from clDZ import *
from clGEOOBJ import *
from OpenGL.GLU import *
from clDZBLOCK import *
from draw import getmv,drawinbuf
import glfw
import techs


def initi(dw, dh):
    glClearColor(0.8, 0.8, 0.8, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-dw / 2, dw / 2, -dh / 2, dh / 2, -1500, 1500)
    glMatrixMode(GL_MODELVIEW)
    # glEnable(GL_CULL_FACE)



def main():
    wwi, whei = (800, 800)
    if not glfw.init():
        return
    window = glfw.create_window(wwi, whei, "My OpenGL window", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    initi(wwi,whei)

    rotx, roty = 0, 0
    current_mouse_pos, prev_mouse_pos,rev_mouse_pos = (0, 0), (0, 0),(0,0)
    mvMatrix = np.identity(4)
    timer = 0
    dt=.001
    time=0
    sc=1
    tr = 0,0
    glEnable(GL_DEPTH_TEST)
    FBO = fbufinit(wwi, whei)


    saugeo = techs.georedo("sau.stl",10)
    sau = GEOOBJ(saugeo)
    sau.setcoord((-400, 0, 0))
    pl = 171
    orgs = []
    for org in sau.faces[pl]:
        orgs.append(sau.points[org-1])
    org = orgs[1]
    norm = list(sau.getnormaltoface(pl))


    geos = techs.georedo("dz.stl",20)
    geoobj = GEOOBJ(geos)
    dzelement = DZ(geoobj)
    dzelement.geoobj.setrotate((0,90,0))


    nx, ny = 8, 2
    dx,dy = 45, 25
    offs = (10,40,0.1)
    dzblock = DZBLOCK(dzelement,org,norm,nx,ny,dx,dy,offs)
    #dzblock.stats()

    while not glfw.window_should_close(window):
        glfw.poll_events()
        mvMatrix = getmv(sc,tr,rotx, roty, mvMatrix)

        objid, planeid = drawinbuf([sau,dzblock],FBO,rev_mouse_pos)

        glClearColor(0.2, 0.2, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        for obj in (sau,dzblock):
            if obj.showplane(planeid,objid) == 1:
                break
        sau.show()
        dzblock.show()

        if time>timer+dt:
            sau.update(mvMatrix)
            dzblock.update(mvMatrix)
            mouse_state, rotx, roty,sc,tr = techs.checkmouse(window, prev_mouse_pos)
            timer=time+dt

        prev_mouse_pos = glfw.get_cursor_pos(window)
        rev_mouse_pos =prev_mouse_pos[0],whei-prev_mouse_pos[1]

        time = glfw.get_time()
        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()
