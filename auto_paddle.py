from turtle import Turtle

class AutoPaddle:
    def __init__(self):
        self.paddle = []

    def create_paddle(self, xcor, ycor):
        for i in range(6):
            paddle_segment = Turtle('square')
            paddle_segment.color('white')
            paddle_segment.speed('fastest')
            paddle_segment.penup()
            self.paddle.append(paddle_segment)
            ycor = ycor
            paddle_segment.goto(xcor, ycor-20*i)

    def move(self, x, y):
        for i in range(len(self.paddle)):
            self.paddle[0].goto(x, y)
            if self.paddle[i] != self.paddle[0]:
                self.paddle[i].goto(x, y-20*i)
