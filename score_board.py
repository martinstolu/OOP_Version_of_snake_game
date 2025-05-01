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
        self.update_score_board()

    def update_score_board(self):
        self.write(arg= f"Score: {self.score}", move= True,
                   align= ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg= "Game over",
                   move= True, align= ALIGNMENT,
                   font= GAME_OVER_FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.goto(x=0, y=280)
        self.update_score_board()