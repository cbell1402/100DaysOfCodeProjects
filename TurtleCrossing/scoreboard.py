from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=-280, y=260)
        self.hideturtle()
        self.level = 0
        self.update_level()

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(-75, 0)
        self.write(arg="Game Over", font=FONT)

