from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.score = 0

        self.hideturtle()
        self.penup()
        self.goto(coordinates)
        self.write(f"Score: {self.score}", move=False, align='left', font=('Arial', 12, 'normal'))

    def increase_score(self):
        """increase the score of other player when ball goes out of bound"""
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align='left', font=('Arial', 12, 'normal'))

    def game_over(self):
        """prints game over on the screen"""
        self.goto(-80, 0)
        self.write(f"GAME OVER", move=False, align='left', font=('Arial', 21, 'normal'))