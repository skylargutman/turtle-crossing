import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = []
scoreboard = Scoreboard()

#generate 10 cars to start
for _ in range(1,11):
    cars.append(CarManager())

#listen for keys
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")


game_counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #Move cars and detect collision
    for car in cars:
        car.move()
        if player.distance(car) < 30 and abs(player.ycor() - car.ycor()) < 20:
            scoreboard.game_over()
            game_is_on = False

    #Add car
    if game_counter % 5 == 0:
        cars.append(CarManager())

    #counter for generating next car
    game_counter +=1

    #detect score
    if player.ycor() > 280:
        #player score
        scoreboard.update_score()
        player.restart()

screen.exitonclick()