from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.all_cars = [] # An open list so that we can be flexible of how many cars we will add to the game
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        """Creating our cars"""
        random_chance = random.randint(1,6) # every 6 times there is a chance a car is created
        if random_chance == 1:
            car = Turtle(shape="square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup() # This is to make the animation not lag
            car.color(random.choice(COLORS)) # So the car colors are randomly colored
            random_y = random.randint(-250, 250) # Where the cars move randomly in through the y axis in the middle of the screen
            car.goto(300, random_y) 
            self.all_cars.append(car) # adding our cars to the game

    def move_cars(self):
        """To have our cars move through the screen"""
        for car in self.all_cars:
            car.backward(self.car_speed)
    
    def level_up(self):
        """It increases the speed each level of the game"""
        self.car_speed += MOVE_INCREMENT
