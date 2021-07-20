from turtle import Turtle, Screen
import turtle


# Screen Settings
screen = Screen()
screen.color("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")

pong = Turtle()
pong.shape("square")
pong.shapesize(stretch_wid=5, stretch_len=1)
pong.penup()
pong.goto(350, 0)


# Key Settings
def go_up():
    new_y = pong.ycor() + 20
    pong.goto(pong.xcor(), new_y)

def go_down():
    new_y = pong.ycor() - 20
    pong.goto(pong.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")


screen.exitonclick()