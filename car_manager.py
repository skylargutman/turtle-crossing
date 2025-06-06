import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
LANES = list(range(-240, 260, 30))
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SPEEDS = [10,20,30,40]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.resizemode(rmode="user")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.setheading(180)
        self.goto(260, random.choice(LANES))
        self.color(random.choice(COLORS))
        self.car_speed = random.choice(SPEEDS)

    def move(self):
        self.forward(self.car_speed)
