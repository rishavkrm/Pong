from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x,color):
        super().__init__()
        self.create_paddle(x,color=color)

    def create_paddle(self, x,color):
        self.shape("square")
        self.shapesize(0.3, 4)
        self.color(color)
        self.right(90)
        self.penup()
        self.goto(x * 350, 0)

    def move_up(self):
        if 250 > self.ycor():
            for x in range(0, 4):
                self.fd(-5)

    def move_down(self):
        if self.ycor() > -250:
            for x in range(0, 4):
                self.fd(5)


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        # self.speed("fastest")
        self.right(-90)
        self.shape("square")
        self.shapesize(stretch_wid=0.1, stretch_len=0.4)
        self.penup()
        self.goto(0, 300)
        while self.ycor() > -300:
            self.pendown()
            self.fd(-5)
            self.penup()
            self.fd(-5)
        self.hideturtle()
