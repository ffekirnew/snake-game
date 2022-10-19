from turtle import Turtle
from heapq import *
import json

ALIGNMENT = 'Center'
FONT = ('Courier', 16, 'normal')

class Board(Turtle):
	def __init__(self):
		super().__init__()
		self.color('white')
		self.ht()
		self.penup()
		self.goto(0, -330)

class ScoreBoard:
	def __init__(self, player: str):
		self.player = player
		with open("data.json") as file:
			self.high_score_value = json.load(open("data.json"))['scores']
		file.close()

		self.score_value = 0
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
	
	def display(self):
		self.clear()
		self.score.write(f"Score: {self.score_value}", align=ALIGNMENT, font=FONT)
		self.high_score.write(f"Highscore: {-self.high_score_value[0][0]}", align=ALIGNMENT, font=FONT)
		self.player_name.write(f"{self.player}", align=ALIGNMENT, font=FONT)
	
	def reset(self):
		self.score_value = 0
		with open("data.json", mode="w") as file:
			json.dump({"scores": self.high_score_value}, file)
		file.close()

		self.display()
	
	def update_score(self):
		self.score_value += 1
		if -self.score_value < self.high_score_value[0][0]:
			heappush(self.high_score_value, [-self.score_value, self.player])
		self.clear()
		self.display()

	def clear(self):
		for turtle in self.turtles:
			turtle.clear()

	def button_clicked(self, x, y):
		self.clicked = not self.clicked

	def is_clicked(self):
		return self.clicked

	def display_all_scores(self):
		self.scores_table.goto(0, 200)
		self.scores_table.write(f"All Time Best Scores\n\nName\tScore\n", align=ALIGNMENT, font=FONT)
		scores = self.high_score_value[:]
		for i in range(min(10, len(scores))):
			score = heappop(scores)
			self.scores_table.write(f"{score[1]}\t{-score[0]}", align=ALIGNMENT, font=FONT)
			self.scores_table.goto(self.scores_table.xcor(), self.scores_table.ycor() - FONT[1] - 4)

	def remove_all_scores(self):
		self.scores_table.clear()