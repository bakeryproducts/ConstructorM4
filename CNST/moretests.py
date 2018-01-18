import xml.etree.ElementTree as ET
file = "C:\\Users\\User\Documents\GitHub\ConstructorM4\MATERIALS\\KM.xml"

tree = ET.parse(file)
root = tree.getroot()

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

def getinto(root):
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
                getinto(el)
            except:
                pass
        elif  t == 'material':
            ch.setmat(a["name"])
            for ph in el[3]:
                ch.setprop([ph.attrib['displayname'],ph.attrib['value']])
    global arr
    arr.append(ch)

arr = []
getinto(root)

for obj in arr[:1]:
    m = obj.getmats()
    p = obj.getprops()
    print('Category: '+obj.name+'\n\t')
    for mat in m:
        print('\tMaterial name: '+mat)
        for prop in p:
            pn = prop[0]
            pv = prop[1]
            print('\t\t'+pn+(40-len(pn))*'_'+pv)
# for child in root:
#     if child.tag == 'classification':
#         print(child.tag,child.attrib)
#         for subch in child:
#             material = subch.attrib["name"]
#             print("\t",material)
#             #print("\t\t",subch[3].tag)
#             for prop in subch[3]:
#                 params = prop.attrib
#                 parname = params["displayname"]
#                 parval = params["value"]
#                 print("\t\t\t",parname,parval)
