import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard
from random import random


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car = CarManager()
scoreboard = Scoreboard()
count = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.write_level(player)
    screen.onkey(player.up, "Up")
    screen.listen()
    car.create_car()
    car.move()
    if player.check_finish():
        car.restart()
    for cars in car.all_cars:
        if cars.distance(player) <= 25:
            scoreboard.game_over()
            game_is_on = False

    
screen.exitonclick()