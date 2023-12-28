from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
LIGHT_RED = "#e2979c"
DARK_RED = "#e7305b"
LIGHT_GREEN = "#9bdeac"
LIGHT_YELLOW = "#f7f5dd"
FONT_STYLE = "Courier"
WORK_MINUTES = 1
SHORT_BREAK_MINUTES = 5
LONG_BREAK_MINUTES = 20
session_count = 0
active_timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_pomodoro():
    window.after_cancel(active_timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Pomodoro Timer")
    check_marks.config(text="")
    global session_count
    session_count = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_pomodoro():
    global session_count
    session_count += 1

    work_seconds = WORK_MINUTES * 60
    short_break_seconds = SHORT_BREAK_MINUTES * 60
    long_break_seconds = LONG_BREAK_MINUTES * 60

    if session_count % 8 == 0:
        initiate_countdown(long_break_seconds)
        title_label.config(text="Long Break", fg=DARK_RED)
    elif session_count % 2 == 0:
        initiate_countdown(short_break_seconds)
        title_label.config(text="Short Break", fg=LIGHT_RED)
    else:
        initiate_countdown(work_seconds)
        title_label.config(text="Work Session", fg=LIGHT_GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def initiate_countdown(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global active_timer
        active_timer = window.after(1000, initiate_countdown, count - 1)
    else:
        start_pomodoro()
        marks = ""
        completed_sessions = math.floor(session_count / 2)
        for _ in range(completed_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Custom Pomodoro Timer")
window.config(padx=100, pady=50, bg=LIGHT_YELLOW)

title_label = Label(text="Pomodoro Timer", fg=LIGHT_GREEN, bg=LIGHT_YELLOW, font=(FONT_STYLE, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=LIGHT_YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_STYLE, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_pomodoro)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_pomodoro)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=LIGHT_GREEN, bg=LIGHT_YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
