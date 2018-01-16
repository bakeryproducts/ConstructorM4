class RESH:
    def __init__(self,geo):
        self.geoobj = geo.getcp()

    def show(self):
        self.geoobj.show()

    def update(self,mvMatrix):
        self.geoobj.update(mvMatrix)
