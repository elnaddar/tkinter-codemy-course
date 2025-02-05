import tkinter as tk
import commands as cm


def number_button(frame, number, entry=None, **kargs):
    return tk.Button(frame, text=number,
                     command=cm.insert_number(entry, number), **kargs)
