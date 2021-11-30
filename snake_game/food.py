from turtle import Turtle
import random

NEGATIVE_COORD = -280
POSITIVE_COORD = 280


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(NEGATIVE_COORD, POSITIVE_COORD)
        random_y = random.randint(NEGATIVE_COORD, POSITIVE_COORD)
        self.goto(random_x, random_y)