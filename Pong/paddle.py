from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.speed(0)
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(x=350, y=0)

    # def up(self):


    # def down(self):


    # def left(self):

    
    # def right(self):


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
paddle = Paddle()

screen.exitonclick()

