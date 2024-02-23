import random
from turtle import Turtle
from utils import *


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1, STRETCH_FACTOR)
        self.color(random.choice(CAR_COLORS))
        self.init_x = 0
        self.init_y = 0
        self.setheading(180)
        self.velocity = 0.2


class CarManager:
    def __init__(self, car_move_block):
        self.all_cars = []
        self.last_offset = SCREEN_WIDTH / 4
        # self.moving_cars = []
        self.move_block = car_move_block

    def create_car_bank(self, max_cars):
        while len(self.all_cars) < max_cars:
            car_gap = random.randint(5, 10)
            self.last_offset += car_gap * self.move_block
            next_car = Car()
            next_car.init_x = self.last_offset
            next_car.init_y = random.randint(round(-SCREEN_HEIGHT / 2 + 2 * TURTLE_HEIGHT), round(SCREEN_HEIGHT / 2 - 2
                                                                                                  * TURTLE_HEIGHT))
            next_car.goto(next_car.init_x, next_car.init_y)
            self.all_cars.append(next_car)

    def reset_list(self, car_move_block):
        for car in self.all_cars:
            new_init_y = random.randint(round(-SCREEN_HEIGHT / 2 + 2 * TURTLE_HEIGHT),
                                        round(SCREEN_HEIGHT / 2 - 2 * TURTLE_HEIGHT))
            car.goto(car.init_x, new_init_y)
        self.move_block = car_move_block
