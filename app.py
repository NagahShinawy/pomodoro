"""
created by Nagaj at 03/07/2021
"""

from tkinter import *
from tkinter import messagebox

# from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.2
LONG_BREAK_MIN = 20
reps = 0
timer = None


def show_notification(msg):
    messagebox.showinfo(title="test", message=msg)


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    count_down(25 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):
    global timer
    count_minutes = seconds // 60
    count_seconds = seconds % 60
    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if seconds > 0:
        # wait 1 second then run function[count_down with params count - 1]
        window.after(1000, count_down, seconds - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)  # YELLOW
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(row=0, column=1)
# Canvas: allow you to layer things one on top of the others
# ex: add image to screen and layout text on top of that
canvas = Canvas(width=200, height=224, bg="green", highlightthickness=5)  # # YELLOW
tomato_img = PhotoImage(file="tomato.png")
# canvas accept <PhotoImage> obj not <str> as path
# image in the center of the canvas so, it takes high of x & y of canvas dimensions
canvas.create_image(104, 112, image=tomato_img)
timer_text = canvas.create_text(104, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
# count_down(5)
# canvas.pack()

start_btn = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
reset_btn = Button(text="Reset", bg=YELLOW)

start_btn.grid(row=2, column=0)
reset_btn.grid(row=2, column=2)

check_label = Label(text="✔", fg="green")
check_label.grid(row=2, column=1)

window.mainloop()
