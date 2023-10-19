from turtle import Turtle, Screen
import  random

screen = Screen()
screen.setup(height= 400, width= 500)
choice = screen.textinput(title="Make your bet", prompt="Which turtle will the race? Enter a color: ")
play = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_cord = [-70, -40, -10, 20, 50, 80]
turtles = []

if choice:
    play = True

for i in range(6):
    newtut = Turtle(shape="turtle")
    newtut.color(colors[i])
    newtut.penup()
    newtut.goto(x=-230, y=y_cord[i])
    turtles.append(newtut)

while play:

    for tut in turtles:
        if tut.xcor() > 230:

            play = False
            winner = tut.pencolor()
            if winner == choice:
                print(f"You've won. {winner} turtle wins")
            else:
                print(f"You've lost. {winner} turtle wins")

        dist = random.randint(0, 6)
        tut.forward(dist)

screen.exitonclick()

