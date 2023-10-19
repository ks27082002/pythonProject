from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    entry3.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        entry1.get(): {
            "email": entry2.get(),
            "password": entry3.get()
        }
    }
    if len(entry1.get()) == 0 or len(entry3.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        # is_ok = messagebox.askokcancel(title=entry1.get(), message="These are the details entered :\n Email: "+entry2.get()+"\n"+"Password: "+entry3.get())
        # if is_ok:

        # file.write(entry1.get() + " | " + entry2.get() + " | " + entry3.get() + "\n")
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", mode="w") as new_file:
                json.dump(new_data, new_file, indent=4)
                # entry1.delete(0, END)
                # entry3.delete(0, END)
        else:
            with open("data.json", mode="w") as file:

                json.dump(data, file, indent=4)
                # entry1.delete(0, END)
                # entry3.delete(0, END)
        finally:
            entry1.delete(0, END)
            entry3.delete(0, END)

def search():
    website = entry1.get()
    try:
        with open("data.json") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No password saved")

    else:
        try:
            password = data[website]["password"]
            email = data[website]["email"]
        except KeyError:
            messagebox.showinfo(title="Error", message="Password not registered")
        else:
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
# window.minsize(height=400, width=400)
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
myimage = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=myimage)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

entry1 = Entry(width=33)
entry1.grid(row=1, column=1, sticky="EW")
entry1.focus()

entry2 = Entry(width=35)
entry2.grid(row=2, column=1, columnspan=2, sticky="EW")
entry2.insert(0, "krishna.sharma21b@iiitg.ac.in")

entry3 = Entry(width=33)
entry3.grid(row=3, column=1, sticky="W")

button1 = Button(text="Generate Password", command=generate_password)
button1.grid(row=3, column=2)

button2 = Button(text="Add", width=36, command=save)
button2.grid(row=4, column=1, columnspan=2, sticky="EW")

button3 = Button(text="Search", command=search, width=14)
button3.grid(row=1, column=2)

window.mainloop()
