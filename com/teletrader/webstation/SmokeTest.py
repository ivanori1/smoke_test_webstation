import unittest
from typing import Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By


class SmokeTest(unittest.TestCase):
    # Instance of Chrome browser
    driver = webdriver.Chrome()
    base_url = 'http://webstationtest3.ttweb.net/WebStation.aspx'
    base_title = 'TeleTrader WebStation'
    str_username = 'ivan.coric91'
    str_password = 'ictrader123'

    # Elements
    username = By.ID, 'userName'
    password = By.ID, 'password'
    login = By.ID, 'loginUser'

    def test(self):
        # Opens test branch
        self.driver.get(self.base_url)
        # Assert Title is TeleTrader WebStation
        self.assertIn(self.base_title, self.driver.title)
        # Uncheck eula
        self.driver.find_element(self.username).send_keys(self.str_username)
        #self.driver.find_element_by_id("userName").send_keys(self.str_username)
        self.driver.find_element_by_id("password").send_keys(self.str_password)
        self.driver.find_element_by_id("loginUser").click()
        # Assert eula error
        self.assertEqual("You have to accept the End User License Agreement in order to log in."
                         , self.driver.find_element_by_class_name("error_container_inner").text)



