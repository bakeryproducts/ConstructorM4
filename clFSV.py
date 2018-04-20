import numpy
import re

class FSV:
    def __init__(self,cat):
        category = cat



    def fsvinit(self, fsvstring):
        func = '''
def fsv(ARGS):
    t = FSV
    return t
    '''
        compstr = ''
        for i, comp in enumerate(self.components):
            compstr += comp.getname() + ','

        func = re.sub('ARGS', compstr[:-1], func)
        func = re.sub('FSV', fsvstring, func)
        print(func)
        exec(func, globals())

    def fsvact(self, ids):
        li = len(self.components) * [0]
        for id in ids:
            li[id] = 1
        return fsv(*li)