import logging
import tkinter as tk
from tkinter import ttk
import loancalc
import loancalc.view.widgets as lcw

# Instantiate our global logger
logger = logging.getLogger(__name__)

class MainAppWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        # Init code heavily inspired by:
        # https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes
        tk.Tk.__init__(self, *args, **kwargs)
        logger.info('Initializing main window...')

        self.wm_title(f'{loancalc.APP_NAME} {loancalc.APP_VERSION}')

        # Calculate geometry and position of the main window
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = screen_width // 2
        center_y = screen_height // 2

        window_width = screen_width // 2
        window_height = screen_height // 2

        titlebarHeight = self.winfo_rooty() - self.winfo_y()

        self.geometry('{}x{}+{}+{}'.format(
            window_width,
            window_height,
            center_x - (window_width // 2),
            center_y - (window_height // 2)
        ))

        self.resizable(False, False)

        self.grid_rowconfigure(0, minsize=window_height )
        self.grid_columnconfigure(0, minsize=(window_width // 2.5))
        self.grid_columnconfigure(1, minsize=(window_width - (window_width // 2.5)))


        container = lcw.Container(row=0, column=0)
        container2 = lcw.Container(row=0, column=1)

        self.frames = []



