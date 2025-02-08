import os
from tkinter import *
from helpers.images import *
from helpers.commands import *

current_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(current_dir, "images")
# images_files = os.listdir(images_dir)
# img_path =
#

root = Tk()

viewed_image = Label(root)
image_handler = ImageHandler(images_dir, viewed_image)

frame = Frame(root)
prev_button = Button(frame, text="<<-", font="Arial 16", command=image_handler.prev)
next_button = Button(frame, text="->>", font="Arial 16", command=image_handler.next)
exit_button = Button(frame, text="Close Window", command=root.quit, font="Arial 16")

viewed_image.grid(row=0, column=0)
frame.grid(row=1, column=0)
prev_button.grid(row=0, column=0)
next_button.grid(row=0, column=2)
exit_button.grid(row=0, column=1, padx=12)

root.mainloop()
