#import stereo
import numpy as np
#import wrtfiles

# from mpl_toolkits.mplot3d import Axes3D
# from mpl_toolkits.mplot3d.art3d import Poly3DCollection
# import matplotlib.pyplot as plt


def sparerib(n, faces):
    ribsall = []
    for face in faces:
        iface = face[:]
        iface.append(iface[0])
        ribsall.append([iface[i:i + 2] for i in range(len(iface) - 1)])
    ribs = ribsall[n]
    # print(ribs)
    nneighbours = []
    for rib in ribs:
        for (i, ribface) in enumerate(ribsall):
            if rib[::-1] in ribface:
                nneighbours.append(i)
    # print(n,nneighbours)
    return nneighbours


def getfacepoints(face, rules):
    iface = []
    for point in face:
        iface.append(rules[point])
    return iface


def dist(point, plane):
    (v0, v1, v2) = np.array(plane[:3])
    e1 = v1 - v0
    e2 = v2 - v0
    (a, b, c) = np.cross(e1, e2)
    d = -np.dot((a, b, c), v1)

    eps = 1e-4
    if np.linalg.norm((a, b, c)) < eps:
        return 1e5
    r = abs(np.dot((a, b, c), point) + d)/ np.linalg.norm((a, b, c))
    # print(r)
    return r


def checkpl(pl1, pl2):
    #eps = 1e-2
    eps = planeparam
    for point in pl1:
        # print(abs(dist(point, pl2)))
        if dist(point, pl2) > eps:
            return False
    return True


def adddel(faces, face1, face2, newface):
    ifaces = faces[:]
    ifaces.append(newface)
    ifaces = [item for i, item in enumerate(ifaces) if i not in [face1, face2]]
    return ifaces


def rotate(l, n):
    return np.append(l[-n:], l[:-n], axis=0)


def seekpos(l, commonelems):
    el1, el2 = commonelems
    li = l[:]
    i = 0
    while (li[0] != el1 or li[1] != el2) and (li[0] != el2 or li[1] != el1):
        li = list(rotate(li, 1))
        if i == len(li):
            return False
        i += 1
    return li


def createf(f1, f2):
    common = list(set(f1).intersection(f2))
    if len(common) > 2:
        print("Too Many EL")
        return False
    ref1 = seekpos(f1, common)
    ref2 = seekpos(f2, common)
    return ref1[1:] + ref2[1:]


def getpair(faces, rules2):
    for num, face1 in enumerate(faces):
        neighs = sparerib(num, faces)
        pface1 = getfacepoints(face1, rules2)
        # print("%s has neighs:%s"%(num,neighs))
        for neigh in neighs:
            face2 = faces[neigh]
            pface2 = getfacepoints(face2, rules2)
            if checkpl(pface1, pface2):
                # print("%s and %s are in plane" % (num, neigh))
                tempface = createf(face1, face2)
                if type(tempface) == bool:
                    break
                if checkconv(getfacepoints(tempface, rules2)):
                    #print("%s + %s "%(num,neigh)+20 * "_" + " Done ")
                    return (num, neigh)
    return False


def getangle(e1, e2):
    cos = (np.dot(e1, e2)) / (np.linalg.norm(e1) * np.linalg.norm(e2))
    angle = np.arccos(cos - 1e-10)
    return np.degrees(angle)


def checkconv(iface):
    pface = iface[:]
    signsum = 0
    vects = getvect(list(pface))
    cross = getcross(vects)

    for vect in cross:
        si = np.sign(np.dot(vect, cross[0]))
        if si == 0:
            si += 1
        signsum += si
    if abs(signsum) != len(cross):
        return False
    return True


def getvect(plane):
    a, b = np.array(plane), np.array(rotate(plane, len(plane) - 1))
    return b - a


def getcross(vects):
    a, b = vects, rotate(vects, 1)
    crossprod = []
    for i in range(len(a)):
        crossprod.append(np.cross(a[i], b[i]))
    return crossprod


def remeshing(points, faces,plpar=1e-2):
    global planeparam
    planeparam=plpar

    values = range(1, 1 + len(points))
    keys = [repr(point) for point in points]
    # rules = dict(zip(keys, values))
    rules2 = dict(zip(values, points))

    allneighs = []
    for i in range(len(faces)):
        allneighs.append(sparerib(i, faces))
    t = 0
    while t < 1000:
        pair = getpair(faces, rules2)
        if not pair:
            #print("Thats all folks!")
            break
        else:
            (f1, f2) = pair
        uniface = createf(faces[f1], faces[f2])
        faces = adddel(faces, f1, f2, uniface)
        t += 1

    #print(len(faces))
    return points, faces


#(points, faces) = stereo.stlredo("test.stl", 100)
#rpoints, rfaces = remeshing(points, faces)

#wrtfiles.createtrg(points, faces, 10, "test")
#wrtfiles.createtrg(points, rfaces, 10, "testREMESH")


# values = range(1, 1 + len(rpoints))
# keys = [repr(point) for point in rpoints]
# rules = dict(zip(keys, values))
# rules2 = dict(zip(values, points))
#
# x = []
# y = []
# z = []
# verts = []
# fig = plt.figure()
# ax = Axes3D(fig)
#
# rf = [rfaces[206], rfaces[207]]
# for i, face in enumerate(rf):
#     x, y, z = [[], [], []]
#     for point in face:
#         p = rules2[point]
#         x.append(p[0])
#         y.append(p[1])
#         z.append(p[2])
#     ver = [list(zip(x, y, z))]
#     # verts.append(ver)
#     if i == 17 or i == 3:
#         clr = 'r'
#     else:
#         clr = 'k'
#     ax.add_collection3d(Poly3DCollection(ver, edgecolors=clr))
#
# ax.set_xlim(-200, 200)
# ax.set_ylim(-100, 300)
# ax.set_zlim(-200, 200)
#
# plt.show()
