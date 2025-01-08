import depend
#from Class import
mapsint = 64
up = depend.machine.Pin(4, depend.machine.Pin.IN, depend.machine.Pin.PULL_UP)
down = depend.machine.Pin(5, depend.machine.Pin.IN, depend.machine.Pin.PULL_UP)
left = depend.machine.Pin(6, depend.machine.Pin.IN, depend.machine.Pin.PULL_UP)
right = depend.machine.Pin(7, depend.machine.Pin.IN, depend.machine.Pin.PULL_UP)
np = depend.neopixel.NeoPixel(depend.machine.Pin(3), mapsint)

def Pri(color):
    if(color[1] == None):
        for i in range(color[0]):
            np[i] = color[2]
    else:
        np[color[1]] = color[2]
    np.write()
    
def Element():
    grass = list((mapsint,None,(0, 1, 0)))
    sn = list((1,27,(0,1,2),0))
    apple = list((1,AppleRan(sn, None),(2,0,0),"ordinary"))
    print(apple)
    return apple,grass,sn


def AppleRan(sn, appleco):
    while True:
        apple=depend.random.randint(0, mapsint-1)
        if(apple!=sn):
            if(appleco == None):
                return apple
            else:
                appleco[1] = apple
                return appleco

def Quality(apple,sn):
    rand = depend.random.randint(0, 9)
    if(rand == 0):
        apple[3] = "poisoned"
        apple[2] = (2,2,3)
        return apple
    elif(rand == 1):
        apple[3] = "golden"
        apple[2] = (2,2,0)
        return apple
    #elif(rand == 2 and sn[0] > 1):
        #apple[3] = "laxative"
        #apple[2] = (2,1,2)
        #return apple
    elif(rand == 3):
        apple[3] = "hiden"
        apple[2] = (0,3,0)
        return apple
    elif(rand == 4):
        apple[3] = "evil"
        apple[2] = (0,0,0)
        return apple
    elif(rand == 5):
        apple[3] = "angel"
        apple[2] = (0,0,0)
        return apple
    else:
        apple[3] = "ordinary"
        apple[2] = (2,0,0)
        return apple
              

def Move(dir):
    if(up.value()==0):
        if(dir=="down"):
            return dir
        else:
            return "up"
    elif(down.value()==0):
        if(dir=="up"):
            return dir
        else:
            return "down"
    elif(left.value()==0):
        if(dir=="right"):
            return dir
        else:
            return "left"
    elif(right.value()==0):
        if(dir=="left"):
            return dir
        else:
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
    
def Lesn(sn,snize,grass):
    snize.append(sn[1])
    if(len(snize) > sn[0]):
        Pri(list((1,snize[0],grass[2])))
        snize.pop(0)
    Pri(sn)

def Start(apple,grass,sn):
    Pri(grass)
    Pri(apple)
    Pri(sn)
    
def Effect(sn,apple):
    if(apple[3] == "ordinary"):
        sn[3] = sn[3]+1
        sn[0] = sn[0]+1
    elif(apple[3] == "golden"):
        sn[3] = sn[3]+5
        sn[0] = sn[0]+1
    elif(apple[3] == "laxative"):
        sn[0] = sn[0]-1
    elif(apple[3] == "hiden"):
        sn[3] = sn[3]+5
        sn[0] = sn[0]+1
    elif(apple[3] == "poisoned"):
        sn[3] = sn[3]-10
        sn[0] = sn[0]+0
    elif(apple[3] == "evil"):
        sn[3] = sn[3]-30
        sn[0] = sn[0]+1
    elif(apple[3] == "angel"):
        sn[3] = sn[3]+30
        sn[0] = sn[0]+0
    #elif(apple[3] == "cherry"):
        #sn[0] = sn[0]+1
        
def Eat(sn,apple):
    if(apple[1]==sn[1]):
        Effect(sn,apple)
        apple = AppleRan(sn, apple)
        apple = Quality(apple,sn)
        Pri(apple)

def Lose(snize, sn):
    for t in range(sn[0]):
        if(snize[t] == sn[1]):
            return True

def GameOver():
    Pri(list((mapsint,None,(0, 1, 0))))
    depend.time.sleep(1)
    Pri(list((mapsint,None,(1, 1, 0))))

def deathpown(timer,apple,grass,sn):
    timer= timer+1
    if(timer>20 and timer < 30):
        Pri(apple)
        depend.time.sleep(0.1)
        Pri((None, apple[1], grass[2]))
    elif(timer>30):
        timer = 0
        apple = AppleRan(sn, apple)
        apple = Quality(apple,sn)
        Pri(apple)
        print(apple)
    return timer
        
def StartMain():
    apple, grass, sn = Element()
    Start(apple,grass,sn)
    dir="right"
    snize =[sn[1]]
    timer= 0;
    while True:
        Eat(sn,apple)
        Lesn(sn,snize,grass)
        dir = Move(dir)
        sn[1] = Snake(dir, sn[1])
        depend.time.sleep(0.3)
        timer = deathpown(timer,apple,grass,sn)
        if(Lose(snize, sn)==True):
            break
print("run")
StartMain()
GameOver()