import depend
from Component_file import Printing
class Grass(Printing):
    def __init__(self, Matrice):
        self.Matrice = Matrice
        self.number = Matrice.mapsint
        self.color = (0, 1, 0)
        self.position = -1
        super().__init__(Matrice, self.color)