import Tkinter as tk
import data_holder
import traceback
from tkFileDialog import askopenfilename
from os import getcwd


from function_3 import procurement_dictionary1,total_procurement_dictionary1,sorted_total_procurement_dictionary1
from function_4 import function_4
from function_5 import function_5
import function_2
from message_dialog import MessageDialog
from function_7 import procurement_dictionary1,total_procurement_dictionary1,agency_no,average_procurement1,sorted_average_procurement
from function_8 import procurement_dictionary1,total_procurement_dictionary1,agency_max_procurement,sorted_max_procurement
from function_9 import procurement_dictionary1,total_procurement_dictionary1,agency_min_procurement,sorted_min_procurement
from function_10 import contractor_workhead_grade
from function_11 import sort_date_time1,sort_by_expired_date1

class MainPage(tk.Frame):
    output_text = False

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # title START
        title_frame = tk.Frame(self, bd=10, bg="red")
        title_frame.grid(row=0, column=0, columnspan=12, sticky=(tk.W, tk.E))
        heading = tk.Label(title_frame, text="Welcome to Python Project 2k18", font=("arial", 20, "bold"), fg="black")
        heading.grid(row=0, column=1)
        title_frame.grid_columnconfigure(0, weight=1)  # fill up empty spaces to left of heading
        title_frame.grid_columnconfigure(2, weight=1)  # fill up empty spaces to right of heading
        # title END
        basic_stats_text = False

        # contractors sheet input START
        contractors_input_frame = tk.Frame(self)
        contractors_input_frame.grid(row=1, column=0, sticky=tk.W)

        contractors_input_label = tk.Label(contractors_input_frame, text="Select your contractors sheet: ")
        contractors_input_label.grid(row=0, column=0)

        contractors_input_button = tk.Button(contractors_input_frame, text="Browse")
        contractors_input_button.grid(row=0, column=1)
        contractors_input_button.bind('<Button-1>', self.handle_sheet_loading(data_holder.load_contractor_list))
        # contractors sheet input END

        # procurements sheet input START
        gov_procurements_input_frame = tk.Frame(self)
        gov_procurements_input_frame.grid(row=2, column=0, sticky=tk.W)

        gov_procurements_input_label = tk.Label(gov_procurements_input_frame, text="Select your procurements sheet: ")
        gov_procurements_input_label.grid(row=0, column=0)

        gov_procurements_input_button = tk.Button(gov_procurements_input_frame, text="Browse")
        gov_procurements_input_button.grid(row=0, column=1)
        gov_procurements_input_button.bind('<Button-1>', self.handle_sheet_loading(data_holder.load_procurement_list))
        # procurements sheet input END

        # Function 1

        # Function 2 List down the total amount of procurement for each government sectors
        # and allow users to order those sectors either by ascending order or descending order.
        function_input_frame = tk.Frame(self)
        function_input_frame.grid(row=3, column=0, sticky=tk.W)
        #
        # function2_input_label = tk.Label(function_input_frame, text="Function 2: ")
        # function2_input_label.grid(row=0, column=0)

        function2_input_button = tk.Button(function_input_frame, text="Function 2")
        function2_input_button.grid(row=0, column=0)
        function2_input_button.bind('<Button-1>', self.function_2_clicked)

        # Function 3 List down the  amount  of  the  procurement award  to  registered contractors and
        # non-registered contractors, and top 5 contractors who were awarded by the most procurement

        # function3_input_label = tk.Label(function3_input_frame, text="Function 3: ")
        # function3_input_label.grid(row=0, column=0)

        function3_input_button = tk.Menubutton(function_input_frame, text="Function 3", relief=tk.RAISED)
        function3_input_button.grid(row=0, column=1)
        # function3_input_button.bind('<Button-1>', self.function_3_clicked)

        function3_input_button.menu = tk.Menu(function3_input_button)
        function3_input_button.menu.add_command(label='Ascending', command=self.function_3_clicked(True))
        function3_input_button.menu.add_command(label='Descending ', command=self.function_3_clicked(False))
        function3_input_button['menu'] = function3_input_button.menu

        # Function 4 List down the awarded vendors which are the registered contractors.

        #
        # function4_input_label = tk.Label(function4_input_frame, text="Function 4: ")
        # function4_input_label.grid(row=0, column=0)

        function4_input_button = tk.Button(function_input_frame, text="Function 4")
        function4_input_button.grid(row=0, column=2)
        function4_input_button.bind('<Button-1>', self.function_4_clicked)
        # Function 5 Identify  one  way  to  categorize  the  government  agency  and see
        # # how much money the government spend on each category.These categories can be like IHL(institute of higher learning),transportation agency etc.

        # function5_input_label = tk.Label(function5_input_frame, text="Function 5: ")
        # function5_input_label.grid(row=0, column=0)

        function5_input_button = tk.Button(function_input_frame, text="Function 5")
        function5_input_button.grid(row=0, column=3)
        function5_input_button.bind('<Button-1>', self.function_5_clicked)

        # Function 6
        function5_input_button = tk.Button(function_input_frame, text="Function 6")
        function5_input_button.grid(row=0, column=4)
        function5_input_button.bind('<Button-1>', self.function_6_clicked)
        
         #Function 7
        function7_input_button = tk.Menubutton(function_input_frame, text="Function 7", relief=tk.RAISED)
        function7_input_button.grid(row=0, column=5)
        # function7_input_button.bind('<Button-1>', self.function_7_clicked)

        function7_input_button.menu = tk.Menu(function7_input_button)
        function7_input_button.menu.add_command(label='Ascending', command=self.function_7_clicked(True))
        function7_input_button.menu.add_command(label='Descending', command=self.function_7_clicked(False))
        function7_input_button['menu'] = function7_input_button.menu

        # Function 8
        function8_input_button = tk.Menubutton(function_input_frame, text="Function 8", relief=tk.RAISED)
        function8_input_button.grid(row=0, column=6)
        # function8_input_button.bind('<Button-1>', self.function_8_clicked)

        function8_input_button.menu = tk.Menu(function8_input_button)
        function8_input_button.menu.add_command(label='Ascending', command=self.function_8_clicked(True))
        function8_input_button.menu.add_command(label='Descending', command=self.function_8_clicked(False))
        function8_input_button['menu'] = function8_input_button.menu

        # Function 9
        function9_input_button = tk.Menubutton(function_input_frame, text="Function 9", relief=tk.RAISED)
        function9_input_button.grid(row=0, column=7)
        # function9_input_button.bind('<Button-1>', self.function_9_clicked)

        function9_input_button.menu = tk.Menu(function9_input_button)
        function9_input_button.menu.add_command(label='Ascending', command=self.function_9_clicked(True))
        function9_input_button.menu.add_command(label='Descending', command=self.function_9_clicked(False))
        function9_input_button['menu'] = function9_input_button.menu

        # Function 10
        function10_input_button = tk.Menubutton(function_input_frame, text="Function 10", relief=tk.RAISED)
        function10_input_button.grid(row=0, column=8)
        # function10_input_button.bind('<Button-1>', self.function_10_clicked)

        function10_input_button.menu = tk.Menu(function10_input_button)
        function10_input_button.menu.add_command(label='Ascending', command=self.function_10_clicked(True))
        function10_input_button.menu.add_command(label='Descending', command=self.function_10_clicked(False))
        function10_input_button['menu'] = function10_input_button.menu

        # Function 11
        function11_input_button = tk.Menubutton(function_input_frame, text="Function 11", relief=tk.RAISED)
        function11_input_button.grid(row=0, column=9)
        # function11_input_button.bind('<Button-1>', self.function_11_clicked)

        function11_input_button.menu = tk.Menu(function11_input_button)
        function11_input_button.menu.add_command(label='Ascending', command=self.function_11_clicked(True))
        function11_input_button.menu.add_command(label='Descending', command=self.function_11_clicked(False))
        function11_input_button['menu'] = function11_input_button.menu


        # basic statistics START
        basic_stats_label = tk.Label(self, text="Basic Statistics")
        basic_stats_label.grid(row=4, column=0, sticky=tk.W)

        basic_stats_text_container = tk.Frame(self)
        basic_stats_text_container.grid(row=5, column=0, sticky=(tk.W, tk.E))

        basic_stats_text = tk.Text(basic_stats_text_container, state=tk.DISABLED)
        basic_stats_text.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.output_text = basic_stats_text

        basic_stats_text_scroll = tk.Scrollbar(basic_stats_text_container)
        basic_stats_text_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        """
        Link scroll bar to text. When u move the scrollbar, the text box will move
        """
        basic_stats_text_scroll.config(command=basic_stats_text.yview)
        """
        Link text to scrollbar. When you scroll in textbox it will also move the scrollbar
        """
        basic_stats_text.config(yscrollcommand=basic_stats_text_scroll.set)
        # basic statistics END

    def prompt_sheet_location(self):
        current_working_directory = getcwd()  # where the code is ran from
        filename = askopenfilename(initialdir=current_working_directory, title="Select sheet",
                                   filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        return filename
        # we can call the import csv here with the filename

    def set_output(self, text):
        self.clear_output()
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, text)
        self.output_text.config(state=tk.DISABLED)

    def clear_output(self):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete('1.0', tk.END)
        self.output_text.config(state=tk.DISABLED)

    ''' Click listeners START '''

    def handle_sheet_loading(self, func):
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
        function_2.createFolder()
        function_2.writetxt()
        function_2.txtdetails()
        if not data_holder.are_sheets_loaded():
            MessageDialog(self, "Load contractors and procurements first!")
            return
        # self.set_output(function_2())

    def function_3_clicked(self, asc):
        def wrapper():
            if not data_holder.are_sheets_loaded():
                MessageDialog(self, "Load contractors and procurements first!")
                return

            self.set_output(procurement_dictionary1())
            self.set_output(total_procurement_dictionary1())
            self.set_output(sorted_total_procurement_dictionary1(asc))
        return wrapper


    def function_4_clicked(self, e):
        if not data_holder.are_sheets_loaded():
            MessageDialog(self, "Load contractors and procurements first!")
            return
        self.set_output(function_4())

    def function_5_clicked(self, e):
        if not data_holder.are_sheets_loaded():
            MessageDialog(self, "Load contractors and procurements first!")
            return
        self.set_output(function_5())

    def function_7_clicked(self, asc):
        def wrapper():
            if not data_holder.are_sheets_loaded():
                MessageDialog(self, "Load contractors and procurements first!")
                return

            self.set_output(function_3(asc))
        return wrapper

    def function_6_clicked(self, e):
        if not data_holder.are_sheets_loaded():
            MessageDialog(self, "Load contractors and procurements first!")
            return

        self.set_output(function_5())
        
    def function_7_clicked(self, asc):
        def wrapper():
            if not data_holder.are_sheets_loaded():
                MessageDialog(self, "Load contractors and procurements first!")
                return

            self.set_output(procurement_dictionary1())
            self.set_output(total_procurement_dictionary1())
            self.set_output(agency_no())
            self.set_output(average_procurement1())
            self.set_output(sorted_average_procurement(asc))
        return wrapper

    def function_8_clicked(self, asc):
        def wrapper():
            if not data_holder.are_sheets_loaded():
                MessageDialog(self, "Load contractors and procurements first!")
                return

            self.set_output(procurement_dictionary1())
            self.set_output(total_procurement_dictionary1())
            self.set_output(agency_max_procurement())
            self.set_output(sorted_max_procurement(asc))
        return wrapper

    def function_9_clicked(self, asc):
        def wrapper():
            if not data_holder.are_sheets_loaded():
                MessageDialog(self, "Load contractors and procurements first!")
                return

            self.set_output(procurement_dictionary1())
            self.set_output(total_procurement_dictionary1())
            self.set_output(agency_min_procurement())
            self.set_output(sorted_min_procurement(asc))
        return wrapper

    def function_10_clicked(self, asc):
        def wrapper():
            if not data_holder.are_sheets_loaded():
                MessageDialog(self, "Load contractors and procurements first!")
                return

            self.set_output(contractor_workhead_grade())
        return wrapper

    def function_11_clicked(self, asc):
        def wrapper():
            if not data_holder.are_sheets_loaded():
                MessageDialog(self, "Load contractors and procurements first!")
                return

            self.set_output(sort_date_time1())
            self.set_output(sort_by_expired_date1(True))
        return wrapper

    ''' Click listeners END '''
