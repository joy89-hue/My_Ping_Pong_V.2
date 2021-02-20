from tkinter import *

TABLE_SIZE_WITH = 1200
TABLE_SIZE_HEIGHT = 600
TABLE_X_POSITION = None
TABLE_Y_POSITION = 10

FIELD_COLOR = "white"
BALL_COLOR = "black"
PADDLE_COLOR = "black"
MARGIN_COLOR = "black"

BALL_SPEED = 10
SPEED_INCREASE = 0
ANGLE_CHANGE = 0
IS_HARD = False


def screen_size(ad, bms):
    global TABLE_SIZE_WITH, TABLE_SIZE_HEIGHT
    if ad == 1:
        # this option is relative to the screen size
        TABLE_SIZE_WITH = 0.89
        TABLE_SIZE_HEIGHT = 0.86
    else:
        # fixed size options Big, Medium, Small
        if bms == 1:
            TABLE_SIZE_WITH = 1200
            TABLE_SIZE_HEIGHT = 600
        elif bms == 2:
            TABLE_SIZE_WITH = 900
            TABLE_SIZE_HEIGHT = 500
        elif bms == 3:
            TABLE_SIZE_WITH = 600
            TABLE_SIZE_HEIGHT = 300


def color_or_bw(cbw, ygb):
    global FIELD_COLOR, BALL_COLOR, PADDLE_COLOR, MARGIN_COLOR
    if cbw == 1:
        FIELD_COLOR = "black"
        BALL_COLOR = "white"
        PADDLE_COLOR = "white"
        MARGIN_COLOR = "white"
    elif cbw == 2:
        if ygb == 1:
            FIELD_COLOR = "gold"
            BALL_COLOR = "blue"
            PADDLE_COLOR = "green"
            MARGIN_COLOR = "green"
        elif ygb == 2:
            FIELD_COLOR = "pale green"
            BALL_COLOR = "red"
            PADDLE_COLOR = "dark blue"
            MARGIN_COLOR = "dark blue"
        elif ygb == 3:
            FIELD_COLOR = "blue"
            BALL_COLOR = "orange"
            PADDLE_COLOR = "yellow"
            MARGIN_COLOR = "yellow"


def start_game():
    c_b_w = classic.get()
    y_g_b = color.get()
    e_n_h = level.get()
    bms = table_size.get()
    ad = screen_dim.get()
    screen_size(ad, bms)
    color_or_bw(c_b_w, y_g_b)
    game_level(e_n_h)
    root.quit()
    return True


def enable():
    yellow_button.configure(state=NORMAL)
    green_button.configure(state=NORMAL)
    blue_button.configure(state=NORMAL)


def disable():
    yellow_button.configure(state=DISABLED)
    green_button.configure(state=DISABLED)
    blue_button.configure(state=DISABLED)


def enable_fix():
    big_size_button.configure(state=NORMAL)
    medium_size_button.configure(state=NORMAL)
    small_size_button.configure(state=NORMAL)


def disable_fix():
    big_size_button.configure(state=DISABLED)
    medium_size_button.configure(state=DISABLED)
    small_size_button.configure(state=DISABLED)


def game_level(enh):
    global BALL_SPEED, SPEED_INCREASE, ANGLE_CHANGE, IS_HARD
    if enh == 1:
        BALL_SPEED = 15
    elif enh == 2:
        BALL_SPEED = 20
        SPEED_INCREASE = 2
    elif enh == 3:
        BALL_SPEED = 25
        SPEED_INCREASE = 3
        ANGLE_CHANGE = 5
        IS_HARD = True


root = Tk()
# root.geometry("200x200")
root.geometry('%dx%d+%d+%d' % (TABLE_SIZE_WITH / 2.9, TABLE_SIZE_HEIGHT / 1.3, 500, 100))
root.title("My Ping Pong ")

# define label, message, buttons, and radio buttons area
classic = IntVar()
classic.set(1)
color = IntVar()
color.set(1)
level = IntVar()
level.set(1)
screen_dim = IntVar()
screen_dim.set(1)
table_size = IntVar()
table_size.set(1)
label = Label(text='Welcome to Ping-Pong Game', font=("Courier", 20))
message_label1 = Label(text="The controls are 'w' and 's' for left paddle and ", font=('Verdana', 12))
message_label2 = Label(text=" 'up' and 'down' arrows for the right paddle ", font=('Verdana', 12))
empty_label1 = Label(text="")
classic_button = Radiobutton(text='Classic Game', var=classic, value=1, command=disable).place(x=90, y=85)
color_button = Radiobutton(text="Color Game", var=classic, value=2, command=enable).place(x=220, y=85)
message_label3 = Label(text="For color mode pick color combination:", font=('Verdana', 12))
yellow_button = Radiobutton(text='Yellow background, Green paddles and Blue Ball  ', state=DISABLED, var=color, value=1)
green_button = Radiobutton(text=' Green background, Dark blue paddles and Red Ball', state=DISABLED, var=color, value=2)
blue_button = Radiobutton(text=' Blue background, Yellow paddles and Orange Ball ', state=DISABLED, var=color, value=3)
message_label4 = Label(text="For starting level:", font=('Verdana', 12))
easy_button = Radiobutton(text='Easy: The ball speed will not change during the game  ', var=level, value=1)
normal_button = Radiobutton(text='Normal: The ball start normal speed and then increase after ', var=level, value=2)
hard_button = Radiobutton(text='Hard: The ball speed increase and angle change and paddle size', var=level, value=3)
empty_label2 = Label(text="")
adaptive_button = Radiobutton(text='Adaptive table size', var=screen_dim, value=1, command=disable_fix).place(x=90,
                                                                                                              y=297)
fixed_button = Radiobutton(text="Fixed table size", var=screen_dim, value=2, command=enable_fix).place(x=220, y=297)
message_label5 = Label(text="Fixed table size:", font=('Verdana', 12))
big_size_button = Radiobutton(text='Big Size: 1200 X 600  ', state=DISABLED, var=table_size, value=1)
medium_size_button = Radiobutton(text='Medium Size: 900 X 500 ', state=DISABLED, var=table_size, value=2)
small_size_button = Radiobutton(text='Small Size: 600 x 300', state=DISABLED, var=table_size, value=3)
start_button = Button(text="Start Game", command=start_game)

# positioning all components on the pop up window
label.grid(row=0, column=1)
message_label1.grid(row=1, column=1, columnspan=3)
message_label2.grid(row=2, column=1, columnspan=3)
empty_label1.grid(row=3, column=0)
message_label3.grid(row=4, column=0, columnspan=3)
yellow_button.grid(row=5, column=1)
green_button.grid(row=6, column=1)
blue_button.grid(row=7, column=1)
message_label4.grid(row=8, column=0, columnspan=3)
easy_button.grid(row=9, column=1)
normal_button.grid(row=10, column=1)
hard_button.grid(row=11, column=1)
empty_label2.grid(row=12, column=0)
message_label5.grid(row=13, column=0, columnspan=3)
big_size_button.grid(row=14, column=1)
medium_size_button.grid(row=15, column=1)
small_size_button.grid(row=16, column=1)
start_button.grid(row=17, column=1)

mainloop()
