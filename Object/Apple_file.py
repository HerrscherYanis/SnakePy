import depend

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
        self.position = 0
        self.AppleRan(snake)    
    def AppleRan(self, snake):
        if(self.quality == None):
            get_proprety = depend.random.choice(list(self.data.items()))
        else:
            get_proprety = [self.quality,self.data[self.quality]]
        self.quality = get_proprety[0]
        self.color = get_proprety[1]["color"]
        self.score = get_proprety[1]["score"]
        self.size = get_proprety[1]["size"]
        apple_position = depend.random.randint(0, self.Matrice.mapsint-1)
        rule = False
        self.quality = None
        for position in snake.position :
            if(apple_position == position):
                rule = True
        if(rule == True):
            self.AppleRan(snake)
        else:
            self.position = apple_position
            self.Matrice.Pri(self)
    def deathpown(self,grass,sn):
        self.timer = self.timer+1
        if(self.timer>20 and self.timer < 30):
            self.Matrice.Pri(self)
            depend.time.sleep(0.1)
            self.Matrice.Pri(self, (0, 1, 0))
        elif(self.timer>30):
            self.timer = 0
            self.AppleRan(sn)
            self.Matrice.Pri(self)
    def Pri(self):
        self.Matrice.Pri(self)      