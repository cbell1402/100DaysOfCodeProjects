from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.current_score}", align=ALIGNMENT, font=FONT)
        #self.current_score += 1

    def update_score(self):
        self.current_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)

