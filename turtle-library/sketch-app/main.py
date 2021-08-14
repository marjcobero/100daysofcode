from turtle import Turtle, Screen, forward, pen
import turtle

pencil = Turtle()
screen = Screen()

def move_forward():
    pencil.forward(10)
    
    
def move_backward():
    pencil.backward(10)
    
    
def move_left():
    pencil.left(10)
    pencil.heading()
    
    
def move_right():
    pencil.right(10)
    pencil.heading()
    pencil.penup()
    pencil.pendown()


def clear():
    pencil.clear()
    pencil.home()
    
    
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.exitonclick()