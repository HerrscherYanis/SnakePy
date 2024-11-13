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


def AppleRan():
    return (1,random.randint(0, mapsint-1),(2,0,0))

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
    r=(0,15,16,31,32,47,48,63)
    l=(7,8,23,24,39,40,55,56)
    d=(0,1,2,3,4,5,6,7)
    
    if(dir=="up"):
        print("Wip")
        return sn
    elif(dir=="down"):
        print("Wip")
        return sn
    elif(dir=="right"):
        for t in r-1:
            if(sn==r[t]):
                return l[t]
        return sn-1
    elif(dir=="left"):
        print("Wip")
        return sn 
    else:
        return sn
    
def Start():
    sn = (1,27,(0,1,2))
    Pri(Grass())
    Pri(AppleRan())
    Pri(sn)
    return sn
    
print("run")
sn = list(Start())
dir="right"
while True:
    dir = Move(dir)
    sn[1] = Snake(dir, sn[1])
    print(sn[1])