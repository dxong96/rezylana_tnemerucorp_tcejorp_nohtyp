"""
The TopLevel dialog for procurements grouped by topic
"""

import Tkinter as tk
import ttk

from output_text_box import OutputTextBox
from topic_modeling import TopicModeller
import Queue
import threading


class ProcurementTopicsDialog(tk.Toplevel):
    complete = False
    queue = Queue.Queue()

    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.topic_modeller = TopicModeller()
        self.minsize(300, 100)
        self.title("Procurements by topics...")

        self.progress_bar = ttk.Progressbar(self, orient='horizontal', mode='indeterminate')
        self.progress_bar.grid(sticky=(tk.W, tk.E), row=0)
        self.progress_bar.start(50)

        self.output_tb = OutputTextBox(self)
        self.output_tb.grid(sticky=(tk.W, tk.E), row=1)
        self.output_tb.output_text.configure(height=15)

        self.retrain_button = tk.Button(self, text="Relaod the topics (takes awhile)")
        self.retrain_button.grid(sticky=tk.W, row=2)
        self.retrain_button.bind('<Button-1>', self.retrain_button_clicked)

        self.grab_set()
        self.queue_task()

    def queue_task(self):
        """
        Start loading procurement and topics in another Thread
        :return: None
        """
        self.queue = Queue.Queue()
        ThreadedTask(self.queue, self.topic_modeller).start()
        self.master.after(100, self.process_queue)
        self.retrain_button.configure(state=tk.DISABLED)

    def retrain_button_clicked(self, e):
        """
        Delete the cache file start the task to retrain the LDA model
        :param e: tkinter event object
        :return: None
        """
        button_state = self.retrain_button['state']
        if button_state == tk.DISABLED:
            return

        self.topic_modeller.clear_cache_file()
        self.progress_bar.grid()
        self.output_tb.clear_output()
        self.queue_task()

    def process_queue(self):
        """
        Check if task is completed.
        If it is completed show result and hide the progress bar
        :return: None
        """
        try:
            msg = self.queue.get(0)

            # show grouped procurements grouped by topics
            topic_procurement_text = []
            for topic_index in range(len(self.topic_modeller.grouped_topic_procurements)):
                topic_procurement_text.append('Topic %d\n' % topic_index)
                for p in self.topic_modeller.grouped_topic_procurements[topic_index]:
                    topic_procurement_text.append('\t' + p.display_text().replace('\n', '\n\t'))
                    topic_procurement_text.append('\t===============================')

            self.output_tb.set_output('\n'.join(topic_procurement_text))
            self.progress_bar.grid_remove()
            self.retrain_button.config(state=tk.NORMAL)
        except Queue.Empty:
            self.master.after(100, self.process_queue)


class ThreadedTask(threading.Thread):
    def __init__(self, queue, topic_modeller):
        threading.Thread.__init__(self)
        self.topic_modeller = topic_modeller
        self.queue = queue

    def run(self):
        """
        The method to load the topic and procurements is called in the threaded task
        :return: None
        """
        self.topic_modeller.load_topic_and_procurements()
        self.queue.put("Task finished")
