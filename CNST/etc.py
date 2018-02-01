import numpy as np
import mathutils.geometry as mth
import sys
import time

def seekp(l, commonelems):
    cl = len(commonelems)
    while l[:cl] != commonelems and l[:cl] != commonelems[::-1] :
        l = list(rotate(l, 1))
    return l

def gennew(f1, f2,edge):
    common = list(edge)#list(set(f1).intersection(f2))

    ref1 = seekp(list(f1), common)
    ref2 = seekp(list(f2), common)
    return ref1[len(common)-1:] + ref2[len(common)-1:]

def getdicts(ffaces,ppi2p):
    global faces, pi2p
    ribsdict = {}
    facesdict = {}
    for ind, face in enumerate(faces):
        facesdict[ind] = np.array([pi2p[pi] for pi in face])

        fface = np.append(face, face[0])
        for i in range(len(fface) - 1):
            t1, t2 = np.sort(fface[i:i + 2])
            ribsdict.setdefault(str(t1) + '-' + str(t2), []).append(ind)
    return ribsdict,facesdict

def sparerib(ind,face,ribsdict):
    nneighbours = []
    ribs = []
    fface = np.append(face,face[0])
    for i in range(len(fface)-1):
        t1, t2 = np.sort(fface[i:i + 2])
        nneighbours.append(ribsdict[str(t1)+'-'+str(t2)])
        ribs.append([t1,t2])
    nneighbours = [i for sl in nneighbours for i in sl if i != ind]
    return nneighbours,ribs

def adddel(faces, face1, face2, newface):
    ifaces = faces[:]
    ifaces.append(newface)
    i1,i2 = np.sort([face1,face2])
    del(ifaces[i2])
    del(ifaces[i1])
    return ifaces

def rotate(l, n):
    return np.append(l[-n:], l[:-n], axis=0)

def checkplanar(planes,plane,eps):
    # M is matrix [Nx3] vectors = points
    results = []
    for ind,M in enumerate(planes):
        (v0, v1, v2) = plane[:3]
        e1 = v1 - v0
        e2 = v2 - v0
        normal = np.cross(e1, e2)
        nlen = np.linalg.norm(normal)
        if nlen==0:
            #print(M.shape[0] * [-1])
            return (M.shape[0] * [-1])
        #print(normal,nlen)
        normal = normal / nlen
        if np.sum(np.abs(M.dot(normal)))<eps:
            #print(ind,np.sum(np.abs(M.dot(normal))))
            res = ind
        else:
            res = -1
        results.append(res)
    return results

def getpair(ffaces, ppi2p):
    global faces,pi2p
    #faces,pi2p = ffaces,ppi2p


    edgesdict,facesdict = getdicts(faces,pi2p)
    eps = 1e2
    for ind1, face1 in enumerate(faces):
        t0 = time.clock()
        neighs,neighedges = sparerib(ind1,face1,edgesdict)
        t1 = time.clock()
        pface1=facesdict[ind1]
        pneighs = [facesdict[neigh] for neigh in neighs]
        indplneigh = checkplanar(pneighs,pface1,eps)
        plneighs = [neighs[i] for i in indplneigh if i !=-1]
        plneighsedges = [neighedges[i] for i in indplneigh if i !=-1]
        if not plneighs:
            continue
        t2 = time.clock()
        for neigh,edge in zip(plneighs,plneighsedges):
            face2 = faces[neigh]
            tempface = gennew(face1, face2,edge)
            #print(face1,face2,tempface)
            if type(tempface) == bool:
                continue
            ptempface = [pi2p[i] for i in tempface]
            if checkconv(ptempface):
                #print("%s + %s "%(ind,neigh)+20 * "_" + " Done ")
                #print(ind1, neigh, tempface)
                # print(neighs,neighedges)
                # print(indplneigh)
                # print(plneighs,plneighsedges)
                # print(ind1,neigh)
                t3 = time.clock()
                #print('\t\t',(t1-t0)/(t3-t1),(t2-t1)/(t3-t1),(t3-t2)/(t3-t1))
                return (ind1, neigh,edge)
    t3 = time.clock()
    #print('\t\t\t',(t1-t0)/(t3-t1))
    return False,False,False

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

def remeshing(ppoints, ffaces):
    #faces = np.array(faces)
    #points = np.array(points)
    global faces
    global points
    faces = ffaces
    points = ppoints

    values = range(1, 1+len(points))
    #keys = [repr(point) for point in points]
    global pi2p
    pi2p = dict(zip(values, points))

    t = 0
    while t < 35:
        stime = time.clock()
        *pair,edge = getpair(faces, pi2p)
        t1 = time.clock()
        #print(pair)
        if not (pair[0]and pair[1]):
            #print("Thats all folks!")
            break
        else:
            (f1, f2) = pair

        uniface = gennew(faces[f1], faces[f2],edge)
        faces = adddel(faces, f1, f2, uniface)
        t += 1
        t2 = time.clock()
        print((t1-stime))
        print(t)
    return points, setback(faces)

def getdist(M,plane):
    # M is matrix [Nx3] vectors = points
    (v0, v1, v2) = plane[:3]
    e1 = v1 - v0
    e2 = v2 - v0
    normal = np.cross(e1, e2)
    nlen  = np.linalg.norm(normal)
    normal = normal/nlen
    normal = normal
    result = np.abs(M.dot(normal))
    return result

def setback(faces):
    rfaces=[]
    for face in faces:
        rfaces.append(list(face))
    return rfaces

