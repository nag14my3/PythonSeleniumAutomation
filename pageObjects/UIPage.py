import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from BaseClass import logger


@pytest.mark.usefixtures('logging')
class UIPageTest:
    log = logger()
    log.info("Script has started")
    radiobutton = (By.XPATH, '//*[@id="radio-btn-example"]/fieldset/label[2]/input')
    countrydropdown = (By.XPATH, '//*[@id="autocomplete"]')
    findcountryIndonesia = (By.XPATH, "//div[contains(text(),'Indonesia')]")
    selectoption = (By.XPATH, '//*[@id="dropdown-class-example"]')
    findoption1 = (By.XPATH, '//*[@id="checkBoxOption1"]')
    findoption3 = (By.XPATH, '//*[@id="checkBoxOption3"]')
    findalertbutton = (By.ID, 'name')
    alertacceptbutton = (By.ID, 'alertbtn')
    alertconfirmbutton = (By.ID, 'confirmbtn')
    openwindow = (By.ID, 'openwindow')
    opentab = (By.ID, 'opentab')
    hideorshowtextbox = (By.ID, 'displayed-text')
    hidetextbox = (By.ID, 'hide-textbox')
    showtextbox = (By.ID, 'show-textbox')
    scrollpageto = (By.XPATH, '/html/body/div[4]/div/fieldset/legend')
    mousehoverbutton = (By.ID, 'mousehover')
    frames = 'iframe-name'
    framesnames = (By.XPATH, '/html/body/app-root/div/header/div[2]/div/div/div[2]/nav/div[2]/ul/li[1]/a')
    alllinksinframes = (By.XPATH, '//a')
    rowspath = (By.XPATH, '//*[@id="product"]/tbody/tr')
    coloumnpath = (By.XPATH, '//*[@id="product"]/tbody/tr[2]/td')
    mousehoverpath = (By.XPATH, '/html/body/div[4]/div/fieldset/div/div/a')

    def __init__(self, driver):
        self.driver = driver

    def select_radiobutton(self):
        radiobutton2 = self.driver.find_element(*UIPageTest.radiobutton)
        radiobutton2.click()
        assert radiobutton2.is_selected()

    log.info("Radio Button2 is selected from Radio button example")

    def select_Country(self, countryname):
        finddropdown = self.driver.find_element(*UIPageTest.countrydropdown)
        finddropdown.send_keys("Ind")
        self.driver.implicitly_wait(10)
        self.driver.find_element(*UIPageTest.findcountryIndonesia).click()
        assert finddropdown.get_attribute("value") == countryname

    log.info("Indonesia is selected from suggestion drop down")

    def select_Option2(self):
        select = Select(self.driver.find_element(*UIPageTest.selectoption))
        select.select_by_visible_text('Option2')
        # assert select=="Option2"

    log.info("option2 is selected from the dropdown in DropDown Example")

    def select_checkbox(self):
        checkbox1 = self.driver.find_element(*UIPageTest.findoption1)
        checkbox3 = self.driver.find_element(*UIPageTest.findoption3)
        checkbox1.click()
        checkbox3.click()
        assert checkbox1.is_selected()
        assert checkbox3.is_selected()

    log.info("Option2 and Option3 is selected from Checkbox Example")

    def accept_Alert(self, name):
        self.driver.find_element(*UIPageTest.findalertbutton).send_keys(name)
        self.driver.find_element(*UIPageTest.alertacceptbutton).click()
        alert = self.driver.switch_to.alert
        msg = alert.text
        if (msg.find(name) == -1):
            raise NameError
        else:
            print(msg)
        alert.accept()

    log.info("Clicked on Alert button and name is displayed in Alert pop up")

    def alert_Dismiss(self, name):
        self.driver.find_element(*UIPageTest.findalertbutton).send_keys(name)
        self.driver.find_element(*UIPageTest.alertconfirmbutton).click()
        confirmalert = self.driver.switch_to.alert
        msg2 = confirmalert.text
        if msg2.find(name) == -1:
            raise NameError
        else:
            print(msg2)
        confirmalert.dismiss()

    log.info("Clicked on Alert button and name is displayed in and Dismissed")

    def open_newwindow(self, windowname):
        self.driver.find_element(*UIPageTest.openwindow).click()
        window1 = self.driver.window_handles[0]
        window2 = self.driver.window_handles[1]
        self.driver.switch_to.window(window2)
        print(self.driver.title)
        assert self.driver.title == windowname
        self.driver.switch_to.window(window1)
        print(self.driver.title)

    log.info("New Window is Opened and asserted the Title")

    def open_Newtab(self, newtab):
        self.driver.find_element(*UIPageTest.opentab).click()
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)
        print(self.driver.title)
        assert newtab in self.driver.title
        self.driver.switch_to.window(self.driver.window_handles[0])
        print(self.driver.title)

    log.info("New Tab is Opened and asserted the Title")

    def hideOrShowButton(self, name):
        self.driver.find_element(*UIPageTest.hideorshowtextbox).send_keys(name)
        hidebutton = self.driver.find_element(*UIPageTest.hidetextbox)
        hidebutton.click()
        '''if hidebutton.isdisplayed():
                AssertionError
        else:
            pass'''
        self.driver.find_element(*UIPageTest.showtextbox).click()


    log.info(
        "Name is entered in Text box and asserted the that hide box is displyed +"
        "or not and asserted the name after text box is displayed")

    def handling_WebTable(self):
        rows = len(self.driver.find_elements(*UIPageTest.rowspath))
        cols = len(self.driver.find_elements(*UIPageTest.coloumnpath))
        count = 0;
        for r in range(2, rows + 1):
            for c in range(1, cols + 1):
                value = self.driver.find_element_by_xpath(
                    '//*[@id="product"]/tbody/tr[' + str(r) + ']/td[' + str(c) + ']').text
                if (value.find("Selenium")) == -1:
                    pass
                else:
                    count = count + 1
                    print(value, end=' ')
                    print()
        print(count)

    log.info("WebTable is handled")

    def mouse_Hover(self):
        mousehover_button = self.driver.find_element(*UIPageTest.scrollpageto)
        mousehover_button.location_once_scrolled_into_view
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(*UIPageTest.mousehoverbutton)).perform()
        getlinks = len(self.driver.find_elements(*UIPageTest.mousehoverpath))
        print(getlinks)
        for links in range(1, getlinks + 1):
            linksname = self.driver.find_element_by_xpath(
                '/html/body/div[4]/div/fieldset/div/div/a[' + str(links) + ']').text
            print(linksname)
        print()

    log.info("Mouse Hover button is verified")

    def frames_CurrentWindow(self, iframename):
        self.driver.switch_to.frame(iframename)
        frame_inside = self.driver.find_element(*UIPageTest.framesnames)
        frame_inside.location_once_scrolled_into_view
        frame_inside.click()
        links_length = len(self.driver.find_elements(*UIPageTest.alllinksinframes))
        print(links_length)
        self.driver.switch_to.default_content()

    log.info("Successfully switched to frame and number of links present in the frame are displayed")
