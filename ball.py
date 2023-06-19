from turtle import Turtle
from random import randint

BALL_COLOR = "black"


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(BALL_COLOR)
        self.penup()
        
        self.x_increment = 5
        self.y_increment = 5


    def move(self):
        """moves ball in a particular diagonal wise direction"""
        x = self.xcor() + self.x_increment
        y = self.ycor() + self.y_increment
        self.goto(x, y)

    def bounce_y(self):
        """inverts y_increment in order to bounce/reverse ball y-axis """
        self.y_increment *= -1

    def bounce_x(self):
        """inverts x_increment in order to bounce/reverse ball x-axis """
        self.x_increment *= -1

    def refresh(self):
        """when the ball goes beyond screen just places the ball back to home and make ball to go in other direction"""
        self.home()
        self.x_increment *= -1
