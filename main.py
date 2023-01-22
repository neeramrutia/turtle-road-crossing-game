from turtle import Screen
import time
from player import Player
from score import Score
from car import Car

screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

player=Player()
car=Car()
score=Score()


screen.listen()
screen.onkey(player.move,"Up")
screen.onkey(player.moveback,"Down")


gameison=True
while gameison:
    time.sleep(.1)    
    screen.update()

    car.createcars()
    car.movecar()
    if player.isatfinishline():
        player.gotostartingline()
        car.inclevel()
        score.level+=1
        score.updatescore()
    for i in car.allcars:
        if player.distance(i)<=20:
            gameison=False
            score.gameover()
            break

screen.exitonclick()        