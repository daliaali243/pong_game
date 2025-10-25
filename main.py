from turtle import Screen,Turtle
from paddle import Paddle
from score import Score
from objects import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

falling_shape = Ball()
paddle=Paddle()
score=Score()
screen.listen()
screen.onkey(paddle.go_left,"Left")
screen.onkey(paddle.go_right,"Right")
shape_speed=0.1
game_on=True
while game_on:
    screen.update()
    time.sleep(shape_speed)
    falling_shape.move()
    if falling_shape.distance(paddle)<50 and falling_shape.ycor()<-230:
        shape_type=falling_shape.shape()
        color_shape=falling_shape.color()[0]
        if shape_type=='turtle':
            if color_shape=='white':
                game_on=False
                score.game_over()
            else:
                points=5
                score.increase_score(points)
        elif shape_type=='circle':
            points=1
            score.increase_score(points)
        elif shape_type=='square':
            points=2
            score.increase_score(points)

        elif shape_type=='triangle':
            score.reset_score()
        falling_shape.reset_position()
        shape_speed*=0.9
    if falling_shape.ycor()<-300 :
        falling_shape.reset_position()

screen.exitonclick()

