from turtle import Screen, Turtle
from snake import Snake
import time


"""Building the classic snake game"""


"""Screen settings"""
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nokia Snake Game")
screen.tracer(0)


"""Snake controls settings"""
#importing Snake class
snake = Snake()
screen.listen()
#keyboard controls for the snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()


screen.exitonclick()