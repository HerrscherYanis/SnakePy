import depend
from Class import Matrice,Button,Snake,Apple,Grass

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
        self.grass.Pri()
        self.snake = Snake(self.matrice,self.up,self.down,self.left,self.right)
        self.snake.Pri()
        self.apple = Apple(self.matrice, self.snake)
    
    def run(self):
        print("Run")
        while True:
            self.snake.Pri()
            print(self.snake.direction)
            self.snake.Eat(self.apple)
            self.snake.Lesn(self.grass)
            self.snake.MovePad()
            self.snake.SnakeMove()
            depend.time.sleep(0.3)
            self.apple.deathpown(self.grass, self.snake)
            if (self.snake.Lose() == True):
                break
            
                          

game = Game(27,26,33,25,32)
game.run()