# TODO 4 Draw a random walk
import turtle
from turtle import Turtle, Screen
import random

tom = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
tom.pensize(15)
tom.speed("fastest")

for n in range(200):
    tom.color(random_color())
    tom.forward(30)
    tom.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
