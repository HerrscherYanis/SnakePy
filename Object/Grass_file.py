import depend

class Grass():
    def __init__(self, Matrice):
        self.Matrice = Matrice
        self.number = Matrice.mapsint
        self.color = (0, 1, 0)
    def Pri(self):
        self.Matrice.Pri(self)