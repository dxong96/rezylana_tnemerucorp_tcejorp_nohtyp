"""
A simple tkinter top level that is made to show messages
"""

import Tkinter as tk


class MessageDialog(tk.Toplevel):
    def __init__(self, parent, message):
        tk.Toplevel.__init__(self, parent)
        self.minsize(300, 100)
        self.title("New Message!")

        # the message to show is inserted into this widget
        msg = tk.Message(self, text=message, width=300)
        msg.pack(fill=tk.X, expand=True)

        button = tk.Button(self, text="Dismiss", command=self.close)
        button.pack()
        # pause the ui
        self.grab_set()

    def close(self):
        # resume the ui on close
        self.grab_release()
        self.destroy()
