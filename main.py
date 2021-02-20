from turtle import Screen
from painter import Paint
from stick import Stick
from ball import Ball
from scores import Scoreboard
from game_settings import TABLE_SIZE_WITH, TABLE_SIZE_HEIGHT, TABLE_X_POSITION, TABLE_Y_POSITION, IS_HARD
from winsound import Beep
import time
import game_settings
from random import randint

# set up the table for the ping-pong game
# the dimensions are changed in the game settings according with the option

field = Screen()
field.setup(width=TABLE_SIZE_WITH, height=TABLE_SIZE_HEIGHT, startx=TABLE_X_POSITION, starty=TABLE_Y_POSITION)
field.screensize(canvwidth=1, canvheight=1)
field.title("My Ping Pong Game")
BOTTOM_MARGIN = field.window_height() * (-0.5) + 12
TOP_MARGIN = field.window_height() * 0.5 - 3
LEFT_GOAL = field.window_width() * (-0.5)
RIGHT_GOAL = field.window_width() * 0.5
field.bgcolor(game_settings.FIELD_COLOR)

# field dimensions to be sent like parameters to other files

x_width = field.window_width()
y_height = field.window_height()
pencil = x_width * 0.01
field.tracer(0)

# painting the playing field

painter = Paint()
painter.pensize(int(pencil))
painter.draw_border(LEFT_GOAL, BOTTOM_MARGIN, TOP_MARGIN)
painter.draw_center(y_height)

# defining the ball, game start with the ball going toward right at a random angle

ball = Ball(x_width)
ball_speed = game_settings.BALL_SPEED
speed_increase = game_settings.SPEED_INCREASE
angle_change = game_settings.ANGLE_CHANGE
angle = randint(-60, 60)
ball.setheading(angle)

# defining the paddles and their position

r_paddle_pos = RIGHT_GOAL - 23
l_paddle_pos = LEFT_GOAL + 13
left_stick = Stick((l_paddle_pos, 0), y_height, x_width)
right_stick = Stick((r_paddle_pos, 0), y_height, x_width)

# calculate the paddle dimensions variable with the table size but fixed relative to the paddle movement
# dimensions are needed for calculating the interaction area with the ball

y_adjustment = left_stick.stick_height * 10
x_adjustment = left_stick.thick * 10 + ball.stretch * 10

# calculating the x coordinates of the face of the paddle that touch the ball

right_virtual_wall = r_paddle_pos - x_adjustment
left_virtual_wall = l_paddle_pos + x_adjustment

# initializing the score, the boolean parameter refer if is on the right side of the field

score_right = Scoreboard(y_height, x_width, True)
score_right.set_start()
score_right.score_ini()
score_left = Scoreboard(y_height, x_width, False)
score_left.set_start()
score_left.score_ini()

is_hit = False
is_game_over = False
right_no_touch = True
left_no_touch = True
r_coeff = right_stick.coefficient
l_coeff = left_stick.coefficient


def goal_reset():
    global right_no_touch, left_no_touch, ball_speed, r_coeff, l_coeff, y_adjustment
    right_no_touch = True
    left_no_touch = True
    ball.reset()
    ball_speed = game_settings.BALL_SPEED
    right_stick.stick_shrink(11)
    left_stick.stick_shrink(11)
    r_coeff = right_stick.coefficient
    l_coeff = left_stick.coefficient
    right_stick.speed = 20
    left_stick.speed = 20
    y_adjustment = left_stick.stick_height * 10


goal_reset()

while not is_game_over:
    #  setting the action keys
    time.sleep(0.01)
    field.onkeypress(fun=right_stick.move_up('Up'), key="Up")
    field.onkeypress(fun=left_stick.move_up("w"), key="w")
    field.onkeypress(fun=right_stick.move_down('Down'), key="Down")
    field.onkeypress(fun=left_stick.move_down('s'), key="s")
    field.listen()

    # action part of the game
    # ball bouncing on paddles

    if right_no_touch:
        # check for contact only if close enough
        if ball.distance(right_stick) < ball_speed + 60:
            # check if ball is not way above or under paddle
            if right_stick.ycor() + y_adjustment > ball.ycor() > right_stick.ycor() - y_adjustment:
                # check the ball distance from the virtual wall
                if ball.xcor() >= right_virtual_wall:
                    is_hit = True
                    # to avoid ball bouncing inside paddle
                    right_no_touch = False
                    left_no_touch = True
                    # speed change on normal and hard mode but capped at 50
                    if ball_speed <= 50:
                        ball_speed += speed_increase
                        right_stick.speed += speed_increase
                        print(ball_speed)
                    else:
                        if right_stick.coefficient > 4 and IS_HARD:
                            r_coeff -= 1
                            right_stick.stick_shrink(r_coeff)
                            y_adjustment = left_stick.stick_height * 10
    if left_no_touch:
        if ball.distance(left_stick) < ball_speed + 60:
            if left_stick.ycor() + y_adjustment > ball.ycor() > left_stick.ycor() - y_adjustment:
                if ball.xcor() <= left_virtual_wall:
                    is_hit = True
                    right_no_touch = True
                    left_no_touch = False
                    if ball_speed <= 50:
                        ball_speed += speed_increase
                        left_stick.speed += speed_increase
                    else:
                        if left_stick.coefficient > 4 and IS_HARD:
                            l_coeff -= 1
                            left_stick.stick_shrink(r_coeff)
    if is_hit:
        new_heading = 180 - ball.heading() + randint(-1, 1) * angle_change  # angle change on hard mode
        ball.setheading(new_heading)
        Beep(1500, 10)

    # ball is far enough from the paddle so we reset is hit variable

    if ball.xcor() < RIGHT_GOAL - 100 or ball.xcor() > LEFT_GOAL + 100:
        is_hit = False

    #  hit wall
    if ball.north_collision(TOP_MARGIN):
        Beep(1000, 10)
    if ball.south_collision(BOTTOM_MARGIN):
        Beep(1000, 10)

    # scoring a goal
    if ball.xcor() > RIGHT_GOAL:
        # update the score and reset all variables
        is_game_over = score_left.score_update()
        goal_reset()
        ball.setheading(randint(120, 240))
        if is_game_over:
            ball.game_over(True)
    if ball.xcor() < LEFT_GOAL:
        is_game_over = score_right.score_update()
        goal_reset()
        ball.setheading(randint(-60, 60))
        if is_game_over:
            ball.game_over(True)

    ball.forward(ball_speed)
    field.update()

field.exitonclick()
