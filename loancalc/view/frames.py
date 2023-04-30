import tkinter as tk
import loancalc.view.widgets as widgets
import logging

logger = logging.getLogger(__name__)


class MainLeftFrame(widgets.Container):

    def __init__(self, master):
        super().__init__(master)
        self.__widgets = [
            {'name': 'test1',
             'label': 'Test Entry 1:',
             'widget': widgets.StackedEntry,
             'value': tk.StringVar(),
             'focus': True
             },
            {'name': 'test2',
             'label': 'Test Entry 2:',
             'widget': widgets.StackedEntry,
             'value': tk.StringVar(),
             },
            {'name': 'test3',
             'label': 'Test Entry 3:',
             'widget': widgets.StackedEntry,
             'value': tk.StringVar(),
             },
            {'name': 'testbutton',
             'label': 'Click Me',
             'widget': tk.Button,
             'sticky': 'sew'
             },
            {'name': 'testbutton2',
             'label': 'Click Me 2',
             'widget': tk.Button,
             'sticky': 'sew'
             }
        ]

        self.generate_ui(self.__widgets)


class MainRightFrame(widgets.Container):

    def __init__(self, master):
        super().__init__(master)
