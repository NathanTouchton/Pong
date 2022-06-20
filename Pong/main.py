from turtle import Screen
from time import sleep
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)

ball = Ball()

screen.listen()
screen.onkeypress(fun=r_paddle.up, key="Up")
screen.onkeypress(fun=r_paddle.down, key="Down")

screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=l_paddle.down, key="s")

GAME_IS_ON = True
while GAME_IS_ON:
    sleep(ball.move_speed)
    screen.update()
    ball.move()
    ball.reset_ball()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_off_edge()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_off_paddle()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_off_paddle()

screen.exitonclick()
