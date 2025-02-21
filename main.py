from tkinter import *
from tkinter import messagebox
import json
import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_nr = random.randint(8, 10)
    numbers_nr = random.randint(2, 4)
    symbols_nr = random.randint(2, 4)

    # new item for item in iterable
    password_list = []
    for i in range(letters_nr):
        password_list += random.choice(letters)

    for i in range(numbers_nr):
        password_list += random.choice(numbers)

    for i in range(symbols_nr):
        password_list += random.choice(symbols)

    random.shuffle(password_list)
    print(password_list)
    password = ''.join(password_list)
    password_entry.insert(END, string=password)


def add_details():
    password = password_entry.get()
    website = web_entry.get().lower()
    username = username_entry.get()
    details = {website: {"username": username, "password": password}}
    if len(password) == 0 or len(website) == 0:
        messagebox.showerror(title="Oops", message="Please input your details!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(details, data_file, indent=4)
        else:
            data.update(details)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)


def search_password():
    website_search = web_entry.get().lower()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="oops", message="THAT FILE DOES NOT EXIST")
    else:
        if website_search in data:
            username = data[website_search]["username"]
            password = data[website_search]["password"]
            messagebox.showinfo(title=website_search.upper(),
                                message=f"username: {username}\n"
                                        f"password: {password}")

        else:
            messagebox.showerror(title="Oops", message=f"details for {website_search.upper()} not found")


window = Tk()
window.title("PASSWORD MANAGER 2")
window.config(padx=20, pady=20)

canvas = Canvas()
image_file = PhotoImage(file="logo.png")
canvas.config(width=200, height=200)
canvas.create_image(100, 95, image=image_file)
canvas.grid(row=0, column=1)

web_label = Label()
web_label.config(text="Website")
web_label.grid(row=1, column=0)

username_label = Label()
username_label.config(text="Email/Username")
username_label.grid(column=0, row=2)

password_label = Label()
password_label.config(text="Password")
password_label.grid(column=0, row=3)

web_entry = Entry()
web_entry.config(width=35)
web_entry.insert(END, string="")
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry()
username_entry.config(width=35)
username_entry.insert(0, string="labankalwigi05@gmail.com")
username_entry.focus()
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry()
password_entry.config(width=35)
password_entry.insert(END, string="")
password_entry.focus()
password_entry.grid(column=1, row=3, columnspan=2)

generate_button = Button(command=generate_password)
generate_button.config(text="Generate Password")
generate_button.grid(row=1, column=3)

add_button = Button(command=add_details)
add_button.config(text="Save")
add_button.grid(column=3, row=3)

search_button = Button(command=search_password)
search_button.config(text="Search Password")
search_button.grid(column=3, row=2)

window.mainloop()
