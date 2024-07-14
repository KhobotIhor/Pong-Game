from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.turtlesize(6, 1)
        self.goto(xcor, ycor)

    def down(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto(x_cor, y_cor - 50)


    def up(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto(x_cor, y_cor + 50)














