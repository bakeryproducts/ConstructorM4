import numpy as np
import numpy.linalg as la

from PIL import Image,ImageOps
import  time

def getangle(a, b):
    if np.linalg.norm(a) != 1:
        a = a/np.linalg.norm(a)
    if np.linalg.norm(b) != 1:
        b =b/ np.linalg.norm(b)
    angle = np.arccos(np.clip(np.dot(a, b), -1, 1)) * 180 / np.pi
    return angle

def py_ang(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'    """
    cosang = np.dot(v1, v2)
    sinang = la.norm(np.cross(v1, v2))
    return np.arctan2(sinang, cosang)

n = 10000
w=690
h = 520



sx = np.random.normal(w/2,200,n)
sy = np.random.normal(h/2,200,n)
print(len(sx))
sx = (sx[np.where(abs(sx - w / 2) < w / 2 - 1)])
sy = (sy[np.where(abs(sy - h / 2) < h / 2 - 1)])
print(len(sx))
sx = list(map(int, np.rint(sx).astype(int)))
sy = list(map(int, np.rint(sy).astype(int)))

dic={}
dic['s'] = 1
for i in range(500):
    dic[i]=np.random.random()

im = Image.open('C:\\Users\\User\Documents\GitHub\ConstructorM4\RESULTS\\norm0.png')
datac = im.load()
st = time.time()
eq=[]
t=0
v1s=[]
b = np.array([0, 2, 1])

for i, x, y in zip(range(n), sx, sy):
    clr = datac[x, y]
    #print(clr)
    plid = clr[0] + clr[1] * 256
    oid = clr[2]
    if oid == 300:
        continue
    else:
        tmp = dic['s']
    a = np.array([np.random.random(),1,5])
    #cosang = np.dot(a, b)
    # sinang = la.norm(np.cross(a, b))
    # ang=np.arctan2(sinang, cosang)
    v1s.append(a)
    # ang = getangle(k,j)
    # cosang = np.abs(np.cos(ang * np.pi / 180))
    # eq.append(ang)
    t+=1
    # if t>3:
    #     break

m = np.array(v1s)

res1 = la.norm(np.cross(m,b),axis=1)
res2 = np.dot(m,b)
res = np.arctan2(res1,res2)

#res = [np.arctan2(v1,v2) for v1,v2 in zip(res2,res1) ]
# print(res)
# print(eq)
print(time.time()-st,t)
