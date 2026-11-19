import turtle
from turtle import Turtle, Screen
import random
import winsound
import time

tim=Turtle()
turtle.colormode(255)
screen=Screen()
screen.bgcolor("black")

tim.speed("fastest")
tim.pensize(2)
tim.hideturtle()

def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    color=(r,g,b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(200)
        tim.setheading(tim.heading() + size_of_gap)
        winsound.Beep(random.randint(300, 1000), 70)
        time.sleep(0.01)

draw_spirograph(7)
screen.exitonclick()

