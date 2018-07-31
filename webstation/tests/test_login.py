import unittest
import pytest
from selenium import webdriver
from webstation.pages.login_page import LoginPage


class TestLogin(unittest.TestCase):
    driver = webdriver.Chrome()
    login_p = LoginPage(driver)

    def test_failed_login(self):
        self.login_p.open_start_page()
        self.login_p.test_failed_login()
        self.assertTrue(self.login_p.verify_failed_login())

    def test_successful_login(self):
        self.login_p.test_success_login()
        self.assertTrue(self.login_p.verify_success_login())
