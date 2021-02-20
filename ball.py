from turtle import Turtle
import game_settings
from random import randint
import time


class Ball(Turtle):

    def __init__(self, field_width):
        super().__init__()
        self.penup()
        self.color(game_settings.BALL_COLOR)
        self.shape("circle")
        self.stretch = field_width * 0.0012
        self.shapesize(stretch_wid=self.stretch, stretch_len=self.stretch)

    def north_collision(self, top):
        if self.ycor() >= top - 15 * self.stretch:
            new_heading = 360 - self.heading() + randint(-1, 1) * game_settings.ANGLE_CHANGE
            self.setheading(new_heading)
            return True

    def south_collision(self, bottom):
        if self.ycor() <= bottom + 15 * self.stretch:
            new_heading = 360 - self.heading() + randint(-1, 1) * game_settings.ANGLE_CHANGE
            self.setheading(new_heading)
            return True

    def game_over(self, is_over):
        if is_over:
            self.goto(0, 0)
            self.write("Game Over", False, align="center", font=("Courier", int(50 * self.stretch), "bold"))
            self.hideturtle()

    def reset(self):
        self.goto(0, 0)
        time.sleep(1)
