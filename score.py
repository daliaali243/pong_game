from turtle import Turtle

class Score (Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.score = 0
        self.update()
        self.ycor=-10
    def update(self):
        self.clear()
        self.goto(0,260)
        self.write( f'score: {self.score} ',align='center', font=('Arial', 10, 'bold'))
    def increase_score(self,points):
        self.score+=points
        self.update()
    def move(self):
        self.goto(self.xcor(),self.ycor()+self.ycor)
    def reset_score(self):
        self.score=0
        self.update()
    def game_over(self):
        self.goto(0,0)
        self.write('game over',align='center', font=('Arial', 20, 'bold'))

