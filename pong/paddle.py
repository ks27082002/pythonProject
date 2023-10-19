from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(x=position[0], y=position[1])
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)


    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
