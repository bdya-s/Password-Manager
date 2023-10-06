from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    test = password_input.get()
    if test == "":
        password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website_name = website_input.get()
    email_info = email_user_input.get()
    password_info = password_input.get()

    new_data = {
        website_name: {
            "email": email_info,
            "password": password_info
        }
    }

    if website_name == "" or email_info == "" or password_info == "":
        messagebox.showinfo("Missing info", "Please make sure there aren't any empty fields.")

    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            email_user_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #

def search_info():
    search_text = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!")
    else:
        if search_text in data:
            email = data[search_text].get("email")
            password = data[search_text].get("password")
            messagebox.showinfo(search_text, f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {search_text} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=30, padx=30)

image = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Label - website, email, password
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
email_user_label = Label(text="Email/Username: ")
email_user_label.grid(column=0, row=2)
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# Entry - website, email, password
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
email_user_input = Entry(width=36)
email_user_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Button - generate password, add, search
search_button = Button(text="Search", width=14, command=search_info)
search_button.grid(column=2, row=1)
gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save_info)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
