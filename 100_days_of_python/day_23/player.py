from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.left(90)
        self.level = 1
    
    def up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)
        

    def check_finish(self):
        if self.ycor() == FINISH_LINE_Y:
            self.level += 1
            self.goto(STARTING_POSITION)