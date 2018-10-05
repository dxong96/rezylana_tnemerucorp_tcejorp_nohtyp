import Tkinter as tk

import data_holder
import workhead
import function_10
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from output_text_box import OutputTextBox

class WorkheadsPage(tk.Toplevel):
    '''
    List states 0 or 1
    'wc' state means listbox shows workhead categories
    'w' state means listbox shows workhead
    'WORKHEAD' state shows the contractor in the given workhead
    '''
    list_state = 'wc'
    canvas_container = None
    workhead_cat_graph_data = None
    workhead_graph_data = {}

    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.minsize(500, 400)
        self.title("Workheads")

        self.name_to_contractors = data_holder.create_dict_for_list(data_holder.contractors, 'company_name')

        self.listbox = tk.Listbox(self, width=30, selectmode=tk.SINGLE)
        self.listbox.bind("<Double-Button-1>", self.listbox_item_clicked)
        self.listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.set_workhead_categories_in_listbox()

        self.output_tb = OutputTextBox(self)
        self.output_tb.output_text.config(height=10)
        self.output_tb.grid(row=0, column=1, sticky=(tk.W, tk.E))
        self.grab_set()

    def show_workhead_categories_piechart(self):
        if (self.workhead_cat_graph_data == None):
            workhead_contractor_count = {}
            for wh in workhead.WORKHEAD_CATEGORIES:
                workhead_contractor_count.setdefault(wh, 0)
                for contractor in data_holder.contractors:
                    if contractor.is_in_workhead_category(wh):
                        workhead_contractor_count[wh] += 1

            self.workhead_cat_graph_data = (map(workhead.WORKHEAD_CATEGORIES.get, workhead_contractor_count.keys()),
                                            workhead_contractor_count.values())

        labels = self.workhead_cat_graph_data[0]
        sizes = self.workhead_cat_graph_data[1]
        self.show_graph('Workhead categories', labels, sizes)

    def show_workhead_for_categories_piechart(self, workhead_category):
        if workhead_category not in self.workhead_graph_data:
            workheads = function_10.get_workheads_for_category(workhead_category)
            workhead_contractor_counts = []
            for wh in workheads:
                number_of_contractors = len(function_10.get_contractors_by_workhead(wh))
                workhead_contractor_counts.append(number_of_contractors)

            self.workhead_graph_data[workhead_category] = (workheads, workhead_contractor_counts)

        labels = self.workhead_graph_data[workhead_category][0]
        values = self.workhead_graph_data[workhead_category][1]
        self.show_graph('Workheads under %s' % workhead.WORKHEAD_CATEGORIES[workhead_category],
                        labels, values)


    def show_graph(self, title, labels, sizes):
        ax1 = plt.subplot()
        ax1.clear()
        ax1.set_title(title)
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.figure.set_size_inches(8, 4)

        canvas = FigureCanvasTkAgg(ax1.figure, master=self)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, columnspan=2)

    def set_workhead_categories_in_listbox(self):
        # clear all the items in the list
        self.listbox.delete(0, self.listbox.size())
        self.listbox.insert(tk.END, *workhead.WORKHEAD_CATEGORIES.values())
        self.list_state = 'wc'
        self.show_workhead_categories_piechart()

    def set_workheads_in_listbox(self, workhead_category):
        self.listbox.delete(0, self.listbox.size())
        self.listbox.insert(0, 'back')
        self.listbox.insert(tk.END, *function_10.get_workheads_for_category(workhead_category))
        self.output_tb.set_output(workhead.WORKHEAD_CATEGORIES[workhead_category])
        self.show_workhead_for_categories_piechart(workhead_category)
        self.list_state = 'w'

    def set_contractors_in_listbox(self, wh):
        self.listbox.delete(0, self.listbox.size())
        self.listbox.insert(0, 'back')
        contractor_names = map(lambda c: c.company_name, function_10.get_contractors_by_workhead(wh))
        self.listbox.insert(tk.END, *contractor_names)
        self.output_tb.set_output(workhead.workhead_display_text(wh))
        self.list_state = wh

    def show_contractor_info(self, contractor_name):
        contractor = self.name_to_contractors[contractor_name][0]
        text_to_display = contractor.display_text()
        self.output_tb.set_output(text_to_display)

    def listbox_item_clicked(self, e):
        index = self.listbox.nearest(e.y)
        item_title = self.listbox.get(index)
        print item_title

        if self.list_state == 'wc':
            # get the workhead category by index
            workhead_category = workhead.WORKHEAD_CATEGORIES.keys()[index]
            self.set_workheads_in_listbox(workhead_category)
        elif self.list_state == 'w':
            if item_title == "back":
                self.set_workhead_categories_in_listbox()
            else:
                self.set_contractors_in_listbox(item_title)
        else:
            if item_title == "back":
                # the list_state now should be a workhead
                # so we can the category by getting the first 2 letters
                workhead_category = self.list_state[0:2]
                self.set_workheads_in_listbox(workhead_category)
            else:
                self.show_contractor_info(item_title)
