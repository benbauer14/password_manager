import tkinter
from tkinter import messagebox
import random
from tkinter.constants import END
from typing import Text
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    input_password.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pyperclip.copy(password)
    input_password.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def store_password():
    if(input_password.get() == "" or input_user.get() == "" or input_website.get() == ""):
        messagebox.showinfo(title="Error!", message="Please complete all inputs")

    with open("passwords.txt", "a") as file:
        file.write(f"{input_website.get()} | {input_user.get()} | {input_password.get()}")
        input_website.delete(0, END)
        input_password.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.minsize(width=300,height=300)
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
canvas.config()
logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1,row=0)

label_web = tkinter.Label(text="Website:")
label_web.grid(column=0, row=1)

label_email = tkinter.Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_pass = tkinter.Label(text="Password:")
label_pass.grid(column=0, row=3)

input_website = tkinter.Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2)

input_user = tkinter.Entry(width=21)
input_user.grid(column=1, row=2)

input_password = tkinter.Entry(width=21)
input_password.grid(column=1, row=3)

button_gen = tkinter.Button(text="Generate Password", command=generate_password)
button_gen.grid(column=2, row=3)

button_add = tkinter.Button(text="Add", command=store_password)
button_add.grid(column=1, row=4)

window.mainloop()