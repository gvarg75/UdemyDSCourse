from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        

    def create_car(self):
        chance = randint(1, 6)
        if chance == 6:
            new_car = Turtle('square')
            new_car.penup()
            new_car.goto((300, randint(-250, 250)))
            new_car.shapesize(stretch_wid = 1, stretch_len=2)
            new_car.color(choice(COLORS))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.setx(car.xcor() - STARTING_MOVE_DISTANCE)

    def restart(self):
        self.all_cars = []
        self.clear()
    