class MATERIAL:
    # _ids=[]

    def __init__(self,cat,name):
        self.category = cat
        self.name = name
        self.properties = {}
        #self.id=0
        #self.setid()

    # def setid(self):
    #     maxid = len(self._ids)
    #     for i in range(maxid):
    #         if i not in self._ids:
    #             self._ids.append(i)
    #             self.id = i
    #             return i
    #     self._ids.append(maxid)
    #     self.id = maxid
    #     return maxid
    #
    # def __del__(self):
    #     self._ids.remove(self.id)

    def addprop(self,name,value):
        self.properties[name] = value

    def getprops(self):
        return self.properties

    def getquant(self,qname):
        return self.properties[qname]

    def getcategory(self):
        return self.category

    def getname(self):
        return self.name

