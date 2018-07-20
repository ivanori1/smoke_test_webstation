import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class SmokeTest(unittest.TestCase):
    # Instance of Chrome browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    base_url = 'http://webstationtest3.ttweb.net/WebStation.aspx'
    base_title = 'TeleTrader WebStation'
    str_username = 'ivan.coric91'
    str_password = 'ictrader123'
    error_accept_eula = 'You have to accept the End User License Agreement in order to log in.'
    # Elements
    username = By.ID, 'userName'
    password = By.ID, 'password'
    login = By.ID, 'loginUser'
    error = By.CLASS_NAME, 'error_container_inner'
    eula_css = By.CSS_SELECTOR, "[for='eulaAccepted'].checkBoxLabel"
    eula_xpath = By.XPATH, "//*[@id='eulaAccepted']"
    auto_login = By.XPATH, "//*[@id='autologin']"
    logo_ws = By.ID, 'logo-ws'
    user_button = By.ID, 'user-button'
    logout = By.CSS_SELECTOR, "[href='Logout.aspx']"
    # Navigation buttons

    def test(self):
        # Opens test branch
        self.driver.get(self.base_url)
        # Test Case: Assert Title is TeleTrader WebStation
        self.assertIn(self.base_title, self.driver.title)
        # Test Case: Uncheck eula
        self.driver.find_element(*self.username).send_keys(self.str_username)
        self.driver.find_element(*self.password).send_keys(self.str_password)
        self.driver.find_element(*self.login).click()
        # Test Outcome: Assert eula error
        self.assertEqual(self.error_accept_eula, self.driver.find_element(*self.error).text)

        # Test Case: Successful login
        self.driver.find_element(*self.username).clear()
        self.driver.find_element(*self.username).send_keys(self.str_username)
        self.driver.find_element(*self.password).send_keys(self.str_password)
        self.driver.find_element(*self.eula_css).click()
        self.driver.find_element(*self.login).click()
        # Test Outcome: Assert logo is_displayed
        assert self.driver.find_element(*self.logo_ws).is_displayed()

        # Test Case: Logout
        self.driver.find_element(*self.user_button).click()
        self.driver.find_element(*self.logout).click()
        # Test Outcome: Login page should appear with empty username and password text box.
        # „EULA“ and „Stay logged in“ are selected.
        assert self.driver.find_element(*self.eula_xpath).is_selected()
        assert self.driver.find_element(*self.auto_login).is_selected()


