import depend

class Matrice:
    mapsint = 64
    def __init__(self, pinMap):
        np = depend.neopixel.NeoPixel(depend.machine.Pin(self.pinMap), mapsint)

class Button:
    def __init__(self, pinButton):
        Direct = depend.machine.Pin(self.pinButton, depend.machine.Pin.IN, depend.machine.Pin.PULL_UP)


class Grass:
    def __init__(self, number, color):
        self.number = number 
        self.color = color

class Apple:
    def __init__(self, number, position, color,score):
        self.number = number 
        self.position = position
        self.color = color
        self.score = score

class Snake:
    def __init__(self, number, position, color,quality):
        self.number = number 
        self.position = position
        self.color = color
        self.quality = quality