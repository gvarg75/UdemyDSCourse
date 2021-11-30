from tkinter import Entry, Tk, Button, Label
from tkinter import ttk

window = Tk()
window.title("My second GUI Program")
window.minsize(width=500, height=300)

#Label
mylabel = Label(text='I am a label', font = ("Ariel", 24, "bold"))
mylabel.pack()


def button_clicked():
    mylabel['text'] = input.get()

button = Button(text= "Click Me", command = button_clicked)
button.pack()

input = Entry(width=10)
input.pack()




window.mainloop()