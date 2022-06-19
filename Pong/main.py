from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")

p1_paddle = Paddle()

screen.listen()
screen.onkey(fun=p1_paddle.up, key="Up")
screen.onkey(fun=p1_paddle.down, key="Down")

screen.exitonclick()
