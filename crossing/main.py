import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move_up, "Up")
cm = CarManager()
board = Scoreboard()


game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    cm.create_car()
    cm.move_cars()

    if player.ycor() >= 280:
        player.refresh()
        cm.increase_level()
        board.increase_level()
        board.update()

    for car in cm.cars:
        if player.distance(car) < 20:
            game_is_on = False
            board.game_over()

screen.exitonclick()
