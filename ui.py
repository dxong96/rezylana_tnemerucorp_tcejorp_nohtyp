from Tkinter import *
from main_page import MainPage

"""
Resources:
http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
"""

root = Tk()
root.title("This is Python Project 2k18")

content = MainPage(root)
content.grid(column=0, row=0, sticky=(N, S, E, W))

root.columnconfigure(0, weight=1)  # set the window to fill up empty spaces (width)
root.rowconfigure(0, weight=1)  # set the window to fill up empty spaces (height)
content.columnconfigure(0, weight=1)
root.update()  # render the ui


def content_rendered(e):
    root.minsize(e.width, e.height)  # set the minimum size of the window to content size


content.bind('<Configure>', content_rendered)  # when window size changes. E.g On render

root.mainloop()
