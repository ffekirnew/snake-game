from turtle import Turtle

ALIGNMENT = 'Center'
FONT = ('Courier', 24, 'normal')
TITLE = "Super Snake"

class Title(Turtle):
	'''
	Represents a custom text that goes on the top of the screen as title
	'''
	def __init__(self):
		'''
		__init__ - initializes a title object to the top of the screen
		'''
		super().__init__()
		self.color('white')
		self.ht()
		self.penup()
		self.goto(0, 300)
		self.write(TITLE, align=ALIGNMENT, font=FONT)