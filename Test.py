import machine, neopixel, time, random, _thread
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
    
def Element():
    grass = list((mapsint,None,(0, 1, 0)))
    sn = list((1,27,(0,1,2)))
    apple = list((1,AppleRan(sn, None),(2,0,0)))
    print(apple)
    return apple,grass,sn


def AppleRan(sn, appleco):
    while True:
        apple=random.randint(0, mapsint-1)
        if(apple!=sn):
            if(appleco == None):
                return apple
            else:
                appleco[1] = apple
                return appleco 

def Move(dir):
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
    relat=(63,15,31,47,63,79,95,111)
    
    if(dir=="up"):
        for t in range(8):
            if(sn>= r[t-1] and sn<= l[t-1]):
                return relat[t]-sn
            
    elif(dir=="down"):
        for t in range(8):
            if(sn>=r[t-1] and sn<=l[t-1]):
                return relat[t-1]-sn
            
    elif(dir=="right"):
        for t in range(8):
            if(sn>=r[t-1] and sn<=l[t-1]):
                print(t%2)
                if(t%2==0):
                    for t in range(8):
                        if(sn==r[t]):
                            return l[t]
                    return sn-1
                else:
                    for t in range(8):
                        if(sn==l[t]):
                            return r[t]
                    return sn+1                    
    
    elif(dir=="left"):
        for t in range(8):
            if(sn>=r[t-1] and sn<=l[t-1]):
                print(t%2)
                if(t%2==0):
                    for t in range(8):
                        if(sn==l[t]):
                            return r[t]
                    return sn+1
                else:
                    for t in range(8):
                        if(sn==r[t]):
                            return l[t]
                    return sn-1 
    
    else:
        return sn
    
def Lesn(sn, snize,grass):
    snize.append(sn[1])
    if(len(snize) > sn[0]):
        Pri(list((1,snize[0],grass[2])))
        snize.pop(0)
    Pri(sn)

def Start(apple,grass,sn):
    Pri(grass)
    Pri(apple)
    Pri(sn)
    
def Eat(sn,apple):
    if(apple[1]==sn[1]):
        apple = AppleRan(sn, apple)
        sn[0] = sn[0]+1
        Pri(apple)


print("run")
apple, grass, sn = Element()
Start(apple,grass,sn)
dir="right"
snize =[sn[1]]
dir = Move(dir)
sn[1] = Snake(dir, sn[1])
while True:
    t1 = _thread.start_new_thread(Eat,(sn,apple))
    t2 = _thread.start_new_thread(Lesn,(sn,snize,grass))
    dir = Move(dir)
    time.sleep(0.1)