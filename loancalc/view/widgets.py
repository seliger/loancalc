import tkinter as tk
import logging

logger = logging.getLogger(__name__)


class Container(tk.Frame):

    widgets = []

    def __init__(self, master, bd=2, relief=tk.GROOVE):
        tk.Frame.__init__(self, master, relief=relief, bd=bd)
        self.columnconfigure(0, weight=1)
        logger.debug(f"{__class__.__name__}'s master: {self.master}")

    def append_widget(self, widget_type, *args, **kwargs):
        logger.debug(f'{__class__.__name__} is {self}')
        widget = widget_type(self, *args, **kwargs)
        self.widgets.append(widget)
        self.widgets[len(self.widgets) - 1].grid(
            column=0,
            row=len(self.widgets) - 1,
            sticky="nsew",
            padx=40,
            pady=20
        )


class StackedEntry(tk.Frame):
    def __init__(self, master, text, validator=None):
        tk.Frame.__init__(self, master)

        self.columnconfigure(0, weight=1)
        self['bg'] = '#ffc0c0'

        self.lbl_entry = tk.Label(self)
        self.txt_entry = tk.Entry(self)

        self.lbl_entry['text'] = text
        self.lbl_entry.grid(row=0, column=0, sticky='nsew')
        self.txt_entry.grid(row=1, column=0, sticky='nsew')

        # Force this widget to set the focus to the entry
        # box when called.
        self.focus_set = self.txt_entry.focus_set
