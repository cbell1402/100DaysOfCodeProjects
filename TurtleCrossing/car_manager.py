from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        #super().__init__()
        self.all_cars = []

    def create_cars(self):
        #super().__init__()
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.seth(180)
        new_car.move_distance = STARTING_MOVE_DISTANCE
        new_car.color(random.choice(COLORS))
        new_car.goto(300, random.randint(-260, 260))
        self.all_cars.append(new_car)


    def move(self):
        for cars in self.all_cars:
            cars.forward(STARTING_MOVE_DISTANCE)

    def next_level(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

    def next_car(self):
        go_nogo = random.randint(0, 100)
        if go_nogo > 90:
            self.__init__()
