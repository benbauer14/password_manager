import tkinter
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def store_password():
    pass

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