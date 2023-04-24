
import logging
from loancalc import calculations
import loancalc.view.windows as windows

log = logging.getLogger(__name__)


class LoanCalc:

    @staticmethod
    def run():
        pp = 100
        ib = calculations.getIntitialBalance(pp)

        log.info(f'Initial balance is: ${str(ib)}')

        # Bootstrap our main application window and kick off
        # the central event loop.
        main_window = windows.MainAppWindow()
        main_window.mainloop()
