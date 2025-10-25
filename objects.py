from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shapes=['turtle','square','circle','star','triangle']
        self.colors=['white','red','green']
        self.y_move=-10
        self.penup()
        self.reset_position()
    def reset_position(self):
        self.goto(random.randint(-380,380),250)
        random_shape=random.choice(self.shapes)
        self.shape(random_shape)
        if random_shape == 'turtle' and random.randint(1,10):
            self.color('white')
        else:
            self.color(random.choice(self.colors))
        random_size=random.uniform(1,2)
        self.shapesize(random_size,random_size)
    def move(self):
        self.goto(self.xcor(),self.ycor()+self.y_move)


