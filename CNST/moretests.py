import time
import numpy as np
n=150000
w,h=620,520
start = time.time()

tt = np.zeros((w,h,4))

for i in range(n):
    # sx = np.random.normal(0,100, n)
    # sy = np.random.normal(0,100, n)
    # sx = (sx[np.where(abs(sx - w / 2) < w / 2 - 1)]).astype(int)
    # sy = (sy[np.where(abs(sy - h / 2) < h / 2 - 1)]).astype(int)
    #sx = sx.astype(int)
    t = tt[0,0]
    tes=t[2]
    tess = t[0]+10*t[1]
    # sy = np.int_(sy)
    # sx = list(map(int, np.rint(sx).astype(int)))
    # sy = list(map(int, np.rint(sy).astype(int)))
#print(sx)

print(time.time()-start)

