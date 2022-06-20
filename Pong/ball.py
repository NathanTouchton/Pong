from turtle import Turtle
from scoreboard import Scoreboard

scoreboard = Scoreboard()

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        scoreboard.update_score()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_off_edge(self):
        self.y_move *= -1

    def bounce_off_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        if self.xcor() > 350:
            scoreboard.l_point()
            self.x_move = -10
            self.goto(0, 0)
            self.move_speed = 0.1

        if self.xcor() < -350:
            scoreboard.r_point()
            self.x_move = 10
            self.goto(0, 0)
            self.move_speed = 0.1
