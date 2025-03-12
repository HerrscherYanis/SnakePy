import depend
from Component_file import Printing

class Snake(Printing):
    def __init__(self, Matrice, up , down, right , left):
        super().__init__(Matrice)
        self.up = up
        self.down = down
        self.right = right
        self.left = left
        self.color = (0,1,2)
        self.position = 27
        self.number = 1
        self.score = 0
        self.direction = "down"
        
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
                 
    def Move(self):
        u=(56,57,58,59,60,61,62,63)
        r=(0,8,16,24,32,40,48,56)
        l=(7,15,23,31,39,47,55,63)
        d=(0,1,2,3,4,5,6,7)
        relat=(63,15,31,47,63,79,95,111)
        
        if(self.direction == "up"):
            for t in range(8):
                if(self.position >= r[t-1] and self.position <= l[t-1]):
                    self.position = relat[t]-self.position
                
        elif(self.direction == "down"):
            for t in range(8):
                if(self.position >= r[t-1] and self.position <= l[t-1]):
                    self.position = relat[t-1]-self.position
                
        elif(self.direction == "right"):
            for t in range(8):
                if(self.position >= r[t-1] and self.position <= l[t-1]):
                    if(t%2 == 0):
                        for t in range(8):
                            if(self.position == r[t]):
                                self.position = l[t]
                        self.position = self.position-1
                    else:
                        for t in range(8):
                            if(self.position == l[t]):
                                self.position = r[t]
                        self.position = self.position+1                    
        
        elif(self.direction == "left"):
            for t in range(8):
                if(self.position >= r[t-1] and self.position <= l[t-1]):
                    if(t%2 == 0):
                        for t in range(8):
                            if(self.position == l[t]):
                                self.position = r[t]
                        self.position = self.position+1
                    else:
                        for t in range(8):
                            if(self.position == r[t]):
                                self.position = l[t]
                        self.position = self.position-1 
