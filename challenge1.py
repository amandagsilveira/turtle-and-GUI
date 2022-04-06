# TODO challenge 1 draw a square
from turtle import Turtle, Screen

tom = Turtle()
tom.shape("turtle")
tom.color("pale violet red")

for n in range(4):
    tom.forward(100)
    tom.right(90)

screen = Screen()
screen.exitonclick()