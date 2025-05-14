import depend
from Component_file import Printing

class Snake(Printing):
    def __init__(self, Matrice, up , down, right , left):
        self.Matrice = Matrice
        self.up = up
        self.down = down
        self.right = right
        self.left = left
        self.color = (0,1,2)
        self.position = [27]
        self.score = 0
        self.direction = "down"
        super().__init__(self.Matrice, self.color, self.position[0])
    def Lose(self):
        x = 0
        for t in self.position:
            if(self.position[0] == t):
                x = x + 1
        if(x >= 2):
            return True
        else:
            return False
        print(x)
    def Eat(self, apple):
        if(apple.position == self.position[0]):
            apple.timer = 0
            self.Effect(apple)
            apple.AppleRan(self)
    def Effect(self, apple):
        self.score += apple.score
        if self.score <= 0: 
            self.score = 0
        self.Regsn(apple.size)
    def Regsn(self, lenght):
        if lenght <= 0:
            for x in range(abs(lenght)):
                if not len(self.position) <= 1:
                    self.position.pop(-1)
                    self.Pri((0,1,2))
        else:
            self.position.insert(0,self.position[0])
        
    def MovePad(self):
        if(self.up.value()==0):
            if(self.direction!="down"):
                 self.direction = "up"
        elif(self.down.value()==0):
            if(self.direction!="up"):
                self.direction = "down"
        elif(self.left.value()==0):
            if(self.direction!="right"):
                 self.direction = "left"
        elif(self.right.value()==0):
            if(self.direction!="left"):
                 self.direction = "right"
    def SnakeMove(self):
        u=[56,57,58,59,60,61,62,63]
        r=[0,8,16,24,32,40,48,56]
        l=[7,15,23,31,39,47,55,63]
        d=[0,1,2,3,4,5,6,7]
        relat=[63,15,31,47,63,79,95,111]
        if(self.direction=="up"):
            for t in range(8):
                if(self.position[0]>=r[t-1] and self.position[0]<=l[t-1]):
                    if(t%2==0):
                        if self.position[0] in r:
                            self.position.insert(0,l[r.index(self.position[0])])
                        else:
                            self.position.insert(0, self.position[0]-1)
                    else:
                        if self.position[0] in l:
                            self.position.insert(0,r[l.index(self.position[0])])
                        else:
                            self.position.insert(0, self.position[0]+1)
                    self.position.pop(-1)
                
        elif(self.direction=="down"):
            for t in range(8):
                if(self.position[0]>=r[t-1] and self.position[0]<=l[t-1]):
                    if(t%2==0):
                        if self.position[0] in l:
                            self.position.insert(0,r[l.index(self.position[0])])
                        else:
                            self.position.insert(0, self.position[0]+1)
                    else:
                        if self.position[0] in r:
                            self.position.insert(0,l[r.index(self.position[0])])
                        else:
                            self.position.insert(0, self.position[0]-1)
                    self.position.pop(-1)
                
        elif(self.direction=="right"):
            for t in range(8):
                if(self.position[0] >= r[t] and self.position[0] <= l[t]):
                    self.position.insert(0, relat[t]-self.position[0])
                    self.position.pop(-1)
                    break
        
        elif(self.direction=="left"):
            for t in range(8):
                if(self.position[0] >= r[t] and self.position[0] <= l[t]):
                    try:
                        self.position.insert(0, relat[t+1]-self.position[0])
                    except:
                        self.position.insert(0, relat[0]-self.position[0])
                    self.position.pop(-1)
                    break