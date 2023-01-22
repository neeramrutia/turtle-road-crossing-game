from turtle import Turtle
import random
class Car:
    colors=["red","green","blue","cyan","brown"]
    move=5
    moveinc=5
    randomnumber=6
    def __init__(self):
        self.allcars=[]
        
    def createcars(self):
        randomchance=random.randint(1,self.randomnumber)
        if randomchance==1:
            newcar=Turtle("square")
            newcar.shapesize(stretch_len=2,stretch_wid=1)
            newcar.penup()
            newcar.color(random.choice(self.colors))
            randomypos=random.randint(-250,250)
            newcar.goto(300,randomypos)
            self.allcars.append(newcar)

    def movecar(self):
        for i in self.allcars:
            i.backward(self.move)  
    def inclevel(self):
        self.move+=self.moveinc
        self.randomnumber-=1
                 