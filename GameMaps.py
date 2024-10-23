import machine, neopixel, time, random

class Maps:
    def __init__(self, mapsint):
        self.mapsint = mapsint

    np = neopixel.NeoPixel(machine.Pin(14), mapsint)

    for i in range(self.mapsint):
        np[i] = (0, 1, 0)
    
    np.write()
    time.sleep(10)
    for i in range(self.mapsint):
        np[i] = (0, 0, 0)
    np.write()

#def AppleRan:
 #   np[random.randint(0, mapsint-1)] = (2,0,0)