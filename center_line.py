from turtle import Turtle


class Line:
    def __init__(self):
        self.line = []

    def create_line(self, h):
        block_size = h/7 - h/9
        for i in range(round(block_size)):
            element = Turtle()
            element.color('white')
            element.shape('square')
            element.penup()
            self.line.append(element)
            element.turtlesize(1.5, 0.5)
            self.line[0].goto(x=0, y=-340)
            y_pos = -340
            if self.line[i] != self.line[0]:
                self.line[i].goto(0, y_pos + i*50)
