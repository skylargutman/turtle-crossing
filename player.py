from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("red")
        self.shape("turtle")
        self.setheading(90)
        self.goto(0,-280)

    def move_up(self):
        self.setheading(90)
        self.forward(30)

    def move_left(self):
        self.setheading(180)
        self.forward(30)

    def move_right(self):
        self.setheading(0)
        self.forward(30)

    def restart(self):
        self.goto(0, -280)
        self.setheading(90)