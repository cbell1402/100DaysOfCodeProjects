from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("High_Score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.current_score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.current_score += 1
        self.update_scoreboard()

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("High_Score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.current_score = 0
        self.update_scoreboard()

