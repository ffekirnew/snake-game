from turtle import Turtle

STARTING_POSTIONS = [(0, 0), (-10, 0), (-20, 0), (-30, 0), (-40, 0), (-50, 0)]
MOVE_DISTANCE = 10


class Snake:
    def __init__(self):
        self.whole_snake = []
        self.creat_segments()
        self.head = self.whole_snake[0]
    
    def creat_segments(self):
        for position in STARTING_POSTIONS:
            self.add_segment(position)
    
    def add_segment(self, position):
        segment = Turtle(shape='square')
        segment.shapesize(0.5, 0.5)
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.whole_snake.append(segment)
    
    def extend(self):
        self.add_segment(self.whole_snake[-1].position())

    def move(self):
        for segment in range(len(self.whole_snake) - 1, 0, -1):
            new_x = self.whole_snake[segment - 1].xcor()
            new_y = self.whole_snake[segment - 1].ycor()
            self.whole_snake[segment].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def stop(self):
        self.head.forward(0)

    def heading(self):
        return self.head.heading()
    
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    
    def out_of_picture(self):
        if self.head.xcor() >= 295 or self.head.xcor() <= -295 or self.head.ycor() <= -295 or self.head.ycor() >= 295:
            return True
        return False

    def restart(self):
        for segment in self.whole_snake:
            segment.goto(1000, 1000)

        self.whole_snake.clear()
        self.creat_segments()
        self.head = self.whole_snake[0]