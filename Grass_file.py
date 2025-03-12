import depend
from Component_file import Printing

class Grass(Printing):
    def __init__(self,Matrice):
        super().__init__(Matrice)
        self.number = Matrice.mapsint
        self.color = (0, 1, 0)