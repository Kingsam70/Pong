from turtle import Turtle
PADDLE_COLOR = "green"


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(coordinates)

    # Below to move the paddle up or down
    def up(self):
        if not self.ycor() > 240:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if not self.ycor() < -230:
            self.goto(self.xcor(), self.ycor() - 20)
