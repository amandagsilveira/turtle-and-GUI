# TODO challenge 3 drawing a different shapes
from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape("turtle")
tim.color("pale violet red")

colours = ["medium spring green", "gold", "firebrick", "light coral", "purple", "dark slate blue", "chartreuse", "gray"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for n in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side)

screen = Screen()
screen.exitonclick()
