import numpy as np

def seekp(l, commonelems):
    cl = 2#len(commonelems)
    while l[:cl] != commonelems and l[:cl] != commonelems[::-1] :
        l = list(rotate(l, 1))
    return l

def rotate(l, n):
    return np.append(l[-n:], l[:-n], axis=0)


import time
import sys

a=time.clock()
time.sleep(1)
b = time.clock()
time.sleep(1)
c = time.clock()

print(b-a,c-a)


import numpy as np
#import wrtfiles
import mathutils.geometry as mth
# from mpl_toolkits.mplot3d import Axes3D
# from mpl_toolkits.mplot3d.art3d import Poly3DCollection
# import matplotlib.pyplot as plt

