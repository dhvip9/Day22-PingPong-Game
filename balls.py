from turtle import Turtle
# from random import randint
PIXEL = 50


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = 10

    def move(self, player1, player2):
        """return bool value"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.is_wall()
        self.is_pedal(player1, player2)

    def is_wall(self):
        """Return bool value"""
        if self.ycor() > 220 or self.ycor() < -295:
            self.bounce_y()

    def is_pedal(self, player1, player2):
        """Checking pedal contact"""
        if self.distance(player1.position()) < PIXEL and self.xcor() > 340:
            self.bounce_x()
        if self.distance(player2.position()) < PIXEL and self.xcor() > -340:
            self.bounce_x()

    def is_out(self):
        x_axis = self.xcor()
        if x_axis > 390 or x_axis < -390:
            return x_axis, False
        else:
            return 0, True

    def bounce_y(self):
        """Return Y axis decrease"""
        self.y_move *= -1

    def bounce_x(self):
        """Return X axis decrease"""
        self.move_speed *= 0.9
        self.x_move *= -1


