from turtle import Screen, Turtle 
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# Screen Settings
screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

# Paddle Settings
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
# Right paddle settings
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# Left paddle settings
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Ball settings
ball = Ball()

# Scoreboard settings
scoreboard = Scoreboard()

# Update's the game settings
game_on = True
while game_on:
    screen.update()
    ball.move()
    
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()