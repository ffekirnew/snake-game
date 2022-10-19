from turtle import Turtle

ALIGNMENT = 'Center'
FONT = ('Courier', 24, 'normal')

class Title(Turtle):
	def __init__(self):
		super().__init__()
		self.color('white')
		self.ht()
		self.penup()
		self.goto(0, 300)
		self.write(f"Snake: Still Fun", align=ALIGNMENT, font=FONT)