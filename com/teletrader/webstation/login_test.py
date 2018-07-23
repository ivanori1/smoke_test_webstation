import unittest
from selenium import webdriver
from com.teletrader.webstation.elements_and_data import Elements, Data


class TestLogin(unittest.TestCase):

    # TEST
    def test_login(self):
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
        # Test Case: Successful login
        driver.find_element(*Elements.username).clear()
        driver.find_element(*Elements.username).send_keys(Data.str_username)
        driver.find_element(*Elements.password).send_keys(Data.str_password)
        driver.find_element(*Elements.eula_css).click()
        driver.find_element(*Elements.login_button).click()
        # Test Outcome: Start page is displayed
        assert driver.find_element(*Elements.logo_ws).is_displayed()
        # Test Case: Logout
        # Logout
        driver.find_element(*Elements.user_button).click()
        driver.find_element(*Elements.logout).click()
        # Test Outcome: Login page should appear with empty username and password text box.
        # „EULA“ and „Stay logged in“ are selected.
        driver.implicitly_wait(10)
        self.assertTrue(driver.find_element(*Elements.eula_xpath).is_selected())
        self.assertTrue(driver.find_element(*Elements.auto_login).is_selected())
