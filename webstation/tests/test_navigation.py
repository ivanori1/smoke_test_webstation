import unittest
import pytest
from selenium import webdriver
from webstation.pages.login_page import LoginPage
from webstation.pages.header_page import HeaderPage
from webstation.pages.navigation_page import NavigationPage


class TestNavigation(unittest.TestCase):
    driver = webdriver.Chrome()
    login_p = LoginPage(driver)
    header_p = HeaderPage(driver)
    navigation_p = NavigationPage(driver)

    def test_1_success_login(self):
        self.login_p.open_start_page()
        self.login_p.test_success_login()
        self.assertTrue(self.header_p.verify_success_login())

    def test_2_click_markets(self):
        self.navigation_p.click_markets_button()
        self.assertTrue(self.navigation_p.is_visible_markets_header())
