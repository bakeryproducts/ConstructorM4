import re
import pickle

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
                #flags[sind]=''
    return name,points,pardict,flags

def importges(path,outpardict=None):
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
    if outpardict:
        pardict = outpardict

    xl, yl = re.split(',', list(points.values())[0])

    points = list(points.items())
    newpoints = []
    ppoints={}
    points = [point for point in points if point[1]]
    func={}

    for i,pair in enumerate(points):
        sind,s = pair
        x, *l = re.split(',', s)
        print('STRING ',sind,': ','\t', x, l[0], end=';\t')
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
        else:
            for ind, point in ppoints.items():
                if set(val) == set(point):
                    prevind = ind
                    break
            if len(l) > 1:
                    func[prevind] = l[-1]

            if sind in flags.keys():
                flags[prevind]=flags[sind]
            if prevind in flags.keys():
                flags[sind] = flags[prevind]

    arcdict, galtdict = funcredo(func)

    corrflags = {}
    for k,v in flags.items():
        if k in ppoints.keys():
            corrflags[k] = v

    return name, ppoints, corrflags, arcdict, galtdict,freverse,pardict
