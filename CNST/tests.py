import re

with open('GEO\\korpus.geo') as f:
    data = f.read()

st = re.split('[;\n]',data)
pardict={}
flags = {}
points = []

for i,s in enumerate(st):
    s = re.sub(' ','',s)
    flag = re.search('.+:', s)
    if s[:4] == ':Par':
        pairpars = re.split(',', s[4:])
        for pairpar in pairpars:
            par, val = re.split('=', pairpar)#.strip(' '))
            pardict[par] = val
    elif s and s[0] == ':':
        continue
    elif flag:
        flagn = flag.group(0)
        flags[i] = flagn
        points.append(re.sub('.+:', '', s))
    else:
        points.append(s)

xl, yl = re.split(',', points[0])
newpoints = []
ppoints=[]
points = [point for point in points if point]

for i,point in enumerate(points):
    x,*y = re.split(',',point)
    print('STRING:',x,y[0],end=';\t')
    y=y[0]
    backval = points[i]
    for li,stepback in enumerate(('3','2','')):
        backpar = '#'+stepback
        if re.search(backpar, x):
            print('REPX:',backpar,'=>',(newpoints[i+li-3])[0],end=';\t')
            x = re.sub(backpar, (newpoints[i+li-3])[0], x)
            break
    for li, stepback in enumerate(('3', '2', '')):
        backpar = '#' + stepback
        if re.search(backpar, y):
            print('REPY:', backpar, '=>', (newpoints[i + li - 3])[1],end=';\t')
            y = re.sub(backpar, newpoints[i+li-3][1], y)
            break


    #print(x,y,end='\t')
    for k in pardict.keys():
        #print(k,pardict[k])
        x = re.sub(k, pardict[k], x)
        y = re.sub(k, pardict[k], y)

    xp,yp = eval(x),eval(y)#re.split('[+-]]',x)
    print('EVAL: ',x,';',y,' => ',xp,';',yp)
    #print(type(xp))
    xl,yl = str(xp),str(yp)

    newpoints.append([xl,yl])
    ppoints.append([xp,yp])

print(ppoints)
print(flags)
xs = [point[0]for point in ppoints]
ys = [point[1]for point in ppoints]

import numpy as np
from matplotlib import pyplot as plt

#plt.plot(ppoints[:])
# plt.figure()
# ax=gca()
plt.plot(xs,ys,'.r-')
plt.axis('equal')
#plt.show()


#print('\n'.join(points[:7]))
#print(npoints[:7])

# for k,v in pardict.items():
#     print(k,' = ',v)

