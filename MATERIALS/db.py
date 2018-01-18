import xml.etree.ElementTree as ET


class froot:
    def __init__(self, name):
        self.name = name
        self.mats = []
        self.props = []

    def setmat(self, newmat):
        self.mats.append(newmat)

    def setprop(self,prop):
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
    def __init__(self,file):
        self.file = file
        self.tree = ET.parse(self.file)
        self.root = self.tree.getroot()
        self.arr = []
        self.getinto(self.root)

    def getinto(self,root):
        try:
            ch = froot(root.attrib['name'])
        except:
            ch = froot(root.attrib)
        for el in root:
            t = el.tag
            a = el.attrib
            if t == 'classification':
                #ch.setbio(a)
                try:
                    self.getinto(el)
                except:
                    pass
            elif  t == 'material':
                ch.setmat(a["name"])
                for subel in el:
                    aa = subel.tag
                    if aa =='physicalproperties':
                        prop = []
                        for subsubel in subel:
                            phys = subsubel.attrib
                            prop.append([phys['displayname'],phys['value']])
                        ch.setprop(prop)
                # for ph in el[3]:
                #     ch.setprop([ph.attrib['displayname'],ph.attrib['value']])

        self.arr.append(ch)

    def getres(self):
        return self.arr

    def getcats(self):
        res = []
        for obj in self.arr[:-1]:
            res.append(obj.name)
        return res

    def getcatmat(self,cat):
        for obj in self.arr[:-1]:
            if obj.name == cat:
                return (obj.getmats(),obj.getprops())

    def getmat(self,mat):
        for obj in self.arr[:-1]:
            ms = obj.getmats
            for mat in ms:
                pass

    def export(self,Mobj):
        for obj in self.arr[:-1]:
            m = obj.getmats()
            p = obj.getprops()
            print('Category: ' + obj.name + '\n\t')
            for mat in m:
                print('\tMaterial name: ' + mat)
                for prop in p:
                    pn = prop[0]
                    pv = prop[1]
                    print('\t\t' + pn + (40 - len(pn)) * '_' + pv)


    def show(self):
        for obj in self.arr[:2]:
            m = obj.getmats()
            p = obj.getprops()
            print('Category: ' + obj.name + '\n\t')
            for mat,props in zip(m,p):
                print('\tMaterial name: ' + mat)
                for prop in props:
                    pn = prop[0]
                    pv = prop[1]
                    print('\t\t' + pn + (40 - len(pn)) * '_' + pv)


db = DB('KM.xml')
#arr = db.getres()
db.show()