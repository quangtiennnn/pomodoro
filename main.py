from tkinter import *
import math
import random
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
timer =0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text ="Timer",fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if reps%2 != 0:
        check_label.config(text="✓"*math.floor((reps+1)/2))
    reps += 1
    work_sec = 25*60
    short_break_sec = 5*60
    long_break_sec = 20*60
    if reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break",fg=RED)
    else:
        count_down(work_sec)
        timer_label.config(text="Work",fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count%60
    if count >= 0:
        if count_sec < 10:
            canvas.itemconfig(timer_text, text=f"{count_min}:0{count_sec}")
        else:
            canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
        #itemconfig and timer_text
        timer = window.after(10,count_down,count-1)
    # else:


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=223,bg = YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text = "00:00",font=(FONT_NAME,35,"bold"),fill="white")
canvas.grid(row=1,column=1)



timer_label = Label(text="Timer",font=(FONT_NAME,35,"bold"),fg = GREEN,bg=YELLOW)
timer_label.grid(row=0,column=1)

start_button = Button(text ="Start",command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text ="Reset",command=reset_timer)
reset_button.grid(row=2,column=2)

check_label = Label(font=(FONT_NAME,20,"bold"),fg = GREEN,bg=YELLOW)
check_label.grid(row=3,column=1)


window.mainloop()
