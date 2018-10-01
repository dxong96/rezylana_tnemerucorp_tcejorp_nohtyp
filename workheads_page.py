import Tkinter as tk

import data_holder
import workhead
import function_10


class WorkheadsPage(tk.Toplevel):
    '''
    List states 0 or 1
    'wc' state means listbox shows workhead categories
    'w' state means listbox shows workhead
    'WORKHEAD' state shows the contractor in the given workhead
    '''
    list_state = 'wc'
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.minsize(500, 400)
        self.title("Workheads")

        self.name_to_contractors = data_holder.create_dict_for_list(data_holder.contractors, 'company_name')

        self.listbox = tk.Listbox(self, width=30, selectmode=tk.SINGLE)
        self.listbox.bind("<Double-Button-1>", self.listbox_item_clicked)
        self.listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.set_workhead_categories_in_listbox()

        # output text START
        basic_stats_text_container = tk.Frame(self)
        basic_stats_text_container.grid(row=0, column=1, sticky=(tk.W, tk.E))

        basic_stats_text = tk.Text(basic_stats_text_container, state=tk.DISABLED)
        basic_stats_text.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.output_text = basic_stats_text

        basic_stats_text_scroll = tk.Scrollbar(basic_stats_text_container)
        basic_stats_text_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        basic_stats_text_scroll.config(command=basic_stats_text.yview)
        basic_stats_text.config(yscrollcommand=basic_stats_text_scroll.set)
        # output text END

    def set_workhead_categories_in_listbox(self):
        # clear all the items in the list
        self.listbox.delete(0, self.listbox.size())
        self.listbox.insert(tk.END, *workhead.WORKHEAD_CATEGORIES.values())
        self.list_state = 'wc'

    def set_workheads_in_listbox(self, workhead_category):
        self.listbox.delete(0, self.listbox.size())
        self.listbox.insert(0, 'back')
        self.listbox.insert(tk.END, *function_10.get_workheads_for_category(workhead_category))
        self.set_output(workhead.WORKHEAD_CATEGORIES[workhead_category])
        self.list_state = 'w'

    def set_contractors_in_listbox(self, wh):
        self.listbox.delete(0, self.listbox.size())
        self.listbox.insert(0, 'back')
        contractor_names = map(lambda c: c.company_name, function_10.get_contractors_by_workhead(wh))
        self.listbox.insert(tk.END, *contractor_names)
        self.set_output(workhead.workhead_display_text(wh))
        self.list_state = wh

    def show_contractor_info(self, contractor_name):
        contractor = self.name_to_contractors[contractor_name][0]
        text_to_display = contractor.display_text()
        self.set_output(text_to_display)

    def set_output(self, text):
        self.clear_output()
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, text)
        self.output_text.config(state=tk.DISABLED)

    def clear_output(self):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete('1.0', tk.END)
        self.output_text.config(state=tk.DISABLED)

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
