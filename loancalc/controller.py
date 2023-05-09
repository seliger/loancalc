import logging
import loancalc.view.windows as windows
import loancalc.model.loan as loan

log = logging.getLogger(__name__)


class LoanCalcController:
    def __init__(self):
        pass


class LoanCalcApp:
    views = {'main_window': windows.MainAppWindow()}
    models = {}
    controllers = {}

    def __init__(self):
        # Bootstrap our main application window and kick off
        # the central event loop.
        self.views['main_window'].mainloop()
