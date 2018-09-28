from Tkinter import *
<<<<<<< Updated upstream
from main_page import MainPage
=======
from tkFileDialog import askopenfilename

import tkFileDialog as filedialog
from os import getcwd
import basic_statistics
import data_holder
from function_3 import function_3
from function_4 import function_4
from function_5 import function_5

>>>>>>> Stashed changes

"""
Resources:
http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
"""

root = Tk()
root.title("This is Python Project 2k18")

content = MainPage(root)
content.grid(column=0, row=0, sticky=(N, S, E, W))

<<<<<<< Updated upstream
=======
# title START
title_frame = Frame(content, bd=10, bg= "red")
title_frame.grid(row=0, column=0, columnspan=12, sticky=(W, E))
heading = Label(title_frame, text="Welcome to Python Project 2k18", font=("arial", 20, "bold"), fg="red")
heading.grid(row=0, column=1)
title_frame.grid_columnconfigure(0, weight=1)  # fill up empty spaces to left of heading
title_frame.grid_columnconfigure(2, weight=1)  # fill up empty spaces to right of heading
# title END
basic_stats_text = False


def prompt_sheet_location():
    current_working_directory = getcwd()  # where the code is ran from
    filename = askopenfilename(initialdir=current_working_directory, title="Select sheet", \
                               filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    return filename
    # we can call the import csv here with the filename


def contractors_browse_clicked(e):
    path = prompt_sheet_location()
    if (path == ''):  # don't do anything when path is empty
        return

    data_holder.load_contractor_list(path)

    if (data_holder.are_sheets_loaded()):
        # stats = basic_statistics.generate_stats()
        basic_stats_text.config(state=NORMAL)
        basic_stats_text.insert(END, stats)
        basic_stats_text.config(state=DISABLED)


def procurements_browse_clicked(e):
    path = prompt_sheet_location()
    if (path == ''):
        return

    data_holder.load_procurement_list(path)

    # if (data_holder.are_sheets_loaded()):
    #     # stats = basic_statistics.generate_stats()
    #     basic_stats_text.config(state=NORMAL)
    #     basic_stats_text.insert(END, stats)
    #     basic_stats_text.config(state=DISABLED)


def function3(e):
    basic_stats_text.config(state=NORMAL)
    basic_stats_text.delete('1.0', END)
    basic_stats_text.config(state=DISABLED)
    stats = function_3(True)
    # stats = basic_statistics.generate_stats()
    basic_stats_text.config(state=NORMAL)
    basic_stats_text.insert(END, stats)
    basic_stats_text.config(state=DISABLED)

def function4(e):
    basic_stats_text.config(state=NORMAL)
    basic_stats_text.delete(1.0,END)
    basic_stats_text.config(state=DISABLED)
    stats = function_4()
    # stats = basic_statistics.generate_stats()
    basic_stats_text.config(state=NORMAL)
    basic_stats_text.insert(END, stats)
    basic_stats_text.config(state=DISABLED)
def function5(e):
    basic_stats_text.config(state=NORMAL)
    basic_stats_text.delete('1.0', END)
    basic_stats_text.config(state=DISABLED)
    stats = function_5()
    # stats = basic_statistics.generate_stats()
    basic_stats_text.config(state=NORMAL)
    basic_stats_text.insert(END, stats)
    basic_stats_text.config(state=DISABLED)


# contractors sheet input START
contractors_input_frame = Frame(content)
contractors_input_frame.grid(row=1, column=0, sticky=W)

contractors_input_label = Label(contractors_input_frame, text="Select your contractors sheet: ")
contractors_input_label.grid(row=0, column=0)

contractors_input_button = Button(contractors_input_frame, text="Browse")
contractors_input_button.grid(row=0, column=1)
contractors_input_button.bind('<Button-1>', contractors_browse_clicked)
# contractors sheet input END

# procurements sheet input START
gov_procurements_input_frame = Frame(content)
gov_procurements_input_frame.grid(row=2, column=0, sticky=W)

gov_procurements_input_label = Label(gov_procurements_input_frame, text="Select your procurements sheet: ")
gov_procurements_input_label.grid(row=0, column=0)

gov_procurements_input_button = Button(gov_procurements_input_frame, text="Browse")
gov_procurements_input_button.grid(row=0, column=1)
gov_procurements_input_button.bind('<Button-1>', procurements_browse_clicked)
# procurements sheet input END

# Function 1

# Function 2 List down the total amount of procurement for each government sectors
# and allow users to order those sectors either by ascending order or descending order.
function2_input_frame = Frame(content)
function2_input_frame.grid(row=3, column=0, sticky=W)
#
# function2_input_label = Label(function2_input_frame, text="Function 2: ")
# function2_input_label.grid(row=0, column=0)

function2_input_button = Button(function2_input_frame, text="Function 2")
function2_input_button.grid(row=0, column=0)
function2_input_button.bind('<Button-1>',procurements_browse_clicked)


# Function 3 List down the  amount  of  the  procurement award  to  registered contractors and
# non-registered contractors, and top 5 contractors who were awarded by the most procurement



# function3_input_label = Label(function3_input_frame, text="Function 3: ")
# function3_input_label.grid(row=0, column=0)

function3_input_button = Button(function2_input_frame, text="Total Amount Of Procurement")
function3_input_button.grid(row=0, column=1)
function3_input_button.bind('<Button-1>', function3)

# Function 4 List down the awarded vendors which are the registered contractors.


#
# function4_input_label = Label(function4_input_frame, text="Function 4: ")
# function4_input_label.grid(row=0, column=0)

function4_input_button = Button(function2_input_frame, text="List Of Companies")
function4_input_button.grid(row=0, column=2)
function4_input_button.bind('<Button-1>', function4)
# Function 5 Identify  one  way  to  categorize  the  government  agency  and see
# # how much money the government spend on each category.These categories can be like IHL(institute of higher learning),transportation agency etc.

# function5_input_label = Label(function5_input_frame, text="Function 5: ")
# function5_input_label.grid(row=0, column=0)

function5_input_button = Button(function2_input_frame, text="Top 5 Companies")
function5_input_button.grid(row=0, column=3)
function5_input_button.bind('<Button-1>', function5)

# Function 6






# basic statistics START
basic_stats_label = Label(content, text="Basic Statistics")
basic_stats_label.grid(row=4, column=0, sticky=W)
#
basic_stats_text_container = Frame(content)
basic_stats_text_container.grid(row=5, column=0, sticky=W)

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

>>>>>>> Stashed changes
root.columnconfigure(0, weight=1)  # set the window to fill up empty spaces (width)
root.rowconfigure(0, weight=1)  # set the window to fill up empty spaces (height)
content.columnconfigure(0, weight=1)
root.update()  # render the ui


def content_rendered(e):
    root.minsize(e.width, e.height)  # set the minimum size of the window to content size


content.bind('<Configure>', content_rendered)  # when window size changes. E.g On render

root.mainloop()