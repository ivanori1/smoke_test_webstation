import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from com.teletrader.webstation.elements_and_data import Elements, Data


class SmokeTest(unittest.TestCase):

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
