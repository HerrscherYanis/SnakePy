import depend

class Matric:
    def __init__(self, pinMap):
        self.mapsint = 64
        self.np = depend.neopixel.NeoPixel(depend.machine.Pin(pinMap), self.mapsint)
    def Pri(self, Class_Obj, color = None):
        if(color == None):
            color = Class_Obj.color
        try:
            self.np[Class_Obj.position] = color
        except:
            for i in range(Class_Obj.number):
                self.np[i] = color
        self.np.write()

class Button:
    def __init__(self, pinButton):
        self.value = depend.machine.Pin(pinButton, depend.machine.Pin.IN, depend.machine.Pin.PULL_UP)