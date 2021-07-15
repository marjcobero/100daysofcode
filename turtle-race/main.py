"""Building a turtle race game where you can bet on any choice of color with Turtle library"""

#importing turtle library
from turtle import Turtle, Screen, color, title



#screen from the python library so that we have a visual of what i am creating
screen = Screen()

#setting up the screen and its size 
screen.setup(width=500, height=400)

#adding a greeting before the game starts using the built in method textinput
#this needs to be returned so we will need to declare this for an output
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

#creating different color for the turtles
colors = ['red', 'purple', 'blue', 'yellow', 'green', 'orange']

#postions for the turtles
y_positions = [-70, -40, -10, 20, 50, 80]


#to create different colors of turtle
for turtle_index in range(0, 6):
    #tim is the name of the turtle
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    #the direction of tim is going
    tim.goto(x=-230, y=y_positions)



"""Screen settings"""
screen.listen()
#when you click on the screen it will automatically exit
screen.exitonclick()