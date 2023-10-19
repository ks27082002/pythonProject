# import colorgram
# colors = colorgram.extract("img.jpg", 30)
# print(colors)
# rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb.append((r, g, b))
# print(rgb)
import turtle, random
from turtle import Turtle, Screen
turtle.colormode(255)
colors = [(205, 156, 99), (106, 107, 126), (141, 141, 151), (177, 66, 39), (224, 211, 113), (235, 217, 225), (203, 150, 175), (105, 112, 167), (171, 154, 53), (37, 40, 23), (29, 29, 63), (181, 23, 10), (31, 42, 27), (226, 231, 226), (223, 170, 196), (206, 88, 63), (46, 48, 99), (232, 174, 162), (115, 99, 106), (184, 185, 210), (83, 91, 82), (68, 69, 45), (155, 160, 155), (189, 93, 107), (43, 30, 42), (58, 69, 55), (97, 49, 61), (188, 195, 187)]
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(400)
tim.setheading(0)

for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(colors))
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen = Screen()
screen.exitonclick()
