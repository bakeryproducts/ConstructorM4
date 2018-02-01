import time
import numpy as np


def rotate(l, n):
    return np.append(l[-n:], l[:-n], axis=0)


def getdicts(faces, pi2p, whl):
    ribsdict = {}
    facesdict = {}
    for ind, face in enumerate(faces):
        if ind in whl:
            facesdict[ind] = np.array([pi2p[pi] for pi in face])
            fface = np.append(face, face[0])
            for i in range(len(fface) - 1):
                t1, t2 = fface[i:i + 2]#np.sort(fface[i:i + 2])
                ribsdict.setdefault(str(t1) + '-' + str(t2), []).append(ind)
    return ribsdict, facesdict


def sparerib(ind, face, ribsdict):
    nneighbours = []
    ribs = []
    fface = np.append(face, face[0])
    for i in range(len(fface) - 1):
        t1, t2 = reversed(fface[i:i + 2]) #np.sort(fface[i:i + 2])
        nneighbours.append(ribsdict[str(t1) + '-' + str(t2)])
        ribs.append([t1, t2])
    nneighbours = [i for sl in nneighbours for i in sl if i != ind]
    return nneighbours, ribs


def getpair(faces, rules2, planedict, whitelist):
    edgesdict, facesdict = getdicts(faces, rules2, whitelist)

    for ind, face in enumerate(faces):
        if ind in whitelist:
            #print(ind,face)
            neighs, nedges = sparerib(ind, face, edgesdict)
            #print(face,faces[neighs[0]],nedges)
            for neigh, edge in zip(neighs, nedges):
                #print('\t', neigh in whitelist)
                if neigh in planedict[ind] and neigh in whitelist:
                    #print('\t\t',face, neigh,edge)
                    tempface = gennew(face, faces[neigh], edge)
                    if not tempface:
                        continue
                    ptempface = [rules2[i] for i in tempface]
                    #print('\t\t',tempface)
                    if checkconv(ptempface):
                        return (ind, neigh, edge)
    #print(whitelist)
    return False, False, False


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
    # print(signsum,len(cross))
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


def remeshing(points, faces):
    values = range(1, 1 + len(points))
    rules2 = dict(zip(values, points))

    nfaces = np.array(faces)
    npoints = np.array(points)
    pdict = {ind + 1: poi for ind, poi in zip(range(len(npoints)), npoints)}
    pfaces = []
    for face in nfaces:
        iface = []
        for ind in face:
            iface.append(pdict[ind])
        pfaces.append(iface)
    pldict = planars(pfaces, nfaces, npoints)
    wholeplanedict = {}
    for k, v in pldict.items():
        wholeplanedict[k] = v
        for pl in v:
            nv = v[:]
            nv.remove(pl)
            nv.append(k)
            wholeplanedict[pl] = nv

    for i in range(len(faces)):
        try:
            wholeplanedict[i]
        except:
            wholeplanedict[i] = []

    # for k,v in wholeplanedict.items():
    #     print(k,v)

    wl = list(range(len(faces)))
    t = 0
    startt = time.clock()
    while t < 1000:
        t0 = time.clock()
        *pair, edge = getpair(faces, rules2, wholeplanedict, wl)
        t1 = time.clock()
        if not (pair[0] or pair[1]):
            # print("Thats all folks!")
            break
        f1, f2 = pair
        faces.append(gennew(faces[f1], faces[f2], edge))
        newitem = wl[-1] + 1
        wl.append(newitem)
        wl.remove(f1)
        wl.remove(f2)
        dicadd(wholeplanedict, newitem, f1)
        # wholeplanedict[newitem] = wholeplanedict[f1][:]
        # wholeplanedict.setdefault(newitem, []).append(f1)
        # print(f1,wholeplanedict[f1])
        # print(f2,wholeplanedict[f2])

        del (wholeplanedict[f1])
        del (wholeplanedict[f2])
        t += 1
        # print(pair)
        #print(t1 - t0)
    faces = [faces[i] for i in wl]
    print(time.clock() - startt)
    return points, faces


def dicadd(pldict, newitem, f1):
    for k, v in pldict.items():
        if f1 in v:
            pldict.setdefault(k, []).append(newitem)
    pldict[newitem] = pldict[f1]
    pldict.setdefault(newitem, []).append(f1)


def seekp(l, commonelems):
    cl = len(commonelems)
    t=0
    while l[:cl] != commonelems and l[:cl] != commonelems[::-1]:
        l = list(rotate(l, 1))
        t+=1
        # if t>20:
        #     print(50*'#',commonelems,l)
        #     return False
    return l


def gennew(f1, f2, edge):
    common = list(edge)
    #common = list(set(f1).intersection(f2))
    ref1 = seekp(list(f1), common)
    ref2 = seekp(list(f2), common)
    # if not(ref1 and ref2) and not common:
    #     return False
    return ref1[len(common) - 1:] + ref2[len(common) - 1:]


def planars(pfaces, faces, points):
    planechecked = set()
    planardict = {}
    eps = 1e-1
    for ind, face in enumerate(pfaces):
        if ind not in planechecked:
            restpoints = np.array([point - face[0] for i, point in enumerate(points, start=1)])
            dists = {i: dist for i, dist in enumerate(getdist(restpoints, face), start=1)}
            for iind, iface in enumerate(faces):
                res = [dists[i] for i in iface]
                if iind != ind and np.sum(res) < eps:
                    planardict.setdefault(ind, []).append(iind)
                    planechecked.add(iind)
                planechecked.add(ind)
    return planardict


def getdist(M, plane):
    # M is matrix [Nx3] vectors = points
    (v0, v1, v2) = plane[:3]
    e1 = v1 - v0
    e2 = v2 - v0
    normal = np.cross(e1, e2)
    nlen = np.linalg.norm(normal)
    normal = normal / nlen
    result = np.abs(M.dot(normal))
    return result
