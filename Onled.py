import machine, neopixel, time, random
mapsint = 64
up = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
down = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
left = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
right = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_UP)
np = neopixel.NeoPixel(machine.Pin(3), mapsint)

def Pri(color):
    if(color[1] == None):
        for i in range(color[0]):
            np[i] = color[2]
    else:
        np[color[1]] = color[2]
    np.write()
    
def Grass():
    return (mapsint,None,(0, 1, 0))


def AppleRan(sn):
    while True:
        apple=random.randint(0, mapsint-1)
        if(apple!=sn):
            return (1,apple,(2,0,0))

def Move(dir):
    time.sleep(0.1)
    if(up.value()==0):
        return "up"
    elif(down.value()==0):
        return "down"
    elif(left.value()==0):
        return "left"
    elif(right.value()==0):
        return "right"
    else:
        return dir

def Snake(dir, sn):
    u=(56,57,58,59,60,61,62,63)
    r=(0,8,16,24,32,40,48,56)
    l=(7,15,23,31,39,47,55,63)
    d=(0,1,2,3,4,5,6,7)
    relat=(15,31,47,63,79,95,101,63)
    
    if(dir=="up"):
        for t in range(8):
            if(sn==u[t]):
                return d[t]
        for t in range(8):
            if(sn>=r[t] and sn<=l[t]):
                return relat[t]-sn
            
    elif(dir=="down"):
        for t in range(8):
            if(sn==d[t]):
              return u[t]
        for t in range(8):
            if(sn>=r[t] and sn<=l[t]):
                return relat[t-1]-sn
            
    elif(dir=="right"):
        for t in range(8):
            if(sn==r[t]):
                return l[t]
        return sn-1
    
    elif(dir=="left"):
        for t in range(8):
            if(sn==l[t]):
                return r[t]
        return sn+1
    
    else:
        return sn
    
def Start(sn):
    Pri(Grass())
    Pri(sn)

print("run")
sn = list((1,27,(0,1,2)))
Pri(AppleRan(sn[1]))
dir="right"

while True:
    Start(sn)
    dir = Move(dir)
    sn[1] = Snake(dir, sn[1])
    print(sn[1])