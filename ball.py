from turtle import Turtle
from paddle import Paddle

class Ball:

    def __init__(self):

        self.ball = Turtle('circle')
        self.ball.color('white')
        self.ball.goto(0, 0)
        self.ball.speed(1)
        self.ball.penup()
        self.x_move = 10
        self.y_move = 10

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.ball.speed(0)

    def move(self):

        if self.ball.ycor() > 380 or self.ball.ycor() < -380:
            self.bounce()
        ycor = self.ball.ycor() + self.y_move
        xcor = self.ball.xcor() + self.x_move
        self.ball.goto(xcor, ycor)

    def y_cor(self):
        y_cor = self.ball.ycor()
        return y_cor



