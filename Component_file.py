import depend

class Matrice:
    def __init__(self, pinMap):
        self.mapsint = 64
        self.np = depend.neopixel.NeoPixel(depend.machine.Pin(pinMap), self.mapsint)

class Button:
    def __init__(self, pinButton):
        self.value = depend.machine.Pin(pinButton, depend.machine.Pin.IN, depend.machine.Pin.PULL_UP)
        
class Printing:
    def __init__(self, Matrice, color, position = None):
        self.Matrice = Matrice
        self.color = color
        self.positionsave = position
    def Pri(self, color = None):
        if(color == None):
            color = self.color
        if type(self.position) == int:
            if self.position == -1:
                for i in range(self.number):
                    self.Matrice.np[i] = color
            else:
                self.Matrice.np[self.position] = color
        else:
            self.Matrice.np[self.positionsave] = color
            for i in self.position:
                self.Matrice.np[i] = self.color
            self.positionsave = self.position[-1]
        self.Matrice.np.write()