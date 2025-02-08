from tkinter import *
from tkinter import messagebox

import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.fullmatch(pattern, email) is not None

root = Tk()
root.geometry("500x500")

email_entry=Entry(root)
password_entry=Entry(root, show="*")

def login():
    email=email_entry.get()
    password=password_entry.get()

    if email == "" or password == "":
        messagebox.showwarning("Required Fields", "Email and Password must not be empty")
    elif not is_valid_email(email):
        messagebox.showwarning("Email Warning", "Email must be in form of example@example.com")
    elif email != "test@test.com" or password != "1234":
        messagebox.showerror("Invalid Credentials", "Make sure you have tyoed correct data")
    else:
        messagebox.showinfo("Authenticated successfully", "Welcome to your dashboard")

    


Label(root, text="Email: ").grid(row=0, column=0, padx=5, pady=5)
email_entry.grid(row=0, column=1, padx=5, pady=5)
Label(root, text="Password: ").grid(row=1, column=0, padx=5, pady=5)
password_entry.grid(row=1, column=1, padx=5, pady=5)
Button(root, text="Login", padx=12, pady=4, command=login).grid(row=2, column=0, columnspan=2, padx=5, pady=5)
root.mainloop()