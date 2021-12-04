import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
turtle = Player()
car = CarManager()

tracker = 0

screen.listen()
screen.onkey(fun=turtle.move, key="Up")
screen.onkey(fun=turtle.move, key="w")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    tracker += 1
    car.move()

    if tracker == 10:
        car.create_cars()
        tracker = 0

    # Detect Level Win
    if turtle.ycor() > turtle.finish:
        turtle.reset()
        scoreboard.update_level()
        car.next_level()

    for cars in car.all_cars:
        if turtle.distance(cars) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
