"""
The UI for the first page containing the buttons to access different function
"""

import Tkinter as tk
import data_holder
import traceback
from tkFileDialog import askopenfilename
from os import getcwd

from nlp_dialog import ProcurementTopicsDialog
from workheads_page import WorkheadsPage
from output_text_box import OutputTextBox

import function_3
from function_4 import function_4
from function_5 import function_5
from function_6 import function_6
import function_2
from message_dialog import MessageDialog
import function_7
import function_8
import function_9
import function_11
import function_12


class MainPage(tk.Frame):
    """
    Starting of the main frame of the program
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(bg="black")

        # title START
        title_frame = tk.Frame(self, bd=10, bg="black")
        title_frame.grid(row=0, column=0, columnspan=12, sticky=(tk.W, tk.E))
        heading = tk.Label(title_frame, text="Government Procurement Analysis System", font=("arial", 20, "bold"), fg="black")
        heading.grid(row=0, column=1)
        title_frame.grid_columnconfigure(0, weight=1)  # fill up empty spaces to left of heading
        title_frame.grid_columnconfigure(2, weight=1)  # fill up empty spaces to right of heading
        # title END

        # contractors sheet input START
        contractors_input_frame = tk.Frame(self, bd=10, bg="black")
        contractors_input_frame.grid(row=1, column=0, sticky=tk.W)

        contractors_input_label = tk.Label(contractors_input_frame, text="Select your contractors sheet: ",
                                           bg="black", fg="white")
        contractors_input_label.grid(row=0, column=0)

        contractors_input_button = tk.Button(contractors_input_frame, text="Browse")
        contractors_input_button.grid(row=0, column=1)
        contractors_input_button.bind('<Button-1>', self.handle_sheet_loading(data_holder.load_contractor_list))
        # contractors sheet input END

        # procurements sheet input START
        gov_procurements_input_frame = tk.Frame(self, bd=10, bg="black")
        gov_procurements_input_frame.grid(row=2, column=0, sticky=tk.W)

        gov_procurements_input_label = tk.Label(gov_procurements_input_frame, text="Select your procurements sheet: ",
                                           bg="black", fg="white")
        gov_procurements_input_label.grid(row=0, column=0)

        gov_procurements_input_button = tk.Button(gov_procurements_input_frame, text="Browse")
        gov_procurements_input_button.grid(row=0, column=1)
        gov_procurements_input_button.bind('<Button-1>', self.handle_sheet_loading(data_holder.load_procurement_list))
        # procurements sheet input END

        # Function 1

        # Function 2 List down the total amount of procurement for each government sectors
        # and allow users to order those sectors either by ascending order or descending order.

        basic_function_row = tk.Frame(self, bd=10, bg="black")
        basic_function_row.grid(row=4, column=0, sticky=tk.W)

        function2_input_button = tk.Button(basic_function_row, text="Save as text file")
        function2_input_button.grid(row=0, column=0)
        function2_input_button.bind('<Button-1>', self.function_2_clicked)

        function3_input_button = tk.Menubutton(basic_function_row, text="Total awarded amount", relief=tk.RAISED)
        function3_input_button.grid(row=0, column=1)
        function3_input_button.menu = tk.Menu(function3_input_button)
        function3_input_button.menu.add_command(label='Ascending', command=self.function_3_clicked(True))
        function3_input_button.menu.add_command(label='Descending ', command=self.function_3_clicked(False))
        function3_input_button['menu'] = function3_input_button.menu

        # Function 4 List down the awarded vendors which are the registered contractors.

        function4_input_button = tk.Button(basic_function_row, text="Awarded Registered Contractors")
        function4_input_button.grid(row=0, column=2)
        function4_input_button.bind('<Button-1>', self.function_4_clicked)
        # Function 5 Identify  one  way  to  categorize  the  government  agency  and see
        # # how much money the government spend on each category.These categories can be like IHL(institute of higher learning),transportation agency etc.

        function5_input_button = tk.Button(basic_function_row, text="Top 5 contractors")
        function5_input_button.grid(row=0, column=3)
        function5_input_button.bind('<Button-1>', self.function_5_clicked)

        # Function 6
        function6_input_button = tk.Menubutton(basic_function_row, text="Total Expenditure", relief=tk.RAISED)
        function6_input_button.grid(row=0, column=4)
        # function6_input_button.bind('<Button-1>', self.function_6_clicked)

        function6_input_button.menu = tk.Menu(function6_input_button)
        function6_input_button.menu.add_command(label='1.Technology', command=self.function_6_clicked('Technology'))
        function6_input_button.menu.add_command(label='2.Transport', command=self.function_6_clicked('Transport'))
        function6_input_button.menu.add_command(label='3.Goveernment', command=self.function_6_clicked('Government'))
        function6_input_button.menu.add_command(label='4.Law', command=self.function_6_clicked('Law'))
        function6_input_button.menu.add_command(label='5.Public Service',
                                                command=self.function_6_clicked('Public Service'))
        function6_input_button.menu.add_command(label='6.Finance', command=self.function_6_clicked('Finance'))
        function6_input_button.menu.add_command(label='7.Clubs', command=self.function_6_clicked('Clubs'))
        function6_input_button.menu.add_command(label='8.Health', command=self.function_6_clicked('Health'))
        function6_input_button.menu.add_command(label='9.Housing', command=self.function_6_clicked('Housing'))
        function6_input_button.menu.add_command(label='10.Maritime', command=self.function_6_clicked('Maritime'))
        function6_input_button.menu.add_command(label='11.Eduction', command=self.function_6_clicked('Education'))
        function6_input_button.menu.add_command(label='12.Defence', command=self.function_6_clicked('Defence'))

        function6_input_button['menu'] = function6_input_button.menu

        advance_functions_label = self.create_title_label("Advance functions")
        advance_functions_label.grid(row=5, sticky=tk.W)
        advance_functions_row = tk.Frame(self)
        advance_functions_row.grid(row=6, sticky=tk.W)

        # Function 7
        function7_input_button = tk.Menubutton(advance_functions_row, text="Average spending by Gov.Agency",
                                               relief=tk.RAISED, direction=tk.RIGHT)
        function7_input_button.grid(sticky=(tk.W, tk.E), row=0)
        # function7_input_button.bind('<Button-1>', self.function_7_clicked)

        function7_input_button.menu = tk.Menu(function7_input_button)
        function7_input_button.menu.add_command(label='Ascending', command=self.function_7_clicked(True))
        function7_input_button.menu.add_command(label='Descending', command=self.function_7_clicked(False))
        function7_input_button['menu'] = function7_input_button.menu

        # Function 8
        function8_input_button = tk.Menubutton(advance_functions_row, text="Max procurement by Gov.Agency",
                                               relief=tk.RAISED, direction=tk.RIGHT)
        function8_input_button.grid(sticky=(tk.W, tk.E), row=1)
        # function8_input_button.bind('<Button-1>', self.function_8_clicked)

        function8_input_button.menu = tk.Menu(function8_input_button)
        function8_input_button.menu.add_command(label='Ascending', command=self.function_8_clicked(True))
        function8_input_button.menu.add_command(label='Descending', command=self.function_8_clicked(False))
        function8_input_button['menu'] = function8_input_button.menu

        # Function 9
        function9_input_button = tk.Menubutton(advance_functions_row, text="Min procurement by Gov.Agency",
                                               relief=tk.RAISED, direction=tk.RIGHT)
        function9_input_button.grid(sticky=(tk.W, tk.E), row=2)
        # function9_input_button.bind('<Button-1>', self.function_9_clicked)

        function9_input_button.menu = tk.Menu(function9_input_button)
        function9_input_button.menu.add_command(label='Ascending', command=self.function_9_clicked(True))
        function9_input_button.menu.add_command(label='Descending', command=self.function_9_clicked(False))
        function9_input_button['menu'] = function9_input_button.menu

        # Function 10
        function10_input_button = tk.Button(advance_functions_row, text="Contractor Workhead graph and browser")
        function10_input_button.grid(sticky=(tk.W, tk.E), row=3)
        function10_input_button.bind('<Button-1>', self.function_10_clicked)

        # Function 11
        function11_input_button = tk.Menubutton(advance_functions_row, text="Contractor with expired Workhead",
                                                relief=tk.RAISED, direction=tk.RIGHT)
        function11_input_button.grid(sticky=(tk.W, tk.E), row=4)
        # function11_input_button.bind('<Button-1>', self.function_11_clicked)

        function11_input_button.menu = tk.Menu(function11_input_button)
        function11_input_button.menu.add_command(label='Ascending', command=self.function_11_clicked(True))
        function11_input_button.menu.add_command(label='Descending', command=self.function_11_clicked(False))
        function11_input_button['menu'] = function11_input_button.menu

        # Function 12
        function12_input_button = tk.Menubutton(advance_functions_row, text="Contractor with unexpired Workhead",
                                                relief=tk.RAISED, direction=tk.RIGHT)
        function12_input_button.grid(sticky=(tk.W, tk.E), row=5)

        function12_input_button.menu = tk.Menu(function12_input_button)
        function12_input_button.menu.add_command(label='Ascending', command=self.function_12_clicked(True))
        function12_input_button.menu.add_command(label='Descending', command=self.function_12_clicked(False))
        function12_input_button['menu'] = function12_input_button.menu

        lda_function_button = tk.Button(advance_functions_row, text="Procurements grouped using LDA model")
        lda_function_button.grid(sticky=(tk.W, tk.E), row=6)
        lda_function_button.bind('<Button-1>', self.lda_function_clicked)

        basic_stats_label = self.create_title_label("\nINFORMATION:")
        basic_stats_label.grid(row=7, column=0, sticky=tk.W)
        self.output_tb = OutputTextBox(self)
        self.output_tb.grid(row=8, column=0, sticky=(tk.W, tk.E))
        self.output_tb.output_text.configure(height=15, bd=10, bg="white", fg="black")

        search_input_frame = tk.Frame(self)
        search_input_frame.grid(row=9, column=0, sticky=tk.W)

        data_holder.load_contractor_registry()

    @staticmethod
    def prompt_sheet_location():
        """
        Ask the user to select which sheet to use
        :return: String, path of excel sheet
        """
        current_working_directory = getcwd()  # where the code is ran from
        filename = askopenfilename(initialdir=current_working_directory, title="Select sheet",
                                   filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        return filename

    def create_title_label(self, text):
        """ A helper method to create a 'Title' Label with the 'Title' configuration '"""
        return tk.Label(self, text=text, font='Helvetica 10 bold', bg="black", fg="white")

    # Click listeners START
    def handle_sheet_loading(self, func):
        """
        Contains the logic to ask and call the function to handle the path
        :param func: the function that handles path
        :return: a function object that handles the load button click
        """

        def inner_func(e):
            path = self.prompt_sheet_location()
            if path == '':
                return

            try:
                func(path)
            except:
                traceback.print_exc()
                MessageDialog(self, "Please select the correct sheet")

        return inner_func

    def function_2_clicked(self, e):
        """
        Check if sheets are loaded and perform function 2
        """
        if not data_holder.are_sheets_loaded():
            MessageDialog(self, "Load contractors and procurements first!")
            return
        function_2.save()

    def function_3_clicked(self, asc):
        """
        Check if sheets are loaded and perform function 3
        """

        def wrapper():
            if not data_holder.are_sheets_loaded():
                MessageDialog(self, "Load contractors and procurements first!")
                return
            function_3.procurement_dictionary1()
            function_3.total_procurement_dictionary1()
            self.output_tb.set_output(function_3.sorted_total_procurement_dictionary1(asc))

        return wrapper

    def function_4_clicked(self, e):
        """
        Check if sheets are loaded and perform function 4
        """
        if not data_holder.are_sheets_loaded():
            MessageDialog(self, "Load contractors and procurements first!")
            return
        self.output_tb.set_output(function_4())

    def function_5_clicked(self, e):
        """
        Check if sheets are loaded and perform function 5
        """
        if not data_holder.are_sheets_loaded():
            MessageDialog(self, "Load contractors and procurements first!")
            return
        self.output_tb.set_output(function_5())

    def function_6_clicked(self, category):
        """
        Check if sheets are loaded and perform function 6 with the selected category
        """

        def wrapper():
            if not data_holder.are_sheets_loaded():
                MessageDialog(self, "Load contractors and procurements first!")
                return
            self.output_tb.set_output(function_6(category))

        return wrapper

    def function_7_clicked(self, asc):
        """
        Check if sheets are loaded and perform function 7
        """

        def wrapper():
            if not data_holder.are_sheets_loaded():
                MessageDialog(self, "Load contractors and procurements first!")
                return

            self.output_tb.set_output(function_7.agency_no())
            self.output_tb.set_output(function_7.average_procurement1())
            self.output_tb.set_output(function_7.sorted_average_procurement(asc))

        return wrapper

    def function_8_clicked(self, asc):
        """
        Check if sheets are loaded and perform function 8
        """

        def wrapper():
            if not data_holder.are_sheets_loaded():
                MessageDialog(self, "Load contractors and procurements first!")
                return
            self.output_tb.set_output(function_8.agency_max_procurement())
            self.output_tb.set_output(function_8.sorted_max_procurement(asc))

        return wrapper

    def function_9_clicked(self, asc):
        """
        Check if sheets are loaded and perform function 9
        """

        def wrapper():
            if not data_holder.are_sheets_loaded():
                MessageDialog(self, "Load contractors and procurements first!")
                return

            self.output_tb.set_output(function_9.agency_min_procurement())
            self.output_tb.set_output(function_9.sorted_min_procurement(asc))

        return wrapper

    def function_10_clicked(self, e):
        """
        Check if sheets are loaded and show the workheads pop up window
        """
        if not data_holder.are_sheets_loaded():
            MessageDialog(self, "Load contractors and procurements first!")
            return

        WorkheadsPage(self)

    def function_11_clicked(self, asc):
        """
        Check if sheets are loaded and perform function 11
        """

        def wrapper():
            if not data_holder.are_sheets_loaded():
                MessageDialog(self, "Load contractors and procurements first!")
                return

            self.output_tb.set_output(function_11.sort_date_time1())
            self.output_tb.set_output(function_11.sort_by_expired_date1(asc))

        return wrapper

    def function_12_clicked(self, asc):
        """
        Check if sheets are loaded and perform function 12
        """

        def wrapper():
            if not data_holder.are_sheets_loaded():
                MessageDialog(self, "Load contractors and procurements first!")
                return

            self.output_tb.set_output(function_12.sort_by_nonexpired_date1(asc))

        return wrapper

    def lda_function_clicked(self, e):
        """
        Check if sheets are loaded and show procurements grouped by topic.
        The topics are created using natural language processing, LDA model
        """

        if not data_holder.are_sheets_loaded():
            MessageDialog(self, "Load contractors and procurements first!")
            return
        ProcurementTopicsDialog(self)

    # Click listeners END
