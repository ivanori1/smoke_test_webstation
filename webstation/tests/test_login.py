import unittest
import pytest
from selenium import webdriver
from webstation.pages.login_page import LoginPage
from webstation.pages.header_page import HeaderPage


class TestLogin(unittest.TestCase):
    driver = webdriver.Chrome()
    login_p = LoginPage(driver)
    header_p = HeaderPage(driver)

    @pytest.mark.run(order=1)
    def test_1_failed_login(self):
        self.login_p.open_start_page()
        self.login_p.test_failed_login()
        self.assertTrue(self.login_p.verify_failed_login())

    @pytest.mark.run(order=2)
    def test_2_successful_login(self):
        self.login_p.test_success_login()
        self.assertTrue(self.header_p.verify_success_login())

    @pytest.mark.run(order=3)
    def test_3_logout(self):
        self.header_p.perform_logout()
        self.assertTrue(self.login_p.verify_auto_login_and_eula_checked())
