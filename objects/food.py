from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.color('cyan')
        self.shape('circle')
        self.penup()
        self.shapesize(0.4, 0.4)
        self.speed('fastest')
        self.random_generate()
        self.onclick(self.here)
    
    def random_generate(self):
        self.clear()
        randomXCor = randint(-280, 280)
        randomYCor = randint(-280, 280)
        self.goto(randomXCor, randomYCor)

    def here(self, x, y):
        self.write(f"Here.", align='Left', font = ('Courier', 10, 'normal'))