import xml.etree.ElementTree as ET
from MATERIALS.clMATERIAL import MATERIAL


class froot:
    def __init__(self, name):
        self.name = name
        self.mats = []
        self.props = []

    def setmat(self, newmat):
        self.mats.append(newmat)

    def setprop(self, prop):
        self.props.append(prop)

    def getprops(self):
        return self.props

    def getmats(self):
        return self.mats

    def child(self, name):
        child = froot(name)
        child.setmat(self.mats)
        return child


class DB:
    def __init__(self, file):
        self.file = file
        self.tree = ET.parse(self.file)
        self.root = self.tree.getroot()
        self.__arr = []
        self.getinto(self.root)

    def getinto(self, root):
        try:
            ch = froot(root.attrib['name'])
        except:
            ch = froot(root.attrib)
        for el in root:
            t = el.tag
            a = el.attrib
            if t == 'classification':
                # ch.setbio(a)
                try:
                    self.getinto(el)
                except:
                    pass
            elif t == 'material':
                ch.setmat(a["name"])
                for subel in el:
                    tt = subel.tag
                    if tt == 'physicalproperties':
                        prop = []
                        for subsubel in subel:
                            phys = subsubel.attrib
                            prop.append([phys['displayname'], phys['value']])
                        ch.setprop(prop)
                        # for ph in el[3]:
                        #     ch.setprop([ph.attrib['displayname'],ph.attrib['value']])

        self.__arr.append(ch)

    def getres(self):
        return self.__arr

    def getcats(self):
        res = []
        for obj in self.__arr[:-1]:
            res.append(obj.name)
        return res

    def getcatmat(self, cat):
        for obj in self.__arr[:-1]:
            if obj.name == cat:
                return obj.getmats()#, obj.getprops()

    def exportall(self):
        objarr = []
        for obj in self.__arr[:-1]:
            m, p = obj.getmats(), obj.getprops()
            for mat, props in zip(m, p):
                matobj = MATERIAL(obj.name, mat)
                for prop in props:
                    pn, pv = prop
                    matobj.addprop(pn, pv)
                objarr.append(matobj)
        return objarr

    def exportmat(self,matname):
        for obj in self.__arr[:-1]:
            m, p = obj.getmats(), obj.getprops()
            for mat, props in zip(m, p):
                if mat == matname:
                    matobj = MATERIAL(obj.name,mat)
                    for prop in props:
                        pn, pv = prop
                        matobj.addprop(pn,pv)
                    return matobj

    def show(self):
        for obj in self.__arr[:1]:
            m, p = obj.getmats(), obj.getprops()
            print('Category: ' + obj.name + '\n\t')
            for mat, props in zip(m, p):
                print('\tMaterial name: ' + mat)
                for prop in props:
                    pn, pv = prop
                    print('\t\t' + pn + (40 - len(pn)) * '_' + pv)


db = DB('GOST.xml')
#db.show()
cats = db.getcats()
matscat0 = db.getcatmat(cats[0])
newobj = db.exportmat(matscat0[0])
print(newobj.properties)