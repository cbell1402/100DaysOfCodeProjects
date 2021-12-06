from turtle import Turtle


class NameWriter(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state(self, position, state):
        self.goto(position)
        self.write(state)

    def game_over(self):
        self.goto(0, 0)
        self.write("Great job!", font=("Arial", 52, "bold"))
