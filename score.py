from turtle import Turtle

FONT = ('Arial', 40, 'normal')

class Score:
    def __init__(self, xcor, ycor):
        self.scoreboard = Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.pencolor('white')
        self.scoreboard.penup()
        self.scoreboard.goto(x=xcor, y=ycor)
        self.scoreboard.pendown()


    def draw(self, score):
        self.scoreboard.write(score, False, 'Right', FONT)

    def clear(self):
        self.scoreboard.clear()
