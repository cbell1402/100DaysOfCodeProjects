from tkinter import *
from tkinter import messagebox
import random
import string
import json

FONT = ("lucida grande", 10, "normal")
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    """Generates random password and adds to clipboard"""
    num_letters = random.randint(8, 10)
    num_symbols = random.randint(2, 4)
    num_numbers = random.randint(2, 4)
    password_list = [random.choices(string.ascii_letters, k=num_letters), random.choices(string.digits, k=num_numbers),
                     random.choices(symbols, k=num_symbols)]
    flattened_list = [item for sublist in password_list for item in sublist]
    random.shuffle(flattened_list)

    password = ''.join(str(item) for item in flattened_list)
    pass_input.delete(0, END)
    pass_input.insert(0, password)
    pass_input.clipboard_clear()
    pass_input.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    """Saves information to text file"""
    website = website_input.get().lower()
    email = user_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if website_input.get() == "" or user_input.get() == "" or pass_input.get() == "":
        messagebox.showinfo(title="Warning", message="Please do not leave any fields blank.")
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)

        website_input.delete(0, END)
        pass_input.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #
def search():
    """Returns users password and username"""
    website = website_input.get().lower()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="No Data", message="There is no saved information. Please save some passwords first.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website.title(), message=f"Username: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Bad Website", message="That website is not in the database.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(width=500, height=400, padx=20, pady=20, bg="white")
window.title("Password Manager")

# Create Image
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

# Website Row
website_label = Label(text="Website:", bg="white", font=FONT)
website_label.grid(column=0, row=1)
website_input = Entry(bg="white")
website_input.grid(column=1, row=1, columnspan=1, sticky="EW")
website_input.focus()

# Username Row
user_label = Label(text="Email/Username:", bg="white", font=FONT)
user_label.grid(column=0, row=2)
user_input = Entry(bg="white")
user_input.grid(column=1, row=2, columnspan=2, sticky="EW")

# Password Row
pass_label = Label(text="Password:", bg="white", font=FONT)
pass_label.grid(column=0, row=3)
pass_input = Entry(bg="white")
pass_input.grid(column=1, row=3, sticky="EW")

generate_button = Button(text="Generate Password", bg="white", font=FONT, command=gen_password)
generate_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", bg="white", font=FONT, width=33, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

search_button = Button(text="Search", bg="white", font=FONT, command=search)
search_button.grid(column=2, row=1, sticky="EW")

canvas.mainloop()
