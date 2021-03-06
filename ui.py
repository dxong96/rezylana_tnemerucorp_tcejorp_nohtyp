"""
The main module that the app starts at
The controls how to display the UI, like the size and etc
"""

from Tkinter import *
from main_page import MainPage


def main():
    root = Tk()
    root.title("This is Python Project 2k18")

    content = MainPage(root)
    content.grid(column=0, row=0, sticky=(N, S, E, W))

    root.columnconfigure(0, weight=1)  # set the window to fill up empty spaces (width)
    root.rowconfigure(0, weight=1)  # set the window to fill up empty spaces (height)
    content.columnconfigure(0, weight=1)
    root.update()  # render the ui

    def content_rendered(e):
        """
        Update the root window to resize to fit the render content
        :param e: event object
        :return: None
        """
        root.minsize(e.width, e.height)

    content.bind('<Configure>', content_rendered)  # when window size changes. E.g On render

    root.mainloop()


if __name__ == '__main__':
    main()
