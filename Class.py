import depend

class Matrice:
    mapsint = 64
    def __init__(self, pinMap):
        np = depend.neopixel.NeoPixel(depend.machine.Pin(self.pinMap), mapsint)

class Button:
    def __init__(self, pinButton):
        Direct = depend.machine.Pin(self.pinButton, depend.machine.Pin.IN, depend.machine.Pin.PULL_UP)


class :
    def __init__(self, number, position, color):
        self.number = number 
        self.position = position
        self.color = color



    sn = list((1,27,(0,1,2),0))
    apple = list((1,AppleRan(sn, None),(2,0,0),"ordinary"))