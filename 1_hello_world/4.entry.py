from tkinter import *

root = Tk()

actions = set()

e = Entry(root, width=50);
e.pack()
e.insert(0, "Your Name...")

def say_hello():
    if "hello" not in actions:
        actions.add("hello")
        hello = f"Hello, {e.get()}"
        Label(root, text=hello).pack()

Button(root, text="Click Me", command=say_hello).pack()

root.mainloop();