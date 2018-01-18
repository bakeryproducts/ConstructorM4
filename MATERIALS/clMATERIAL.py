class MATERIAL:
    def __init__(self,cat,name):
        self.category= cat
        self.name = name
        self.properties = {}

    def addprop(self,name,value):
        self.properties[name] = value

    def getprops(self):
        return self.properties.keys()

    def getquant(self,qname):
        return self.properties[qname]

    def getcategory(self):
        return self.category

    def getname(self):
        return self.name

