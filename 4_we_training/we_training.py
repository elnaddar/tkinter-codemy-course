from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Simple Calculator")
root.configure(bg="lightblue")

# def click():
#     name= name_entry.get()
#     Label(root, text=f"Hello, {name}").pack()

root.geometry("500x400")
# Label(root, text="Hello World", font="Arial 16", fg="#000", bg="#edfa12").pack()
# Button(root, text="Click Me!", fg="#fff", bg="#000", command=click).pack()
# name_entry = Entry(root)
# name_entry.pack()

mcq = {}
for i in range(4):
    key = f"Ans {i+1}"
    mcq[key] = IntVar()
    row = i//2
    column = i%2
    Checkbutton(root, text=key, variable=mcq[key]).grid(row=row, column=column)

def get_answers():
    arr = [i.get() for i in mcq.values()]
    if any(arr):
        messagebox.showinfo("Submitted Successfully", "Your answers have been submitted successfully")
    else:
        messagebox.showwarning("Field Rquired", "You must choose an answere")

    

Button(root, text="Get Answers", command=get_answers).grid(row=2, column=0, columnspan=2)

root.mainloop()