from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.6, 0.6)
        self.color("green")
        self.penup()
        self.move_speed = 0.0001
        self.start_ball()

    def start_ball(self):
        self.goto(-100,0)
        ball_orientation = random.uniform(-36, 36)
        self.setheading(ball_orientation)

    def bounce(self, y):
        current_orientation = self.heading()
        if y == "y":
            new_orientation = 180 - current_orientation
            self.setheading(new_orientation)
        if y == "x":
            new_orientation = -current_orientation
            self.setheading(new_orientation)
