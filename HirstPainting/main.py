import random
import colorgram
import turtle

def x_side():
    for x in range(0, 10):
        timmy.pencolor(random.choice(color_list))
        timmy.dot(20)
        timmy.forward(50)


colors = colorgram.extract('image.jpg', 21)
color_list = []
for i in range(1,21):
    color_list.append((colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b))

print(color_list)


timmy = turtle.Turtle()
timmy.penup()
timmy.hideturtle()
timmy.speed(0)
turtle.colormode(255)
timmy.pensize(10)
#10x10, size 20, space 50

for i in range(-250, 250, 50):
    timmy.goto(-250, i)
    x_side()


screen = turtle.Screen()
screen.exitonclick()
