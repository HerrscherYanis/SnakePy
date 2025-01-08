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
    grass = Grass(matrice.mapsint,(0, 1, 0))
    sn = Snake(1,27,(0,1,2),0)
    apple = Apple(1,AppleRan(sn, None),(2,0,0),"ordinary")
    print(apple)
    return apple,grass,sn