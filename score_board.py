from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")
GAME_OVER_FONT = ("Courier", 34, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(x= 0, y= 280)
        with open("data.txt", mode="r") as data:
            self.highscore = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg= f"Score: {self.score} High Score: {self.highscore}", align= ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
            self.score = 0
        else:
            self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.goto(x=0, y=280)
        self.update_scoreboard()