# TODO challenge 2 draw a dashed line
from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")
timmy.color("pale violet red")

for n in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen = Screen()
screen.exitonclick()