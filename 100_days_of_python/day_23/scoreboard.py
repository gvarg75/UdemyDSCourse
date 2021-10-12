from turtle import Turtle
FONT = ("Courier", 46, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_level(self, player):
        self.goto(-280,280)
        self.pendown()
        self.write(f'Level: {player.level}')


    def game_over(self):
        self.goto(-25,0)
        self.pendown()
        self.write("Game Over", FONT)

class Test(Turtle):
    def __init__(self, shape: str = ..., undobuffersize: int = ..., visible: bool = ...) -> None:
        super().__init__(shape=shape, undobuffersize=undobuffersize, visible=visible)