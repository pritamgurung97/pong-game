from turtle import Turtle

DOWN = 270


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.pencolor("white")
        self.goto(0, 300)
        self.seth(DOWN)
        self.hideturtle()
        self.iterations()

    def iterations(self):
        for i in range(30):
            self.dashed_line()

    def dashed_line(self):
        self.pendown()
        self.fd(10)
        self.penup()
        self.fd(10)
