import unittest
import pytest
from selenium import webdriver
from webstation.pages.login_page import LoginPage


class TestLogin(unittest.TestCase):
    driver = webdriver.Chrome()



    def test_failed_login(self):
        login_p = LoginPage(self.driver)
        login_p.open_start_page()
        login_p.test_failed_login()
        self.assertTrue(login_p.verify_failed_login())

