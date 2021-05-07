from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", font=("Courier", 80, "normal"), align="center")
        self.goto(100, 200)
        self.write(f"{self.r_score}", font=("Courier", 80, "normal"), align="center")

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def game_over(self, x):
        if self.l_score == 5:
            self.write("Player One Wins")
            x = False
        if self.r_score == 5:
            self.write("Player Two Wins")
            x = False
