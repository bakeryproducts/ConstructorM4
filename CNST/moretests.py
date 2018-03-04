import time
# import numpy as np
# n=5
# w,h=600,500
# sx = np.random.normal(0,100, n)
# sy = np.random.normal(0,100, n)
# sx = (sx[np.where(abs(sx - w / 2) < w / 2 - 1)])
# sy = (sy[np.where(abs(sy - h / 2) < h / 2 - 1)])
# sx = sx.astype(int)
# sy = np.int_(sy)
#
# print(type(sy[0]))
# #sx = list(map(int, np.rint(sx).astype(int)))
# # sy = list(map(int, np.rint(sy).astype(int)))
# #print(sx)
# print(time.time()-start)


import re
start = time.time()

def foo(*xs):
    print(xs)
    xs = re.split(',',str(xs))
    #xs = str(1),str(0)
    pars = ['a%','b%']

    st = 'a% and b%'
    for ch,x in zip(pars,xs):
        st = re.sub(ch, x, st)
    return eval(st)

#print(time.time()-start)
#foo(1,1)
class test:
    def fsvinit(self):
        func = '''
def moo(ARGS):
    t = FSV
    return t
        '''
        func = re.sub('ARGS','a%,b%',func)
        func = re.sub('FSV', 'a% and b%', func)
        #print(func)
        exec(func,globals())
        #print(moo(1, 1))
        return moo

    #fmoo = fsvinit()


print(5*[0])

bo = glGenFramebuffers(1)
tex = glGenTextures(1)

glBindTexture(GL_TEXTURE_2D, tex)

glTexImage2D(GL_TEXTURE_2D, 0, GL_DEPTH_COMPONENT32,wwi,whei, 0, GL_DEPTH_COMPONENT, GL_FLOAT, 0)

glBindFramebuffer(GL_FRAMEBUFFER, bo)

glFramebufferTexture(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT,  tex, 0)


glDrawBuffer(GL_NONE)