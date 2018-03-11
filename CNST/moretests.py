import numpy as np
from time import time

# n = 500
# st = time()
# N = 1080
# w=722
# h=522
# for i in range(N):
#     sx = np.random.normal(0,100,n)
#     sy = np.random.normal(0,100, n)
#     sx = (sx[np.where(abs(sx - w / 2) < w / 2 - 1)]).astype(int)
#     sy = (sy[np.where(abs(sy - h / 2) < h / 2 - 1)]).astype(int)
#
#

a = np.array([[1,0],[1,0]])
b = np.array([[10,29,3,15],[0,3,5,1]])
#print(b)
print(b[a[0],a[1]])

# print(time()-st)