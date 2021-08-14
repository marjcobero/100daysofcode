from tkinter import *
import time
import math


# CONSTANTS
GRAY = "#716F81"
PURPLE = "#B97A95"
ORANGE = "#F6AE99"
YELLOW = "#F2E1C1"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# TIMER RESET
def reset():
    window.after_cancel(timer)
    canvas.config(timer_text, text="00:00")
    title.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0

# TIMER MECHANISM 
def start_timer():
    global reps
    reps += 1 
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break)
        title.config(text="Break", fg=PURPLE)
    elif reps % 2 == 0:
        countdown(short_break)
        title.config(text="Break", fg=ORANGE)
    else:
        countdown(work_sec)
        title.config(text="Work", fg=YELLOW)

# COUNTDOWN MECHANISM 
def countdown(count):
    count_min = math.floor(count / 60) # this will give us the number of minutes
    count_sec = count % 60 # modular will help us get the seconds left
    if count_sec < 10:
        count_sec = f"0{count_sec}" #this will set the timer in seconds to 2 digits
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1) # It executes a command after a time delay, this is in mls
    else:
        start_timer()
        check = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            check += "✔️"
        checkmark.config(text=check)

# UI SETUP 
window = Tk()
window.title("Study Timer")
window.config(padx=100, pady=50, bg=GRAY)

title = Label(text="Timer", fg=ORANGE, bg=GRAY, font=(FONT_NAME, 45))
title.grid(column=1, row=0)

canvas = Canvas(width=452, height=452, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="clock.png")
canvas.create_image(226, 228, image=img)
timer_text = canvas.create_text(217, 223, text="00:00", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="start",  highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="reset",  highlightthickness=0, command=reset)
reset.grid(column=2, row=2)

checkmark = Label(text="✔️", fg=ORANGE, bg=GRAY)
checkmark.grid(column=1, row=3)


window.mainloop()