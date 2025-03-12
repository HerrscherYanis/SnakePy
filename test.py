from Apple_file import Apple
from Grass_file import Grass
from Snake_file import Snake
from Component_file import Matrice, Button
import depend

mtest = Matrice(27)
up = Button(26)
down = Button(32)
left = Button(25)
right = Button(33)

snake = Snake(mtest, up, down, left, right)
snake.Pri()

#while True:
    #depend.time.sleep(1)
print(snake.position)
print(snake.direction)
    #snake.Move()
snake.Pri()
    