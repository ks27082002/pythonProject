from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-160, 240)
        self.level = 1
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(arg=f"level is {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1

    def game_over(self):

        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)

