from tkinter import *
import math

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
def reset_timer():
   start_button["state"] = "normal"
    root.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=#A020F0')
    check_marks.config(text="")
    global reps
    reps = 0
def start_timer():
   start_button["state"] = "disabled"
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = root.after(1000, count_down, count - 1)
        else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)

        for _ in range(work_sessions):
            marks += "✓"

        check_marks.config(text=marks)
