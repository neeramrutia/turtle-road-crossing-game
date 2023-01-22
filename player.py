from turtle import Turtle

class Player(Turtle):
    start=(0,-280)
    end=(0,280)
    moveincr=10
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(self.start)
        self.setheading(90)
    def move(self):
        self.forward(self.moveincr)
    def moveback(self):
        self.backward(self.moveincr)   

    def isatfinishline(self):
        if self.ycor()>=280:
            return True
        else: return False  
    def gotostartingline(self):
        self.goto(self.start)               