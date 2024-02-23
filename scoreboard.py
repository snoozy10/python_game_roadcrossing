from turtle import Turtle
from utils import *


class ScoreBoard(Turtle):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.rewrite()
        # self.hideturtle()
        # self.penup()
        #
        # self.pencolor(SCORE_COLOR)
        # self.goto(x=SCREEN_WIDTH / 2 - FONT_SIZE, y=SCREEN_HEIGHT / 2 - 2 * FONT_SIZE)
        # self.write(f"Score: {player.score}", font=("Times New Roman", FONT_SIZE, "normal"), align="right")

    def rewrite(self):
        self.reset()
        self.hideturtle()
        self.penup()
        self.pencolor(SCORE_COLOR)
        self.goto(x=SCREEN_WIDTH / 2 - FONT_SIZE, y=SCREEN_HEIGHT / 2 - 2 * FONT_SIZE)
        self.write(f"Score: {self.player.score}", font=("Times New Roman", FONT_SIZE, "normal"), align="right")