import turtle as t
import random

'''----Início do código para pegar as cores da imagem----'''
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('floral.png', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
'''----Fim do código para pegar as cores da imagem----'''

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(219, 152, 93), (113, 169, 195), (242, 210, 79), (187, 206, 232), (246, 233, 177), (223, 62, 126),
(56, 107, 164), (148, 91, 50), (203, 131, 167), (192, 152, 44), (192, 228, 203), (239, 160, 187), (229, 71, 56),
(140, 185, 143), (19, 176, 105), (168, 188, 227), (19, 169, 218), (241, 193, 213), (101, 111, 176), (188, 46, 118),
(13, 3, 1), (166, 213, 154), (240, 162, 155), (38, 144, 94), (132, 35, 23), (47, 46, 150), (207, 9, 110),
(250, 215, 2), (138, 211, 228), (84, 18, 37)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()

