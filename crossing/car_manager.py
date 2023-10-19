from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.level = 0

    def create_car(self):
        if random.randint(1, 5) == 4:
            new_pos = (280, random.randint(-240, 240))
            new_car = Turtle()

            new_car.setheading(180)
            new_car.penup()

            self.cars.append(new_car)
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=random.randint(1, 3))
            new_car.color(random.choice(COLORS))
            new_car.speed(random.choice(["slowest", "slow", "fast", "fastest"]))
            new_car.goto(new_pos)

    def move_cars(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT + self.level*STARTING_MOVE_DISTANCE)

    def increase_level(self):
        self.level += 1

