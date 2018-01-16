from CNST.clELEM import *

class DZ(ELEM):
    def getcopy(self):
        return DZ(self.geoobj.getcp())

