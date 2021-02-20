from turtle import Turtle
import game_settings


class Paint(Turtle):

    def __init__(self):
        super().__init__()
        self.percent = 0
        self.pencolor(game_settings.MARGIN_COLOR)
        self.penup()
        self.hideturtle()
        self.pensize(20)
        self.speed("fastest")

    def draw_line(self, length, percentage):
        self.pendown()
        draw = length * (100 - percentage) / 100
        self.forward(draw)
        self.penup()
        self.forward(length - draw)

    def draw_border(self, left, bottom, top):
        line_length = left * 2
        my_x_zero = - left
        # find the corner to start
        self.goto(my_x_zero, bottom)
        self.draw_line(line_length, 0)
        self.goto(my_x_zero, top)
        self.draw_line(line_length, 0)

    def draw_center(self, window_height):
        self.penup()
        self.goto(0, window_height / 2)
        self.setheading(270)
        center_length = int(window_height / 10)
        self.pendown()
        for i in range(11):
            self.draw_line(center_length, 60)
