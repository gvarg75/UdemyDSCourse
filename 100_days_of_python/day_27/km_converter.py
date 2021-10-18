from tkinter import Button, Tk, Label, Entry
from tkinter.constants import END, MULTIPLE
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.grid()


equal_text = Label(text = 'is equal to ')
equal_text.grid(column=0, row = 1)

converted = Label(text = '0')
converted.grid(column = 1, row=1)

km_text = Label(text='Km')
km_text.grid(column=2, row=1)

miles_text = Label(text='Miles')
miles_text.grid(column = 2, row = 0)

miles_entry = Entry(width=30)
miles_entry.insert(END, string = '0')
miles_entry.grid(column=1, row=0)

def convert():
    converted['text'] = round(int(miles_entry.get())*1.6)

button = Button(text='Click Me', command=convert)
button.grid(column=1, row=2)





window.mainloop()