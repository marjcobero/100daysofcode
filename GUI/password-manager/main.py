from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


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

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(
            title=website, 
            message=f"These are the details entered: \nEmail: {email}"
            f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                web_input.delete(0, END)
                pass_input.delete(0, END)

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