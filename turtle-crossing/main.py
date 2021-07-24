import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# Screen Settings
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Imported Classes
car = CarManager()
scoreboard = Scoreboard()
player = Player()

# Press Key Settings
screen.listen()
screen.onkey(player.move_up, "Up")

# Game Settings
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()
        
    # Detect collision with car
    for x in car.all_cars:
        if x.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect when successfully crossed
    if player.game_over():
        player.restart()
        car.level_up()
        scoreboard.increase_level()

screen.exitonclick()