import inspect
import logging

import pytest


# @pytest.mark.parametrize("input,expected", [('02-01-1990', 'Thu Feb 01 1990 00:00:00 GMT+0000'), ('02-01-2000', 'Tue Feb 01 2000 00:00:00 GMT+0000')])
@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
