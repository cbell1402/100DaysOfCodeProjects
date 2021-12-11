from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
CHECK = "✔"
NUMBER_CHECKS = 0
time_keeper = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global NUMBER_CHECKS, REPS
    NUMBER_CHECKS = 0
    REPS = 0
    window.after_cancel(time_keeper)
    check_label.config(text="")
    canvas.itemconfig(timer, text="00:00")
    timer_label.config(text="Reset", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif REPS % 2 != 0:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
    elif REPS % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global NUMBER_CHECKS, time_keeper
    # print(count)
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
    if count > 0:
        time_keeper = window.after(1000, count_down, count - 1)
    else:
        if REPS % 2 != 0:
            NUMBER_CHECKS += 1
            check_label.config(text=CHECK * NUMBER_CHECKS)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(width=500, height=400, padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", font=FONT_NAME, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=FONT_NAME, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(bg=YELLOW, fg=GREEN, font=10)
check_label.grid(column=1, row=3)

window.mainloop()
