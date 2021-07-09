"""
created by Nagaj at 03/07/2021
"""

from tkinter import *

# from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        title_label.config(text="BREAK", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:  # 2th/4th/6th
        title_label.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)
    else:
        # 1st/3th/5th/7th
        title_label.config(text="WORK", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):
    count_minutes = seconds // 60
    count_seconds = seconds % 60
    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if seconds > 0:
        # wait 1 second then run function[count_down with params count - 1]
        global timer
        timer = window.after(1000, count_down, seconds - 1)
    else:
        start_timer()
        work_sessions = (
                reps // 2
        )  # for every 2 repos means you completed 1 work session[1 rep work + 1 rep break]
        marks = ""
        for _ in range(work_sessions):
            marks += "✔"

        check_marks.config(text=marks)


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
timer_text = canvas.create_text(
    104, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)
# count_down(5)
# canvas.pack()

start_btn = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
reset_btn = Button(text="Reset", bg=YELLOW, command=reset_timer)

start_btn.grid(row=2, column=0)
reset_btn.grid(row=2, column=2)

check_marks = Label(fg="green")
check_marks.grid(row=2, column=1)

window.mainloop()
