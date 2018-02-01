#import stereo
import numpy as np
#import wrtfiles
import mathutils.geometry as mth
# from mpl_toolkits.mplot3d import Axes3D
# from mpl_toolkits.mplot3d.art3d import Poly3DCollection
# import matplotlib.pyplot as plt

def getdicts(faces,pi2p):
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
    eps = 1e-2
    for point in pl1:
        # print(abs(dist(point, pl2)))
        if dist(point, pl2) > eps:
            return False
    return True


def adddel(faces, face1, face2, newface):
    ifaces = faces[:]
    ifaces.append(newface)
    i1,i2 = np.sort([face1,face2])
    del(ifaces[i2])
    del(ifaces[i1])
    return ifaces


def rotate(l, n):
    return np.append(l[-n:], l[:-n], axis=0)


def seekpos(l, commonelems):
    el1, el2 = commonelems[:2]
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

def checkplanar(planes,plane,eps):
    # M is matrix [Nx3] vectors = points
    results = []
    for ind,M in enumerate(planes):
        (v0, v1, v2) = plane[:3]
        e1 = v1 - v0
        e2 = v2 - v0
        normal = np.cross(e1, e2)
        nlen = np.linalg.norm(normal)
        normal = normal / nlen
        if np.sum(np.abs(M.dot(normal)))<eps:
            res = ind
        else:
            res = -1
        results.append(ind)
    return results


def getpair(faces, pi2p,T):
    edgesdict,facesdict = getdicts(faces,pi2p)
    eps = 1e-1
    for ind1, face1 in enumerate(faces):
        neighs,neighedges = sparerib(ind1,face1,edgesdict)
        return 0
        pface1=facesdict[ind1]
        #print(pface1)
        #print(neighs)
        pneighs = [facesdict[neigh] for neigh in neighs]
        indplneigh = checkplanar(pneighs,pface1,eps)
        plneighs = [neighs[i] for i in indplneigh if i !=-1]
        plneighsedges = [neighedges[i] for i in indplneigh if i !=-1]
        if not plneighs:
            continue
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
                print(neighs,neighedges)
                print(ind1,neigh)
                return (ind1, neigh,edge)
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


def remeshing(points, faces):
    #faces = np.array(faces)
    #points = np.array(points)

    values = range(1, 1+len(points))
    #keys = [repr(point) for point in points]
    pi2p = dict(zip(values, points))

    t = 0
    while t < 88:
        *pair,edge = getpair(faces, pi2p,t)
        if not pair:
            #print("Thats all folks!")
            break
        else:
            (f1, f2) = pair
        if t==87:
            break
        uniface = gennew(faces[f1], faces[f2],edge)
        faces = adddel(faces, f1, f2, uniface)
        t += 1
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



def remeshingNew(points,faces):
    points = np.array(points)
    faces = np.array(faces)
    edges = []
    edgesdict={}
    for i,face in enumerate(faces):
        tf = np.append(face,face[0])
        iedge=[]
        for j in range(len(tf)-1):
            p1,p2 = tf[j],tf[j+1]
            t1,t2 = min(p1,p2),max(p1,p2)
            iedge.append(np.array([p1,p2]))
            edgesdict.setdefault(str(t1)+'-'+str(t2), []).append(i)
        edges.append(np.array(iedge))

    pdict = {ind+1:poi for ind,poi in zip(range(len(points)),points)}
    pfaces =[]
    for face in faces:
        iface=[]
        for ind in face:
            iface.append(pdict[ind])
        pfaces.append(iface)

    pedges = [pdict[ind] for iedges in edges for edge in iedges for ind in edge ]

    planechecked=set()
    planardict={}
    restfaces=set()
    for ind,face in enumerate(pfaces):
        if ind not in planechecked:
            restpoints = np.array([point-face[0] for i,point in enumerate(points,start=1)])# if i not in faces[ind]])
            dists = {i:dist for i, dist in enumerate(getdist(restpoints,face),start=1)}
            for iind,iface in enumerate(faces):
                res = [dists[i] for i in iface]
                if iind != ind and np.sum(res) < 1:
                    planardict.setdefault(ind, []).append(iind)
                    planechecked.add(iind)
                else:
                    restfaces.add(ind)
                planechecked.add(ind)

    print(len(restfaces),len(faces))
    restfaces = [faces[i] for i in restfaces]
    resfaces=[restfaces]
    flind=-1
    for k,plfaces in planardict.items():
        plfaces.append(k)
        lfaces=plfaces[:]
        compfaces = [faces[i] for i in lfaces]
        #compedges,cedict = creedges(compfaces)
        while True:
            compedges, cedict = creedges(compfaces)
            pair,edge,fin = get2neighs(compfaces,compedges,cedict,flind)
            #print(pair,edge)
            #break
            if pair:
                n1,n2 = pair[:2]
                tmpface = gennew(list(compfaces[n1]),list(compfaces[n2]),edge)
                print(tmpface)
                tmppface = [points[i-1] for i in tmpface]
                if not checkconv(tmppface):
                    flind=fin
                    continue
                else:
                    flind=-1
                if not tmpface:
                    continue
                compfaces.append(np.array(tmpface))
                #print(compfaces)
                del(compfaces[n2])
                del(compfaces[n1])
            else:
                break
        resfaces.append(compfaces)

    resfaces = [i for sl in resfaces for i in sl]
    res = setback(resfaces)
    print(setback(list(faces)))
    print(res)

    return list(points),res


def creedges(faces):
    edges = []  # np.array(np.zeros(len(faces)))
    edgesdict = {}
    for i, face in enumerate(faces):
        tf = np.append(face, face[0])
        iedge = []
        for j in range(len(tf) - 1):
            p1, p2 = tf[j], tf[j + 1]
            t1, t2 = min(p1, p2), max(p1, p2)
            iedge.append(np.array([p1, p2]))
            edgesdict.setdefault(str(t1) + '-' + str(t2), []).append(i)
        edges.append(np.array(iedge))
    return edges,edgesdict

def get2neighs(faces,edges,edgesdict,find):
    for ind,face,nedges in zip(range(len(faces)),faces,edges):
        for edge in nedges:
            p1, p2 = edge
            t1, t2 = min(p1, p2), max(p1, p2)
            pair=edgesdict[str(t1) + '-' + str(t2)]
            if len(pair)>1 and ind!=find:
                return pair,edge,ind
    return None,None,None

def setback(faces):
    rfaces=[]
    for face in faces:
        rfaces.append(list(face))
    return rfaces


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