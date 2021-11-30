from tkinter import Canvas, PhotoImage, Tk, Button, Label
from typing import Text
import pandas as pd
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
FONT = 'Ariel'

#Reading the data and creating a dictionary
try:
    data = pd.read_csv('./data/words_to_learn.csv').to_dict(orient='records')
except FileNotFoundError:
    data = pd.read_csv('./data/french_words.csv').to_dict(orient='records')

print(len(data))
word_dict = {}

#Functions
def random_word():
    global word_dict, flip
    window.after_cancel(flip)
    word_dict = choice(data)
    french_word = word_dict['French']
    canvas.itemconfig(language_text, text='French', fill='black')
    canvas.itemconfig(vocab_word, text=french_word, fill='black')
    canvas.itemconfig(card, image=card_front_image)
    flip = window.after(3000, flip_card)

def right_button_click():
    data.remove(word_dict)
    pd.DataFrame(data).to_csv('./data/words_to_learn.csv', index=False)
    
    window.after_cancel(flip)
    random_word()

def wrong_button_click():
    window.after_cancel(flip)
    random_word()

def flip_card():
    canvas.itemconfig(language_text, text='English', fill='white')
    canvas.itemconfig(vocab_word, text=word_dict['English'], fill='white')
    canvas.itemconfig(card, image=card_back_image)

#-----------Creating the User Interface--------
window = Tk()
window.title('Flash Card App')
window.minsize(width=800, height=526)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file='.//images/card_front.png')
card_back_image = PhotoImage(file='./images/card_back.png')
card = canvas.create_image(400, 263, image=card_front_image)
language_text = canvas.create_text(400,150, text='French', fill='black', font=(FONT, 40, 'italic'))
vocab_word = canvas.create_text(400,263, text='French', fill='black', font=(FONT, 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

wrong_button_image = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_button_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=wrong_button_click)
wrong_button.grid(column=0, row=1)

right_button_image = PhotoImage(file='./images/right.png')
right_button = Button(image=right_button_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=right_button_click)
right_button.grid(column=1, row=1)

flip = window.after(3000, flip_card)
random_word()



window.mainloop()