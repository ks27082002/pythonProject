import turtle
from turtle import Turtle,Screen
import random
turtle.colormode(255)
timmy = Turtle()
timmy.shape("turtle")

# for _ in range(4):
#     timmy.right(90)
#     timmy.forward(100)
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
color = ["white", "peru", "dark magenta", "gold", "green", "red", "wheat"]
direct = [0, 90, 180, 270]
# for i in range(3, 11):
#     angle = 360//i
#     while i:
#         timmy.forward(100)
#         timmy.right(angle)
#         i -= 1

#timmy.pensize(15)
timmy.speed("fastest")
for _ in range(int(360/5)):
    timmy.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    timmy.circle(100)
    timmy.setheading(timmy.heading() + 5)



screen = Screen()
screen.exitonclick()