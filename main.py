import time

from tkinter import *
from turtle import Screen

from objects.food import Food
from objects.snake import Snake
from graphics.outline import Outline
from graphics.scoreboard import ScoreBoard
from graphics.title import Title


'''
initialize the screen
'''
screen = Screen()
screen.tracer(0) 
screen.setup(width= 650, height=700)
screen.bgcolor('black')
screen.title('Super Snake')

'''
initialize and create game objects, start playing
'''
title = Title()
outline = Outline()
snake = Snake()
food = Food()
screen.update()
score_board = ScoreBoard(screen.textinput("Player:", "Enter your name here."))

'''
command the screen to listen and set some keys for it to listen to
'''
screen.listen()
screen.onkey(key='space', fun=score_board.button_clicked)
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

    if score_board.is_clicked():
        snake.stop()
        score_board.display_high_scores()
    else:
        snake.move()
        score_board.remove_high_scores()
        
    
screen.exitonclick()
