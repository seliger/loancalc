
import logging
from loancalc import calculations

log = logging.getLogger(__name__)


class LoanCalc:

    @staticmethod
    def run():
        pp = 100
        ib = calculations.getIntitialBalance(pp)

        log.info(f'Initial balance is: ${str(ib)}')





