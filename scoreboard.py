from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 50, 'bold')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(x=0.00, y=240)
        self.player1_score = 0
        self.player2_score = 0
        self.score_body()

    def score_body(self):
        """Set Score Body"""
        self.write(arg=f"[ {self.player2_score} | {self.player1_score} ]", align=ALIGNMENT, font=FONT)

    def increase_score(self, team_get):
        """Set Scoreboard Increase"""
        if float(team_get) > 0:
            self.player2_score += 1
        elif float(team_get) < 0:
            self.player1_score += 1
        self.clear()
        self.score_body()

    def winner(self):
        if self.player1_score == 5:
            return self.player1_score
        elif self.player2_score == 5:
            return self.player2_score
        else:
            return 0

    def game_over(self):
        """Set GameOver Message"""
        self.home()
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=FONT)


