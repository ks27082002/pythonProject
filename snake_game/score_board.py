from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.count = 0
        self.speed("fastest")
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.write(arg=f"score is {self.count}, High Score is {self.high_score}", align=ALIGNMENT, font=FONT)


    def refresh(self):

        self.clear()
        self.write(arg=f"score is {self.count}, High Score is {self.high_score}", align=ALIGNMENT, font=FONT)

    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self) :
        if self.count > self.high_score:
            self.high_score = self.count
            with open("data.txt", mode='w') as file:
                file.write(f"{self.high_score}")

        self.count = 0
        self.refresh()

    def increase_score(self):
        self.count += 1
        self.refresh()

