from turtle import Turtle
ALIGNMENT="center"
FONT=('Arial',10,'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.goto(0,280)
        self.hideturtle()
        self.upd_score()
    def upd_score(self):
        self.write(f"Score:{self.score}",False,align=ALIGNMENT,font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("GameOver",False,align=ALIGNMENT,font=FONT)

    def score_add(self):
        self.score+=1
        self.clear()
        self.upd_score()
        #obj.write

        #return self.score