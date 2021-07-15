from turtle import Turtle


"""Creating the snake"""


STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180 
RIGHT = 0


class Snake:
    
    
    #calling all of our functions
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    
    #we are creating the snake and designing 
    def create_snake(self):
        for position in STARTING_POSITIONS:
            nokia = Turtle(shape="square")
            nokia.penup()
            nokia.color("white")
            nokia.goto(position)
            self.segments.append(nokia)
    
    
    #to make the snake move 
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    
    """To be able to control the snake's direction"""
    def up(self):
        if self.head.setheading() != DOWN:
            self.head.setheading(UP)
    
    
    def down(self):
        if self.head.setheading() != UP:
            self.head.setheading(DOWN)
    
    
    def left(self):
        if self.head.setheading() != RIGHT:
            self.head.setheading(LEFT)
    
    
    def right(self):
        if self.head.setheading() != LEFT:
            self.head.setheading(RIGHT)