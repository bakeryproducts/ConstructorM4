import re

def funcredo(funcs):
    arcdict={}
    gdict={}
    for k,func in funcs.items():
        if func[:3]=='Arc':
            params = re.findall('\(.+\)', func)
            params = params[0][1:-1]
            lparams = params.split(',')
            for param in lparams:
                skip, v = param.split('=')
                arcdict[k] = float(v)
        elif func[:4]=='Galt':
            t = re.findall('{.+}', func)
            gdict[k] = re.sub('[\{\}]', '', t[0])

    return arcdict,gdict

def getinfo(st):
    pardict = {}
    flags = {}
    points = {}
    name='test'
    for i, s in enumerate(st):
        if s:
            sind = re.sub('\|.+','',s)
            s = re.sub('.+\|','',s)
            s = re.sub(' ', '', s)
            #print(sind+'->'+s)
            flag = re.search('.+:', s)
            if s[:4] == ':Par':
                pairpars = re.split(',', s[4:])
                for pairpar in pairpars:
                    par, val = re.split('=', pairpar)
                    pardict[par] = val
            elif s[:6] == ':detal':
                name = s[6:]
            elif s and s[0] == ':':
                continue
            elif flag:
                flagn = flag.group(0)
                flags[sind] = flagn[:-1]
                points[sind] = re.sub('.+:', '', s)
            else:
                points[sind] = s
    return name,points,pardict,flags

def importges(path):
    freverse = False
    #path = 'GEO\\korpus.geo'
    with open(path) as f:
        data = f.read()

    prest = re.split('[;\n]',data)
    #st = [str(i)+'|'+s for i,s in enumerate(st) if s[-2:]!='-1']
    st=[]
    for i,s in enumerate(prest):
        flagcheck = re.split(',',re.sub(' ', '', s))
        if flagcheck[-1] != '-1':
            st.append(str(i)+'|'+s)
        else:
            pass#freverse=True

    name,points,pardict,flags = getinfo(st)

    xl, yl = re.split(',', list(points.values())[0])

    points = list(points.items())
    newpoints = []
    ppoints={}
    points = [point for point in points if point[1]]
    func={}

    for i,pair in enumerate(points):
        sind,s = pair
        x, *l = re.split(',', s)
        print('STRING:', x, l[0], end=';\t')
        y = l[0]
        for li, stepback in enumerate(('3', '2', '')):
            backpar = '#' + stepback
            if re.search(backpar, x):
                print('REPX:',backpar,'=>',(newpoints[i+li-3])[0],end=';\t')
                x = re.sub(backpar, (newpoints[i + li - 3])[0], x)
                break
        for li, stepback in enumerate(('3', '2', '')):
            backpar = '#' + stepback
            if re.search(backpar, y):
                print('REPY:', backpar, '=>', (newpoints[i + li - 3])[1],end=';\t')
                y = re.sub(backpar, newpoints[i + li - 3][1], y)
                break

        for k in pardict.keys():
            #print(k,pardict[k])
            x = re.sub(k, pardict[k], x)
            y = re.sub(k, pardict[k], y)

        xp,yp = eval(x),eval(y)#re.split('[+-]]',x)
        if yp<0:
            continue
        print('EVAL: ',x,';',y,' => ',xp,';',yp)
        #print(type(xp))
        xl,yl = str(xp),str(yp)

        newpoints.append([xl,yl])
        val = (xp,yp/2,0)
        if val not in ppoints.values():
            ppoints[sind] = val
            if len(l) > 1:
                func[sind] = l[-1]
        elif len(l) > 1:
            for ind,point in ppoints.items():
                if set(val) == set(point):
                    func[ind] = l[-1]
            #func[sind] = l[-1]




    arcdict, galtdict = funcredo(func)
    rpoints = []
    # for p in ppoints:
    #     if p not in rpoints:
    #         rpoints.append(p)
    return name, ppoints, flags, arcdict, galtdict,freverse

    # return 0
    # for i,point in enumerate(points):
    #     x,*l = re.split(',',point)
    #     #
    #     # print('STRING:',x,l[0],end=';\t')
    #     y=l[0]
    #     for li,stepback in enumerate(('3','2','')):
    #         backpar = '#'+stepback
    #         if re.search(backpar, x):
    #             #print('REPX:',backpar,'=>',(newpoints[i+li-3])[0],end=';\t')
    #             x = re.sub(backpar, (newpoints[i+li-3])[0], x)
    #             break
    #     for li, stepback in enumerate(('3', '2', '')):
    #         backpar = '#' + stepback
    #         if re.search(backpar, y):
    #             #print('REPY:', backpar, '=>', (newpoints[i + li - 3])[1],end=';\t')
    #             y = re.sub(backpar, newpoints[i+li-3][1], y)
    #             break
    #
    #     for k in pardict.keys():
    #         #print(k,pardict[k])
    #         x = re.sub(k, pardict[k], x)
    #         y = re.sub(k, pardict[k], y)
    #
    #     xp,yp = eval(x),eval(y)#re.split('[+-]]',x)
    #     #print('EVAL: ',x,';',y,' => ',xp,';',yp)
    #     #print(type(xp))
    #     xl,yl = str(xp),str(yp)
    #
    #     newpoints.append([xl,yl])
    #
    #     #print(l)
    #     if (xp,yp/2,0) not in ppoints:
    #         ppoints.append((xp,yp/2,0))
    #         if len(l) > 1:
    #             func[len(ppoints)] = l[-1]
    #     elif len(l) > 1:
    #         func[len(ppoints)] = l[-1]
    #
    # arcdict, galtdict = funcredo(func)
    # rpoints = []
    # for p in ppoints:
    #     if p not in rpoints:
    #         rpoints.append(p)
    # return name,rpoints,flags,arcdict, galtdict

#print(importges('s'))