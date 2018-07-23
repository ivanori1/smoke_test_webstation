import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from com.teletrader.webstation.elements_and_data import Elements, Data


class SmokeTest(unittest.TestCase):

    # Methods
    def change_region_germany(self):
        boolean_funds_visible = self.driver.find_element(*self.funds_button).is_selected()
        region_box = self.driver.find_element(*self.region_box)
        select_region = Select(region_box)
        if not boolean_funds_visible:
            self.driver.find_element(*self.user_button).click()
            self.driver.find_element(*self.account_settings).click()
            select_region.select_by_value("DE")

    def is_eula_selected(self):
        boolean_eula = self.driver.find_element(*self.eula_xpath).is_selected()
        if not boolean_eula:
            self.driver.find_element(*self.eula_css).click()

    def login_method(self):
        self.driver.find_element(*self.username).clear()
        self.driver.find_element(*self.username).send_keys(self.str_username)
        self.driver.find_element(*self.password).send_keys(self.str_password)
        self.is_eula_selected()
        self.driver.find_element(*self.login).click()

    # TEST
    def test(self):
        # Instance of Chrome browser
        driver = webdriver.Chrome()
        driver.maximize_window()

        # Opens test branch
        driver.get(Data.base_url)
        # Test Case: Assert Title is TeleTrader WebStation
        assert Data.base_title == driver.title
        # Test Case: Uncheck eula
        driver.find_element(*Elements.username).send_keys(Data.str_username)
        driver.find_element(*Elements.password).send_keys(Data.str_password)
        driver.find_element(*Elements.login_button).click()
        assert Data.error_accept_eula == driver.find_element(*Elements.error_container).text
