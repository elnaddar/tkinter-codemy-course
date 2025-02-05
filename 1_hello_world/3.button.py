from tkinter import *

root = Tk()

is_button_clicked = False
def click_button():
    global is_button_clicked

    if not is_button_clicked:
        is_button_clicked = True
        Label(root, text="Look you've clicked me!")\
            .pack()

Button(root, text="Click Me!", padx=50,
             command=click_button, bg="#00f", fg="white")\
            .pack()
Button(root, text="Don't Click Me!", pady=50, state=DISABLED)\
            .pack()

root.mainloop()