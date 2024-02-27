from turtle import Turtle
from utils import *


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape("turtle")
        self.color(TURTLE_COLOR)
        self.setheading(90)
        self.penup()
        self.goto(0, PLAYER_INIT_Y)
        self.crossed = False

    def move_down(self):
        if self.ycor() > -SCREEN_HEIGHT/2 + TURTLE_HEIGHT/2:
            self.backward(PIXEL_BLOCK)
        self.sety(max(self.ycor(), -SCREEN_HEIGHT/2 + TURTLE_HEIGHT/2))

    def move_up(self):
        if not self.crossed and self.ycor() >= FINISH_LINE_Y - PIXEL_BLOCK/2:
            self.forward(TURTLE_HEIGHT)
            self.score += 1
            self.crossed = True
        self.sety(min(self.ycor() + PIXEL_BLOCK, FINISH_LINE_Y - PIXEL_BLOCK/2))
