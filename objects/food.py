from random import choice

from turtle import Turtle
from random import randint, choice

COLORS = ['gainsboro', 'floral white', 'old lace', 'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff', 'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender', 'lavender blush', 'misty rose']

class Food(Turtle):
    def __init__(self) -> None:
        '''
        __init__ - initializes and creates a new food object on the screen
        Return: Nothing.
        '''
        super().__init__()

        self.shape('circle')
        self.penup()
        self.speed('fastest')
        self.random_generate()
        self.onclick(self.here)
    
    def random_generate(self) -> None:
        '''
        random_generate - moves the food to a randomly generated location in the screen, also assignes it a new color
        Return: Nothing.
        '''
        self.clear()
        new_size = randint(4, 7) / 10
        self.shapesize(new_size, new_size)
        self.color(choice(COLORS))
        randomXCor = randint(-280, 280)
        randomYCor = randint(-280, 280)
        self.goto(randomXCor, randomYCor)

    def here(self, x: int, y: int) -> None:
        '''
        here - displays the text 'here' when the food is clicked by a mouse, no functional purpose, jut for fun
        Return: Nothing.
        '''
        self.write(f"Here.", align='Left', font = ('Courier', 10, 'normal'))