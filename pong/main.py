from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
screen.listen()


right = Paddle((350, 0))
left = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()


screen.onkey(right.move_up, "Up")
screen.onkey(right.move_down, "Down")
screen.onkey(left.move_up, "w")
screen.onkey(left.move_down, "s")
play = True

while play:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if ball.distance(right) < 50 and ball.xcor() > 320 or ball.distance(left) < 50 and ball.xcor() < -320:
        ball.bounce_x()






screen.exitonclick()