
# ---------------------------- CONSTANTS ------------------------------- #
from typing import Text


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
CHECKMARK = '✔'
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer')
    check_label.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 ==0:
        count_down(long_break_sec)
        timer_label['text'] = 'LONG BREAK'
        timer_label.config(fg=RED)
    elif reps % 2 ==0:
        count_down(short_break_sec)
        timer_label['text'] = 'SHORT BREAK'
        timer_label.config(fg=PINK)
    else:
        count_down(work_sec)
        timer_label['text'] = 'GET TO WORK'
        timer_label.config(fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import math
import time
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec<10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        global reps
        num_check = reps // 2
        check_label['text'] = CHECKMARK * num_check


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import Button, PhotoImage, Tk, Label, Entry, Canvas, font
from tkinter.constants import END, MULTIPLE
window = Tk()
window.title("Pomodoro App")
window.minsize(width=500, height=300)
window.config(padx=100, pady=50, bg=YELLOW)
window.grid()

timer_label = Label(text='Timer', font=(FONT_NAME, 48, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='./tomato.png')
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100, 139, text='00:00', fill='white', font=(FONT_NAME,35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label( font=(FONT_NAME, 24, 'bold'), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)







window.mainloop()