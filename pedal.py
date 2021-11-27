from turtle import Turtle

UP = 90
DOWN = 270


class Pedal(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed(0)
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)

    def down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)

    def block_pedal(self):
        if self.ycor() > 165:
            self.down()
        elif self.ycor() < -235:
            self.up()

