import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logg = logging.getLogger(loggerName)

        filehandler = logging.FileHandler('logfile.log')
        formatt = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatt)

        logg.addHandler(filehandler)

        logg.setLevel(logging.DEBUG)
        return logg

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 7).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)