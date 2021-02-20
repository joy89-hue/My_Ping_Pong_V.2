from turtle import Turtle
import keyboard
import game_settings


class Stick(Turtle):

    def __init__(self, position, field_height, field_width):
        super().__init__()
        self.shape("square")
        self.speed = 20
        self.coefficient = 11
        # adjusting the paddle dimension relative to the field size
        self.thick = field_width * 0.0011
        self.stick_height = field_height * 0.001 * self.coefficient
        self.top = field_height * 0.5
        self.shapesize(stretch_wid=self.stick_height, stretch_len=self.thick)
        # setting up the point for the paddle not to exit the screen (field_width*0.01 represent the border thickness)
        self.stop = self.stick_height * 10 + field_width * 0.01 + self.speed * 0.3
        self.color(game_settings.PADDLE_COLOR)
        self.penup()
        self.goto(position)

    # for fluent movement of the paddle while key pressed have to use keyboard module

    def move_up(self, key_p):
        if keyboard.is_pressed(key_p):
            if self.ycor() < self.top + 3 - self.stop:
                new_y = self.ycor() + self.speed
                self.goto(self.xcor(), new_y)

    def move_down(self, key_p):
        if keyboard.is_pressed(key_p):
            if self.ycor() > -self.top - 3 + self.stop:
                new_y = self.ycor() - self.speed
                self.goto(self.xcor(), new_y)

    # making paddle smaller in hard version

    def stick_shrink(self, val):
        self.coefficient = val
        field_height = self.top * 2
        self.stick_height = field_height * 0.001 * self.coefficient
        self.shapesize(stretch_wid=self.stick_height, stretch_len=self.thick)
