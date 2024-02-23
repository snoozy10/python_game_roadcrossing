import time
from turtle import Screen
from player import Player
from scoreboard import ScoreBoard
from carmanager import CarManager
from utils import *

screen = Screen()


def exit_screen(x, y):
    print(f"clicked at ({x}, {y})")
    screen.isExit = True


def next_level():
    car_factory.reset_list(CAR_MOVE_BLOCK + player.score * CAR_SPEED)
    player.goto(0, PLAYER_INIT_Y)
    player.crossed = False
    scoreboard.rewrite()


screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.bgcolor(BG_COLOR)
screen.title("Cross the Road!")
screen.tracer(0)
screen.isExit = False
screen.onclick(exit_screen)


player = Player()
car_factory = CarManager(CAR_MOVE_BLOCK + player.score * CAR_SPEED)
scoreboard = ScoreBoard(player)
screen.onkeypress(key="Up", fun=player.move_up)
screen.onkeypress(key="Down", fun=player.move_down)
screen.listen()
car_gap = 0
car_factory.create_car_bank(15)

while not screen.isExit:
    time.sleep(SLEEP_TIME)
    if player.crossed:
        next_level()

    for car in car_factory.all_cars:
        car.forward(car_factory.move_block)
        if car.xcor() < -SCREEN_WIDTH / 2 - 4 * PIXEL_BLOCK:
            car_factory.all_cars.remove(car)
            car.goto(car.init_x + SCREEN_WIDTH/4, car.init_y)
            car_factory.all_cars.append(car)
        if player.distance(car) < CAR_WIDTH/2:
            screen.isExit = True
            print("<PTCHT> x.x")
    screen.update()

print(len(car_factory.all_cars))
screen.exitonclick()
