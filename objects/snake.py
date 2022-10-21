from turtle import Turtle

STARTING_POSTIONS = [(0, 0), (-10, 0), (-20, 0), (-30, 0), (-40, 0), (-50, 0)]
MOVE_DISTANCE = 10


class Snake:
    def __init__(self) -> None:
        '''
        __init__ - initializes a snake of three segments
        Return: Nothing.
        '''
        self.whole_snake = []
        self.create_segments()
        self.head = self.whole_snake[0]
    
    def create_segments(self) -> None:
        '''
        create_segments - creates segments for the ammoung required and adds them to the snake
        Return: Nothing.
        '''
        for position in STARTING_POSTIONS:
            self.add_segment(position)
    
    def extend(self) -> None:
        '''
        extend - extends the snake by one segment
        Return: Nothing.
        '''
        self.add_segment(self.whole_snake[-1].position())

    def add_segment(self, position: list[int]) -> None:
        '''
        add_segment - adds a segment to the given posiotion
        @position: the [x, y] coordinate of the position we want the new segment to be added
        Return: Nothing.
        '''
        segment = Turtle(shape='square')
        segment.shapesize(0.5, 0.5)
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.whole_snake.append(segment)

    def move(self) -> None:
        '''
        move - moves the snake in the direction that it was moving in
        Return: Nothing.
        '''
        for segment in range(len(self.whole_snake) - 1, 0, -1):
            new_x = self.whole_snake[segment - 1].xcor()
            new_y = self.whole_snake[segment - 1].ycor()
            self.whole_snake[segment].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def stop(self) -> None:
        '''
        stop - stops the snake from moving
        Return: Nothing.
        '''
        self.head.forward(0)

    def heading(self) -> int:
        '''
        heading - returns the direction the snake is facing (in degrees (0 - 360))
        Return: int
        '''
        return self.head.heading()
    
    def up(self) -> None:
        '''
        up - changes the direction of the snake to face up
        Return: Nothing.
        '''
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self) -> None:
        '''
        down - changes the direction of the snake to face down
        Return: Nothing.
        '''
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self) -> None:
        '''
        right - changes the direction of the snake to face right
        Return: Nothing.
        '''
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self) -> None:
        '''
        left - changes the direction of the snake to face left
        Return: Nothing.
        '''
        if self.head.heading() != 0:
            self.head.setheading(180)

    
    def out_of_picture(self) -> bool:
        '''
        out_of_picture - returnes if the snake has hit a wall and moved out of picture
        Return: bool
        '''
        if self.head.xcor() >= 295 or self.head.xcor() <= -295 or self.head.ycor() <= -295 or self.head.ycor() >= 295:
            return True
        return False

    def restart(self) -> None:
        '''
        restart - resets every thing to the default values and restarts the game
        Return: None
        '''
        for segment in self.whole_snake:
            segment.goto(1000, 1000)

        self.whole_snake.clear()
        self.create_segments()
        self.head = self.whole_snake[0]