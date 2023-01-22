from turtle import Turtle
FONT=("Arial",20,"normal")
class Score(Turtle):
    level=1
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-260,260)
        self.updatescore()
        

    def updatescore(self):
        self.clear()
        self.write(f"LEVEL: {self.level}",align="left",font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)    