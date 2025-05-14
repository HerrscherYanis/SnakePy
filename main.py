import depend
from Component_file import Matrice,Button
from Grass_file import Grass
from Snake_file import Snake
from Apple_file import Apple

class Game:
    def __init__(self, pin_matrice, pin_up, pin_down, pin_left, pin_right):
        #Def Material
        self.matrice = Matrice(pin_matrice)
        self.up = Button(pin_up)
        self.down = Button(pin_down)
        self.left = Button(pin_left)
        self.right = Button(pin_right)
        #Def Game
        self.grass = Grass(self.matrice)
        self.snake = Snake(self.matrice,self.up,self.down,self.left,self.right)
        self.apple = Apple(self.matrice, self.snake)
        self.Islevel = 0
    
    def run(self):
        print("Run")
        while True:
            self.level()
            self.snake.Pri(self.grass.color)
            self.snake.Eat(self.apple)
            self.snake.MovePad()
            self.snake.SnakeMove()
            depend.time.sleep(0.3)
            self.apple.deathpown(self.grass, self.snake)
            #print(self.snake.score)
            if (self.snake.Lose() == True):
                self.GameOver()
                break
            
    def GameOver(self):
        self.grass.Pri((0, 1, 0))
        depend.time.sleep(1)
        self.grass.Pri((1, 1, 0))
        
    def AnimaOver(self):
        pass
    
    def level(self):
        if (self.snake.score <= 1000 and self.Islevel == 0):
            self.grass.color = (0, 1, 0)
            self.grass.Pri()
            self.apple.Pri()
            self.Islevel = 1
        if (self.snake.score >= 1000 and self.snake.score <= 2000 and self.Islevel == 1):
            self.grass.color = (1, 1, 0)
            self.grass.Pri()
            self.apple.Pri()
            self.Islevel = 2
        if (self.snake.score >= 2000 and self.snake.score <= 4000 and self.Islevel == 2):
            self.grass.color = (3, 2, 0)
            self.grass.Pri()
            self.apple.Pri()
            self.Islevel = 3
        if (self.snake.score >= 4000 and self.snake.score <= 8000 and self.Islevel == 3):
            self.grass.color = (0, 1, 1)
            self.grass.Pri()
            self.apple.Pri()
            self.Islevel = 4
            
                          

game = Game(27,26,33,25,32)
game.run()