import pytest

from BaseClass import BaseClassPySel
from pageObjects.UIPage import UIPageTest
from readConfigfile import read_method


@pytest.mark.usefixtures('read_method')
class TestPyselAutomation(BaseClassPySel):

    def test_startExecution(self, read_method):
        driver = self.driver
        login = UIPageTest(driver)
        login.select_radiobutton()
        login.select_Country(read_method['countryname'])
        login.select_Option2()
        login.select_checkbox()
        login.accept_Alert(read_method['name'])
        login.alert_Dismiss(read_method['name'])
        login.open_newwindow(read_method['window'])
        login.open_Newtab(read_method['tab'])
        login.hideOrShowButton(read_method['name'])
        login.handling_WebTable()
        login.mouse_Hover()
        login.frames_CurrentWindow(read_method['framename'])
