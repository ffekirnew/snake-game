from turtle import Turtle
from heapq import *
import json

ALIGNMENT = 'Center'
FONT = ('Courier', 16, 'normal')
		
class Board(Turtle):
	'''
	Board: a class that will represent the boards (title and score)
	'''
	def __init__(self):
		super().__init__()
		self.color('white')
		self.ht()
		self.penup()
		self.goto(0, -330)

class ScoreBoard:
	'''
	ScoreBoard: 
	'''
	def __init__(self, player: str) -> None:
		'''
		__init__ - initializes the scoreboard
		@player: the name of the player currently playing
		'''
		self.player = player
		with open("data.json") as file:
			self.data_base = json.load(open("data.json"))['scores']
		file.close()

		self.score_value = 0
		self.high_score_value = -self.data_base[0][0]
		self.turtles = [Board(), Board(), Board()]
		distance = 600 // len(self.turtles)
		self.score, self.high_score, self.player_name = self.turtles
		self.scores_table = Board()
		self.score.goto(-distance, self.score.ycor())
		self.player_name.goto(distance, self.player_name.ycor())
		self.clicked = False
		# self.player_name.showturtle()
		self.player_name.onclick(self.button_clicked)
		self.display()
	
	def display(self) -> None:
		'''
		display - displays the entire score board on the screen
		Return: Nothing.
		'''
		self.clear()
		self.score.write(f"Score: {self.score_value}", align=ALIGNMENT, font=FONT)
		self.high_score.write(f"Highscore: {self.high_score_value}", align=ALIGNMENT, font=FONT)
		self.player_name.write(f"{self.player}", align=ALIGNMENT, font=FONT)
	
	def reset(self) -> None:
		'''
		reset - resets the scoreboard to 0 and saves the new data, if any change
		Return: Nothing.
		'''
		self.score_value = 0
		if self.high_score_value > self.data_base[0][0]:
			heappush(self.data_base, [-self.high_score_value, self.player])
		self.high_score_value = -self.data_base[0][0]

		with open("data.json", mode="w") as file:
			json.dump({"scores": self.data_base}, file)
		file.close()

		self.display()
	
	def update_score(self) -> None:
		'''
		update_score - updates the running score and the highscore
		Return: Nothing.
		'''
		self.score_value += 1
		self.high_score_value = max(self.score_value, self.high_score_value)
		self.clear()
		self.display()

	def clear(self) -> None:
		'''
		clear - clears all the boards on the screen
		Return: Nothing.
		'''
		for turtle in self.turtles:
			turtle.clear()

	def button_clicked(self, x: int = 0, y: int = 0) -> None:
		'''
		button_clicked - sets the status of the variable clicked
		@x: the x coordinate of the turtle sent by the caller
		@y: the y coordinate of the turtle sent by the caller
		Return: Nothing.
		'''
		self.clicked = not self.clicked

	def is_clicked(self) -> None:
		'''
		is_clicked - returns the status of the button controlled to be clicked
		Return: Nothing.
		'''
		return self.clicked

	def display_high_scores(self) -> None:
		'''
		display_high_scores - displays the previous best scores by fetching them from the database
		Remove: Nothing.
		'''
		self.scores_table.goto(0, 200)
		self.scores_table.write(f"All Time Best Scores\n\n", align=ALIGNMENT, font=FONT)
		scores = self.data_base[:]
		heappush(scores, [-self.score_value, "> " + self.player])
		for i in range(min(10, len(scores))):
			score = heappop(scores)
			self.scores_table.write(f"{score[1]}: {-score[0]}", align=ALIGNMENT, font=FONT)
			self.scores_table.goto(self.scores_table.xcor(), self.scores_table.ycor() - FONT[1] - 4)

	def remove_high_scores(self) -> None:
		'''
		remove_high_scores - removes all the scores printed on the screen
		Return: None
		'''
		self.scores_table.clear()