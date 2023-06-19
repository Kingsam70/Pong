# Pong
This is a simple implementation of the classic Pong Game using the Turtle module in Python.

Prerequisites
Python 3.x
Turtle module


Pong Game
This is a simple implementation of the classic Pong Game using the Turtle module in Python.

Prerequisites
Python 3.x
Turtle module
How to Run


Gameplay
Player 1 controls the left paddle with the "W" and "S" keys to move up and down, respectively.
Player 2 controls the right paddle with the Up and Down arrow keys to move up and down, respectively.
The objective of the game is to bounce the ball past the opponent's paddle.
Each time a player successfully hits the ball past the opponent, their score increases.
The game ends when one player reaches the specified number of points to win (default is 10).


Customization
You can customize the number of points required to win by modifying the POINTS_TO_WIN constant in the code.
Additionally, you can adjust the game window's size by modifying the width and height values in the screen.setup() function.
Also you can increase the fps (frame per second) by decreasing self.x_increment/self.y_increment in ball.py but it would hugely impact speed of the ball movement
