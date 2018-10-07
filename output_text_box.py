"""
The module provides a OutputTextBox that is commonly used throughout the application.
The OutputTextBox is a tkinter Text and scrollbar with the same configuration for easy usage
"""

import Tkinter as tk


class OutputTextBox(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.output_text = tk.Text(self, state=tk.DISABLED)
        self.output_text.pack(side=tk.LEFT, expand=True, fill=tk.X)
        text_scroll_bar = tk.Scrollbar(self)
        text_scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

        # Link scroll bar to text. When u move the scrollbar, the text box will move
        text_scroll_bar.config(command=self.output_text.yview)
        # Link text to scrollbar. When you scroll in textbox it will also move the scrollbar
        self.output_text.config(yscrollcommand=text_scroll_bar.set)

    def set_output(self, text):
        """
        Set the content of the text box
        :param text:
        :return: None
        """
        self.clear_output()
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, text)
        self.output_text.config(state=tk.DISABLED)

    def clear_output(self):
        """
        Remove all content from the text box
        :return: None
        """
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete('1.0', tk.END)
        self.output_text.config(state=tk.DISABLED)
