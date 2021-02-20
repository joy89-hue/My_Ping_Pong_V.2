from turtle import Turtle
import game_settings

WRITE_COLOR = game_settings.MARGIN_COLOR


class Scoreboard(Turtle):

    def __init__(self, field_height, field_width, is_right):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.penup()
        self.color(WRITE_COLOR)
        self.score = 0
        self.elements = []
        # horizontal element len stretch factor and width stretch factor
        self.h_len = field_width * 0.0022
        self.h_width = field_height * 0.0011
        # vertical element len stretch factor and width stretch factor
        self.v_len = field_width * 0.00061728395
        self.v_width = field_width * 0.00194
        # vertical distance between elements
        self.v_dist = 20 * self.v_width - 10 * self.h_width
        # horizontal distance between elements
        self.h_dist = 20 * self.h_len - 20 * self.v_len
        self.y_start = field_height * 0.45
        if is_right:
            self.x_start = field_width * 0.025
        else:
            self.x_start = -field_width * 0.025 - 1.5 * self.h_dist

    def create_elements(self):
        for i in range(8):
            element = Turtle("square")
            element.hideturtle()
            element.penup()
            element.color(game_settings.PADDLE_COLOR)
            self.elements.append(element)

    def set_start(self):
        self.create_elements()
        # stretching all elements at the right dimensions
        self.elements[0].shapesize(stretch_wid=2 * self.v_width, stretch_len=self.v_len)
        for i in range(1, 4):
            self.elements[i].shapesize(stretch_wid=self.h_width, stretch_len=self.h_len)
        for i in range(4, 8):
            self.elements[i].shapesize(stretch_wid=self.v_width, stretch_len=self.v_len)
        # setting the position for elements
        self.elements[0].goto(self.x_start, self.y_start - self.v_dist)
        self.elements[1].goto(self.x_start + self.h_dist, self.y_start)
        self.elements[2].goto(self.x_start + self.h_dist, self.y_start - self.v_dist)
        self.elements[3].goto(self.x_start + self.h_dist, self.y_start - 2 * self.v_dist)
        self.elements[4].goto(self.x_start + 0.5 * self.h_dist, self.y_start - 0.5 * self.v_dist)
        self.elements[5].goto(self.x_start + 0.5 * self.h_dist, self.y_start - 1.5 * self.v_dist)
        self.elements[6].goto(self.x_start + 1.5 * self.h_dist, self.y_start - 0.5 * self.v_dist)
        self.elements[7].goto(self.x_start + 1.5 * self.h_dist, self.y_start - 1.5 * self.v_dist)

    def draw_0(self):
        self.elements[1].showturtle()
        self.elements[3].showturtle()
        self.elements[4].showturtle()
        self.elements[5].showturtle()
        self.elements[6].showturtle()
        self.elements[7].showturtle()

    def draw_1(self):
        self.elements[1].hideturtle()
        self.elements[3].hideturtle()
        self.elements[4].hideturtle()
        self.elements[5].hideturtle()
        self.elements[6].showturtle()
        self.elements[7].showturtle()

    def draw_2(self):
        self.elements[1].showturtle()
        self.elements[2].showturtle()
        self.elements[3].showturtle()
        self.elements[5].showturtle()
        self.elements[7].hideturtle()

    def draw_3(self):
        self.elements[5].hideturtle()
        self.elements[7].showturtle()

    def draw_4(self):
        self.elements[1].hideturtle()
        self.elements[3].hideturtle()
        self.elements[4].showturtle()

    def draw_5(self):
        self.elements[1].showturtle()
        self.elements[3].showturtle()
        self.elements[6].hideturtle()

    def draw_6(self):
        self.elements[5].showturtle()

    def draw_7(self):
        self.elements[2].hideturtle()
        self.elements[3].hideturtle()
        self.elements[4].hideturtle()
        self.elements[5].hideturtle()
        self.elements[6].showturtle()

    def draw_8(self):
        self.elements[2].showturtle()
        self.elements[3].showturtle()
        self.elements[4].showturtle()
        self.elements[5].showturtle()

    def draw_9(self):
        self.elements[5].hideturtle()

    def draw_10(self):
        self.elements[0].showturtle()
        self.elements[2].hideturtle()
        self.elements[5].showturtle()

    def score_ini(self):
        self.draw_nr[0].__call__(self)

    def score_update(self):
        self.draw_nr[self.score].__call__(self)
        self.score += 1
        if self.score < 10:
            self.draw_nr[self.score].__call__(self)
        else:
            self.draw_nr[self.score].__call__(self)
            return True

    #        return is_game_over
    draw_nr = {
        0: draw_0,
        1: draw_1,
        2: draw_2,
        3: draw_3,
        4: draw_4,
        5: draw_5,
        6: draw_6,
        7: draw_7,
        8: draw_8,
        9: draw_9,
        10: draw_10
    }
