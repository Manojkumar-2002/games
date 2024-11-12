import random
from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.pendown()
        self.write(f"Score: {self.score} ", align="center", font=("Arial", 12, "italic"))

    def refresh(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} ", align="center", font=("Arial", 12, "italic"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Arial", 12, "italic"))



