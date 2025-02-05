from tkinter import *
import commands as cm
import helpers as hp

buttons = {}

root = Tk()

# ------ Define Widegts
e = Entry(root, width=35, borderwidth=5)

for number in range(1, 10):
    buttons[number] = hp.number_button(root, number, e, padx=40, pady=20)

buttons[0] = hp.number_button(root, 0, e, padx=40, pady=20)
buttons["+"] = Button(root, text="+", padx=40, pady=20, command=cm.add_command(e))
buttons["="] = Button(root, text="=", padx=88, pady=20, command=cm.equal_command(e))
buttons["clear"] = Button(root, text="clear", padx=75, pady=20, command=cm.clear_field(e))

# ------- The Grid -------
## --- Entry's Grid
e.grid(row=0, column=0, columnspan=3)
## --- Main Number's Grid
idx = 9
for row in range(3):
    for col in range(2, -1, -1):
        buttons[idx].grid(row=row+1, column=col)
        idx -= 1
## --- Rest Of Button's Grid
buttons[0].grid(row=4, column=0)
buttons["+"].grid(row=5, column=0)
buttons["="].grid(row=4, column=1, columnspan=2)
buttons["clear"].grid(row=5, column=1, columnspan=2)


root.mainloop()