from turtle import Turtle, Screen
from paddle import Paddle
from score import Score
from center_line import Line
from ball import Ball
import time

from auto_paddle import AutoPaddle

screen = Screen()
screen.bgcolor('black')
screen.setup(1300, 800)
screen.listen()

screen.tracer(0)
paddle1 = Paddle(600, 150)
auto_paddle = Paddle(-600, 150)
score1 = Score(250, 320)
score2 = Score(xcor=-250, ycor=320)
score_board1 = 0
score_board2 = 0
score1.draw(score_board1)
score2.draw(score_board2)
line = Line()
line.create_line(620)
ball = Ball()

screen.update()


def down():
    paddle1.down()
    screen.update()
    # time.sleep(0.1)
def down1():
    auto_paddle.down()
    screen.update()

def up():
    paddle1.up()
    screen.update()

def up1():
    auto_paddle.up()
    screen.update()
    # time.sleep(0.01)


screen.onkeypress(key='Down', fun=down)
screen.onkeypress(key='Up', fun=up)
screen.onkeypress(key='s', fun=down1)
screen.onkeypress(key='w', fun=up1)
game = True
while game:
    time.sleep(0.02)
    ball.move()
    screen.update()
    if ball.ball.distance(paddle1) < 55 and ball.ball.xcor() > 550:
        ball.paddle_bounce()
    elif ball.ball.distance(auto_paddle) < 55 and ball.ball.xcor() < -380:
        ball.paddle_bounce()
        
    if ball.ball.xcor() > 610:
        score_board2 +=1
        score2.clear()
        score2.draw(score_board2)
        ball.ball.home()
        screen.update()
        time.sleep(3)
    elif ball.ball.xcor() <-610:
        score_board1 += 1
        score1.clear()
        score1.draw(score_board1)
        ball.ball.home()
        screen.update()
        time.sleep(3)


# while True:
#     for i in range(len(paddle1.paddle)):
#         if ball.ball.distance(paddle1.paddle[i]) < 45 and ball.ball.xcor() > 380:
#             ball.paddle_bounce()
#         elif ball.ball.distance(auto_paddle.paddle[i]) < 45 and ball.ball.xcor() < -380:
#             ball.paddle_bounce()






# while True:
#     auto_paddle.move(x_cor, y_cor)
#     screen.update()




screen.exitonclick()
