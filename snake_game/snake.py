from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.body_parts = []
        self.create_snake()
        self.head = self.body_parts[0]

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_body_part(position)


    def add_body_part(self, position):
        snake_body = Turtle("square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.body_parts.append(snake_body)

    def extend(self):
        self.add_body_part(self.body_parts[-1].position())


    def move(self):
        for parts in range(len(self.body_parts) - 1, 0, -1):
            new_x = self.body_parts[parts - 1].xcor()
            new_y = self.body_parts[parts - 1].ycor()
            self.body_parts[parts].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)
