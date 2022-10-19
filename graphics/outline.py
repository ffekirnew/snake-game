from turtle import Turtle

ALIGNMENT = 'Center'
FONT = ('Courier', 20, 'normal')

class Outline(Turtle):
	def __init__(self):
		super().__init__()
		self.color('white')
		self.ht()
		self.penup()
		self.goto(-298, 298)
		self.pendown()
		self.goto(298, 298)
		self.goto(298, -298)
		self.goto(-298, -298)
		self.goto(-298, 298)