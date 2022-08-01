from turtle import Turtle, Screen
from paddle import Paddle, Line
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.colormode(255)
screen.bgcolor("black")

screen.listen()
screen.tracer(0)

line = Line()
paddle1 = Paddle(-1, "magenta")
paddle1.goto(-350, 0)
paddle2 = Paddle(1, "cyan")
paddle2.goto(350, 0)

screen.onkey(paddle1.move_up, "a")
screen.onkey(paddle1.move_down, "z")
screen.onkey(paddle2.move_up, "Up")
screen.onkey(paddle2.move_down, "Down")

ball = Ball()

scoreboard1 = Scoreboard(-1, color="magenta")
scoreboard2 = Scoreboard(1, "cyan")
segments_horizontal = []
segments_vertical = []


def make_horizontal_fence(x, z):
    for i in range(-x, x):
        segment = Turtle()
        segment.shape("square")
        segment.shapesize(stretch_wid=0.5)
        segment.color("yellow")
        segment.penup()
        # segment.right(y)
        segment.goto(10 * i, z)
        segments_horizontal.append(segment)


def make_vertical_fence(x, z):
    for i in range(-x, x):
        segment = Turtle()
        segment.shape("square")
        segment.shapesize(stretch_wid=0.5)
        segment.color("yellow")
        segment.penup()
        segment.right(90)
        segment.goto(z, 10 * i)
        segments_vertical.append(segment)


player1_points = 0
player2_points = 0


def serve():
    self = Turtle()
    self.penup()
    self.goto(0, 0)
    self.color(187, 134, 252)
    self.hideturtle()
    self.write(f"Serve : {player1_points + player2_points + 1}", move=False, align="center",
               font=("Courier", 40, "normal"))
    self.clear()


make_horizontal_fence(40, 300)
make_horizontal_fence(40, -300)
make_vertical_fence(30, 400)
make_vertical_fence(30, -400)

game_on = True

while game_on:
    if ball.xcor() >= 0:
        ball.color("magenta")
    elif ball.xcor() <= 0:
        ball.color("cyan")
    screen.update()
    time.sleep(ball.move_speed)
    ball.forward(5)
    if ball.distance(paddle1) < 50 and -340 > ball.xcor() > -345:
        print(ball.xcor(), ball.ycor())
        print("I hit")
        ball.bounce("y")
        ball.move_speed *= 0.5

    if ball.distance(paddle2) < 50 and 340 < ball.xcor() < 345:
        ball.bounce("y")
        ball.move_speed *= 0.9

    for segment in segments_vertical:
        if ball.distance(segment) < 15:

            if ball.xcor() > 0:
                scoreboard1.clear()
                print(ball.xcor())
                player1_points += 1
                scoreboard1.increase_score()
            if ball.xcor() < 0:
                scoreboard2.clear()
                print(ball.xcor())
                player2_points += 1
                scoreboard2.increase_score()
            ball.hideturtle()
            ball.move_speed = 0.01
            ball = Ball()
            serve()
            time.sleep(1)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce("x")

screen.exitonclick()
