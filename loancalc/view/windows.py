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

        # Set the window to be a static size (no re-sizing!)
        self.resizable(False, False)

        # Configure the grid to have a specific shape (approximately 40/60)
        self.grid_rowconfigure(0, minsize=window_height)
        self.grid_columnconfigure(0, minsize=(window_width // 2.5))
        self.grid_columnconfigure(1, minsize=(window_width - (window_width // 2.5)))

        # Drop two containers into the grid
        container = lcw.Container(self, row=0, column=0)
        container.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        container2 = lcw.Container(self, row=0, column=1)
        container2.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

        # Sorting out how to add a widget to an existing widget
        container.append_widget(lcw.StackedEntry, 'Test Entry 1:')
        container.append_widget(lcw.StackedEntry, 'Test Entry 2:')

        container.widgets[0].focus_set()

        # self.item2 = lcw.StackedEntry('Test entry 2:')
        # self.item2.grid(row=1, column=0, sticky='new', padx=15, pady=15)

        # TODO: Fix this to do something else...
        self.frames = []



