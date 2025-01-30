import depend
from Class import Matrice,Button,Snake,Apple,Grass

def Element():
    #Def Material
    matrice = Matrice(3)
    up = Button(4)
    down = Button(5)
    left = Button(6)
    right = Button(7)
    #Def Game
    grass = Grass(matrice)
    grass.Pri()
    sn = Snake(matrice)
    apple = Apple(matrice, sn)
    
Element()