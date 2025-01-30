import depend

class Matrice:
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
        Direct = depend.machine.Pin(pinButton, depend.machine.Pin.IN, depend.machine.Pin.PULL_UP)

class Grass():
    def __init__(self, Matrice):
        self.Matrice = Matrice
        self.number = Matrice.mapsint
        self.color = (0, 1, 0)
    def Pri(self):
        self.Matrice.Pri(self)


class Apple():
    def __init__(self, Matrice, snake):
        self.Matrice = Matrice
        self.quality = "ordinary"
        self.number = 1
        self.color = None
        self.score = 0
        self.size = 0
        self.timer = 0
        self.data = depend.json.load(open('proprety.json'))   
        self.position = self.AppleRan(snake, self.quality)    
    def AppleRan(self, snake, apple_quality = None):
        if(apple_quality == None):
            get_proprety = depend.random.choice(list(self.data.items()))
        else:
            get_proprety = [apple_quality,self.data[apple_quality]]
        self.quality = get_proprety[0]
        self.color = get_proprety[1]["color"]
        self.score = get_proprety[1]["score"]
        self.size = get_proprety[1]["size"]
        apple_position = depend.random.randint(0, self.Matrice.mapsint-1)
        rule = False
        for position in snake.position :
            if(apple_position == position):
                rule = True
        if(rule == True):
            AppleRan(sn)
        else:
            self.position = apple_position
            self.Matrice.Pri(self)
    def deathpown(self,grass,sn):
        self.timer = self.timer+1
        if(self.timer>20 and self.timer < 30):
            Matrice.Pri(self)
            depend.time.sleep(0.1)
            Matrice.Pri((self, (0, 1, 0)))
        elif(self.timer>30):
            self.timer = 0
            self.AppleRan(sn, apple)
            Matrice.Pri(self)
    def Pri(self):
        self.Matrice.Pri(self)
class Snake():
    def __init__(self, Matrice):
        self.Matrice = Matrice
        self.color = (0,1,2)
        self.position = [27]
        self.number = 1
        self.score = 0
        self.direction = "down"
    def Lose(self):
        for t in range(self.number):
            try:
                if(position[t+1] == position[0]):
                    return True
            except:
                pass
    def Eat(self, apple):
        if(apple.postion==self.position[0]):
            Effect(apple)
            apple.AppleRan(self)
    def Effect(self, apple):
        self.score += apple.score
        self.number += apple.size
    def Lesn(self, grass):
        self.position.append(self.position[0])
        if(len(position) > self.number):
            Matrice.Pri(list((1,self.position[0],grass.color)))
            self.position.pop(0)
        Matrice.Pri(list((number,self.position[0],grass.color)))
    def MovePad(self):
        if(up.value()==0):
            if(self.direction!="down"):
                 self.direction = "up"
        elif(down.value()==0):
            if(self.direction!="up"):
                self.direction = "down"
        elif(left.value()==0):
            if(self.direction!="right"):
                 self.direction = "left"
        elif(right.value()==0):
            if(self.direction!="left"):
                 self.direction = "right"
    def SnakeMove(self):
        u=(56,57,58,59,60,61,62,63)
        r=(0,8,16,24,32,40,48,56)
        l=(7,15,23,31,39,47,55,63)
        d=(0,1,2,3,4,5,6,7)
        relat=(63,15,31,47,63,79,95,111)
        
        if(self.direction=="up"):
            for t in range(8):
                if(self.position>= r[t-1] and self.position<= l[t-1]):
                    self.position = relat[t]-self.position
                
        elif(self.direction=="down"):
            for t in range(8):
                if(self.position>=r[t-1] and self.position<=l[t-1]):
                    self.position = relat[t-1]-self.position
                
        elif(self.direction=="right"):
            for t in range(8):
                if(self.position>=r[t-1] and self.position<=l[t-1]):
                    print(t%2)
                    if(t%2==0):
                        for t in range(8):
                            if(self.position==r[t]):
                                self.position = l[t]
                        self.position-1
                    else:
                        for t in range(8):
                            if(self.position==l[t]):
                                self.position = r[t]
                        self.position+1                    
        
        elif(self.direction=="left"):
            for t in range(8):
                if(self.position>=r[t-1] and self.position<=l[t-1]):
                    print(t%2)
                    if(t%2==0):
                        for t in range(8):
                            if(self.position==l[t]):
                                self.position = r[t]
                        self.position+1
                    else:
                        for t in range(8):
                            if(self.position==r[t]):
                                self.position = l[t]
                        self.position-1 
    def Pri(self):
        self.Matrice.Pri(self)       