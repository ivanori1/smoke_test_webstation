import unittest
import pytest
from selenium import webdriver
from webstation.pages.login_page import LoginPage


class TestLogin(unittest.TestCase):

    def test_failed_login(self):
        # Instance of Chrome browser
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://webstationtest3.ttweb.net/WebStation.aspx")
        login_p = LoginPage(driver)

        login_p.test_failed_login()
        self.assertTrue(login_p.verify_failed_login())
