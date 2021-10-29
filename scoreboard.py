from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.high_score()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore{self.high_score()}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.high_score()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.high_score()
        self.update_scoreboard()

    def high_score(self):
        with open("data.txt", mode="r") as file:
            current_highscore = int(file.read())
            if current_highscore < self.highscore:
                with open("data.txt", mode="w") as file:
                    file.write(f"{self.highscore}")
            return current_highscore

