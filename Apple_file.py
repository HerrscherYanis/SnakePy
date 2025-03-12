import depend
from Component_file import Printing

class Apple(Printing):
    def __init__(self, Matrice):
        super().__init__(Matrice)
        self.quality = "ordinary"
        self.number = 1
        self.color = None
        self.score = 0
        self.size = 0
        self.timer = 0
        self.data = depend.json.load(open('proprety.json'))   
        self.position = 0
        
    def Random(self):
        if(self.quality == None):
            get_proprety = depend.random.choice(list(self.data.items()))
        else:
            get_proprety = [self.quality,self.data[self.quality]]
        self.quality = get_proprety[0]
        self.color = get_proprety[1]["color"]
        self.score = get_proprety[1]["score"]
        self.size = get_proprety[1]["size"]
        apple_position = depend.random.randint(0, self.Matrice.mapsint-1)
        self.position = apple_position
        
    def Safe(self, snake):
        rule = False
        for position in snake.position :
            if(self.position == position):
                rule = True
        if(rule == True):
            self.Random()
        else:
            self.quality = None
        
    def deathpown(self,grass):
        self.timer = self.timer+1
        if(self.timer>20 and self.timer < 30):
            self.Matrice.Pri(self)
            depend.time.sleep(0.1)
            self.Matrice.Pri(self, (0, 1, 0))
        elif(self.timer>30):
            self.timer = 0
            self.Random()
            self.Matrice.Pri(self)   