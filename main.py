from turtle import Screen
from pedal import Pedal
from scoreboard import Score
from balls import Ball
import time

screen = Screen()
screen.title("PING PONG")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Pedal((360, 0))
left_paddle = Pedal((-360, 0))

ball = Ball()

score = Score()
screen.listen()

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")


winning_score = 0
while winning_score < 5:
    is_going = True
    while is_going:
        screen.update()
        time.sleep(0.01)
        right_paddle.block_pedal()
        left_paddle.block_pedal()
        ball.move(right_paddle, left_paddle)
        getting_point = ball.is_out()[0]
        is_going = ball.is_out()[1]
        score.increase_score(getting_point)

    winning_score = score.winner()
    ball.home()
    ball.move_speed = 0.1
    ball.bounce_x()



score.game_over()
screen.exitonclick()
