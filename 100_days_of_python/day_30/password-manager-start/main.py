# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import builtins
import random
import json

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for x in range(nr_letters)]
    password_symbols = [random.choice(symbols)for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter.constants import END
from tkinter import messagebox

def find_password():
    website = website_entry.get()

    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='No entries yet', message='Please add passwords')
    else:
        try:
            entry = data[website]
            messagebox.showinfo(title=website, message= f"Your username is {data[website]['email']} and your password is {data[website]['password']}")
        except KeyError:
            messagebox.showinfo(title='No entry', message='No details for the website exists')


def save():
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Missing Info', message='Please fill out all fields')
        
    else:    
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \n\n\n\nIs it ok to save?")
        if is_ok:
            #Writes to .txt file
            #with open('./passwords.txt','a') as file:
                #file.write(f"{website} | {email} | {password}"'\n')
            try:
                with open('data.json', 'r') as data_file:
                    #Reading old data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                #updating old data with new data
                data.update(new_data)
                with open('data.json', 'w') as data_file:
                    #saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
        

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import Entry, Label, Tk, Button, Canvas, PhotoImage, image_names

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)



canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file= './logo.png')
canvas.create_image(100,100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_entry = Entry(width=17)
website_entry.focus()
website_entry.grid(column=1, row=1)

website_search = Button(text='Search', command=find_password)
website_search.grid(column=2, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)
user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, 'testemail@email.com')

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_button = Button(text='Generate Password', command= generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)






window.mainloop()