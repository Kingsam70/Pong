from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

POINTS_TO_WIN = 10

screen = Screen()
screen.setup(width=700, height=600)
screen.title("My Pong Game")

screen.tracer(0)
screen.listen()

scoreboard1 = ScoreBoard((-162, 260))
paddle1 = Paddle((-325, 0))
ball = Ball()
paddle2 = Paddle((325, 0))
scoreboard2 = ScoreBoard((162, 260))

# Listens to the user commands
screen.onkeypress(key="w", fun=paddle1.up)
screen.onkeypress(key="s", fun=paddle1.down)

screen.onkeypress(key="Up", fun=paddle2.up)
screen.onkeypress(key="Down", fun=paddle2.down)

while True:
    time.sleep(0.03)
    screen.update()

    ball.move()

    # Check the collision of the ball with the wall and make it bounce inverting y-axis
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Check the collision of the ball with the paddles and make it bounce inverting x-axis
    if ball.xcor() > 295 and paddle2.distance(ball) < 60 or ball.xcor() < -295 and paddle1.distance(ball) < 60:
        ball.bounce_x()

    # Check if the player misses the ball
    if ball.xcor() > 320:
        scoreboard1.increase_score()
        ball.refresh()
    elif ball.xcor() < -320:
        scoreboard2.increase_score()
        ball.refresh()

    # Ends the game if someone scored 10 points, you can also change no of points above
    if scoreboard1.score == POINTS_TO_WIN or scoreboard2.score == POINTS_TO_WIN:
        scoreboard1.game_over()
        break

screen.exitonclick()
print("Thanks for playing my Game.")

