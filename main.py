import time

from tkinter import *
from turtle import Screen

from objects.food import Food
from objects.snake import Snake
from graphics.outline import Outline
from graphics.scoreboard import ScoreBoard
from graphics.title import Title

screen = Screen()
screen.tracer(0) 
screen.setup(width= 650, height=700)
screen.bgcolor('black')
screen.title('The Snake Game!')

screen.update()

canvas = screen.getcanvas()
button_clicked = False
def button_action():
    global button_clicked
    button_clicked = not button_clicked
    pause_button.config(text = "Continue" if (button_clicked == True) else "Pause")
pause_button = Button(canvas.master, text="Pause", command=button_action)
pause_button.pack()

snake = Snake()
food = Food()
score_board = ScoreBoard(screen.textinput("Player:", "Enter your name here."))
title = Title()
outline = Outline()

screen.listen()
screen.onkey(key='space', fun=button_action)
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)

    #detect collision with the food
    if snake.head.distance(food) < 15:
        food.random_generate()
        score_board.update_score()
        snake.extend()
    
    for segment in snake.whole_snake[1:]:
        if snake.head.distance(segment) < 5:
            score_board.reset()
            snake.restart()

    if snake.out_of_picture():
        score_board.reset()
        snake.restart()

    if button_clicked:
        snake.stop()
        score_board.display_all_scores()
    else:
        snake.move()
        score_board.remove_all_scores()
        
    
screen.exitonclick()
