from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# CONSTANTS
BG = "#F0E4D7"

# PASSWORD GENERATOR 
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    
    password = "".join(password_list)
    pass_input.insert(0, password)
    pyperclip.copy(password)

# SAVE PASSWORD 
    # src https://www.w3schools.com/python/python_file_write.asp,  https://tkdocs.com/tutorial/widgets.html#entry 
    # src https://pypi.org/project/pyperclip/
def save():
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", 
            message="Please make sure you haven't left any fields empty."
            )
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4) # will dump the data into file
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4) # will dump the data into file
        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)

# FIND PASSWORD
def find_password():
    website = web_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
            
# UI SETUP 
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BG)

canvas = Canvas(width=200, height=200, bg=BG, highlightthickness=0)
img = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=1)

# Labels
web_label = Label(text="Website: ")
web_label.grid(column=0, row=2)
web_input = Entry(width=35)
web_input.grid(column=1, row=2, columnspan=1)
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=2)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=3)
email_input = Entry(width=35)
email_input.grid(column=1, row=3, columnspan=1)

pass_label = Label(text="Password: ")
pass_label.grid(column=0, row=4)
pass_input = Entry(width=21)
pass_input.grid(column=1, row=4, columnspan=1)
gen_button = Button(text="Generate Password", command=generate_password)
gen_button.grid(column=2, row=4)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=5, columnspan=1)



window.mainloop()