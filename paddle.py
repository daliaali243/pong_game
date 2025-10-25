from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(0,-250)
    def go_right(self):
        new_xcor = self.xcor() + 40
        if new_xcor <350:
          self.goto(new_xcor,self.ycor())
    def go_left(self):
        new_xcor = self.xcor() - 40
        if new_xcor > -350:
          self.goto(new_xcor,self.ycor())