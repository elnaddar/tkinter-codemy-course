import tkinter as tk

add = [0]

def insert_number(entry, number):
    return lambda: entry.insert(tk.END, number)

def clear_field(entry):
    def cb():
        entry.delete(0, tk.END)
        add[0] = 0
    return cb

def add_command(entry):
    def cb():
        number = int(entry.get())
        add[0] += number
        entry.delete(0, tk.END)
    return cb

def equal_command(entry):
    def cb():
        add_command(entry)()
        entry.insert(0, add[0])
        add[0] = 0
    return cb
