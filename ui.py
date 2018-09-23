from Tkinter import *
from tkFileDialog import askopenfilename
from os import getcwd
import basic_statistics
import data_holder

"""
Resources:
http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
"""

root = Tk()
root.title("This is Python Project 2k18")

content = Frame(root)
content.grid(column=0, row=0, sticky=(N, S, E, W))

# title START
title_frame = Frame(content, bd=10, bg="red")
title_frame.grid(row=0, column=0, columnspan=12, sticky=(W, E))
heading = Label(title_frame, text="Welcome to Python Project 2k18" ,font=("arial", 20,"bold"), fg="red")
heading.grid(row=0, column=1)
title_frame.grid_columnconfigure(0, weight=1) # fill up empty spaces to left of heading
title_frame.grid_columnconfigure(2, weight=1) # fill up empty spaces to right of heading
# title END
basic_stats_text = False

def prompt_sheet_location():
    current_working_directory = getcwd() # where the code is ran from
    filename = askopenfilename(initialdir = current_working_directory, title = "Select sheet",\
                                       filetypes = (("csv files","*.csv"), ("all files","*.*")))
    return filename
    # we can call the import csv here with the filename

def contractors_browse_clicked(e):
    path = prompt_sheet_location()
    if (path == ''): # don't do anything when path is empty
        return
    
    data_holder.load_contractor_list(path)

    if (data_holder.are_sheets_loaded()):
        stats = basic_statistics.generate_stats()
        basic_stats_text.config(state=NORMAL)
        basic_stats_text.insert(END, stats)
        basic_stats_text.config(state=DISABLED)

def procurements_browse_clicked(e):
    path = prompt_sheet_location()
    if (path == ''):
        return
    
    data_holder.load_procurement_list(path)
    
    if (data_holder.are_sheets_loaded()):
        stats = basic_statistics.generate_stats()
        basic_stats_text.config(state=NORMAL)
        basic_stats_text.insert(END, stats)
        basic_stats_text.config(state=DISABLED)
    
# contractors sheet input START
contractors_input_frame = Frame(content)
contractors_input_frame.grid(row=1, column=0, sticky=W)

contractors_input_label = Label(contractors_input_frame, text="Select your contractors sheet: ")
contractors_input_label.grid(row=0,column=0)

contractors_input_button = Button(contractors_input_frame, text="Browse")
contractors_input_button.grid(row=0,column=1)
contractors_input_button.bind('<Button-1>', contractors_browse_clicked)
# contractors sheet input END

# procurements sheet input START
gov_procurements_input_frame = Frame(content)
gov_procurements_input_frame.grid(row=2, column=0, sticky=W)

gov_procurements_input_label = Label(gov_procurements_input_frame, text="Select your procurements sheet: ")
gov_procurements_input_label.grid(row=0,column=0)

gov_procurements_input_button = Button(gov_procurements_input_frame, text="Browse")
gov_procurements_input_button.grid(row=0,column=1)
gov_procurements_input_button.bind('<Button-1>', procurements_browse_clicked)
# procurements sheet input END

# basic statistics START
basic_stats_label = Label(content, text="Basic Statistics")
basic_stats_label.grid(row=3, column=0, sticky=W)

basic_stats_text_container = Frame(content)
basic_stats_text_container.grid(row=4, column=0, sticky=W)

basic_stats_text = Text(basic_stats_text_container, state=DISABLED)
basic_stats_text.pack(side=LEFT)

basic_stats_text_scroll = Scrollbar(basic_stats_text_container)
basic_stats_text_scroll.pack(side=RIGHT, fill=Y)

"""
Link scroll bar to text. When u move the scrollbar, the text box will move
"""
basic_stats_text_scroll.config(command=basic_stats_text.yview)
"""
Link text to scrollbar. When you scroll in textbox it will also move the scrollbar
"""
basic_stats_text.config(yscrollcommand=basic_stats_text_scroll.set)
# basic statistics END

root.columnconfigure(0, weight=1) # set the window to fill up empty spaces (width)
root.rowconfigure(0, weight=1) # set the window to fill up empty spaces (height)
content.columnconfigure(0, weight=1)
root.update() # render the ui

def content_rendered(e):
    root.minsize(content.winfo_width(), content.winfo_height()) # set the minimum size of the window to content size

content.bind('<Configure>', content_rendered) # when window size changes. E.g On render

root.mainloop()
