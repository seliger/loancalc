import tkinter as tk
from tkinter import ttk
import loancalc


class MainAppWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        # Init code heavily inspired by:
        # https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes
        tk.Tk.__init__(self, *args, **kwargs)

        self.wm_title(f'{loancalc.APP_NAME} {loancalc.APP_VERSION}')

        container = tk.Frame(self, height=900, width=1500)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}


