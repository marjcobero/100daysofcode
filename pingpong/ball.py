from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        """Ball settings"""
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

    # Move settings
    def move(self):
        new_x = self.xcor() + self.x_move 
        new_y = self.ycor() + self.y_move
        self.goto(new_y, new_x)
    
    # Bounce settings
    def bounce_y(self):
        self.y_move *= -1 # This will reverse the cor of move settings ( basically means -10)
    
    def bounce_x(self):
        self.x_move *= -1 
        self.move_speed *= 0.1
    
    # Reset possition when the paddle misses settings
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1 # Speeds up the speeds each time the ball hits the paddle
        self.bounce_x()