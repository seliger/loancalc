
import tkinter as tk
import logging

logger = logging.getLogger(__name__)

class Container(tk.Frame):

    def __init__(self, column=0, row=0, bd=2, relief=tk.GROOVE):
        tk.Frame.__init__(self, relief=relief, bd=bd)
        self.grid(row=row, column=column, sticky='nsew', padx=10, pady=10)
