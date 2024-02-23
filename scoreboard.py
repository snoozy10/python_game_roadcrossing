from turtle import Turtle
from utils import *


class ScoreBoard(Turtle):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.rewrite()

    def rewrite(self):
        self.reset()
        self.hideturtle()
        self.penup()
        self.pencolor(SCORE_COLOR)
        self.goto(x=SCREEN_WIDTH / 2 - FONT_SIZE, y=SCREEN_HEIGHT / 2 - 2 * FONT_SIZE)
        self.write(f"Score: {self.player.score}", font=("Times New Roman", FONT_SIZE, "normal"), align="right")

    def game_over(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.pencolor(SCORE_COLOR)
        self.goto(0, 0 + FONT_SIZE/2 + PIXEL_BLOCK/4)
        self.write("Game Over x.x", font=("Times New Roman", FONT_SIZE, "normal"), align="center")
        self.goto(0, 0 - FONT_SIZE/2 - PIXEL_BLOCK/4)
        self.write(f"Final score: {self.player.score}", font=("Times New Roman", FONT_SIZE, "normal"), align="center")
