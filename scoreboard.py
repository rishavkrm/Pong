from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self,x,color):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(x*200, 260)
        self.hideturtle()
        self.color(color)
        self.update_scoreboard()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.color("orange")
        self.write(f"GAME OVER", move=False, align="center", font=("Sans Serif", 24, "normal"))


    def update_scoreboard(self):
        self.hideturtle()
        self.write(f"Score : {self.score}", move=False, align="center", font=("Courier", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.write(f"Score : {self.score}", move=False, align="center", font=("Courier", 20, "normal"))
