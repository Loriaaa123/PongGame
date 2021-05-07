from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    elif ball.xcor() > 325 and ball.distance(r_paddle) < 50 or ball.xcor() < -325 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
    elif ball.xcor() > 360:
        scoreboard.l_point()
        ball.ball_reset()
    elif ball.xcor() < -360:
        scoreboard.r_point()
        ball.ball_reset()
    elif scoreboard.l_score == 2:
        scoreboard.goto(0, 0)
        scoreboard.color("red")
        scoreboard.write("Left Player Wins", align="center", font=("Courier", 50, "bold"))
        game_is_on = False
    elif scoreboard.r_score == 2:
        scoreboard.goto(0, 0)
        scoreboard.color("red")
        scoreboard.write("Right Player Wins", align="center", font=("Courier", 50, "bold"))
        game_is_on = False

screen.exitonclick()
