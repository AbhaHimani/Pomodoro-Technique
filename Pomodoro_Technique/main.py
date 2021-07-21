import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
# ------------------------------UI----------------------------------- #

timer=None

reps=0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    tomato_label.config(text="Timer", fg="black")
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        tomato_label.config(text="Break",fg="red")

    elif reps % 2 == 0:
        count_down(short_break_sec)
        tomato_label.config(text="Break", fg="red")
    else:

        count_down(work_sec)
        tomato_label.config(text="Work", fg="green")


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "0"
    if int(count_sec)<10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer=window.after(1000, count_down, count-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window= tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_label = tkinter.Label(text="TIMER", font=("Arial", 24, "bold"), bg=YELLOW)
tomato_label.grid(row=2, column=2)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(103, 130, text="00:00", font=("Arial", 24, "bold"), fill="white")
canvas.grid(row=3, column=2)
#Button-1
button = tkinter.Button(text="Start", command = start_timer)
button.grid(row=4, column=1)
#Button-2
button = tkinter.Button(text="Reset", command= reset_timer)
button.grid(row=4, column=3)
check_marks = tkinter.Label(text="✅", fg=GREEN, bg=YELLOW)
check_marks.grid(column=2, row=4)


window.mainloop()
