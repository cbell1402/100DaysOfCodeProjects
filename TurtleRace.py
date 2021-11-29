import random
import turtle

def who_won(winning_turtle):
    if winning_turtle == user_bet:
        print("You won!")
    else:
        print(f"The {winning_turtle} turtle won the race. You lose.")

screen = turtle.Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bets!", prompt="Please select a color:").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = ["tim", "tom", "bill", "gill", "jill", "ed"]


y_pos = -100
for i in range(6):
    turtles[i] = turtle.Turtle(shape="turtle")
    turtles[i].color(colors[i])
    turtles[i].penup()
    y_pos += 30
    turtles[i].goto(x=-250, y=y_pos)

on = True
while on:
    for i in range(6):
        rand_distance = random.randint(0, 10)
        turtles[i].forward(rand_distance)
        if turtles[i].xcor() > 230:
            on = False
            winner = turtles[i].pencolor()
            who_won(winner)

screen.exitonclick()
