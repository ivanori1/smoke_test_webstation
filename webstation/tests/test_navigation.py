import unittest
import pytest
from selenium import webdriver
from webstation.pages.login_page import LoginPage
from webstation.pages.header_page import HeaderPage
from webstation.pages.navigation_page import NavigationPage
from selenium.webdriver.support.ui import WebDriverWait


class TestNavigation(unittest.TestCase):
    driver = webdriver.Chrome()
    login_p = LoginPage(driver)
    header_p = HeaderPage(driver)
    navigation_p = NavigationPage(driver)
    wait = WebDriverWait(driver, 10)

    def test_1_success_login(self):
        self.login_p.open_start_page()
        self.login_p.test_success_login()
        self.assertTrue(self.header_p.verify_success_login())

    def test_2_click_markets(self):
        self.navigation_p.click_markets_button()
        self.assertTrue(self.navigation_p.is_visible_markets_header())

    def test_3_click_currency(self):
        self.navigation_p.click_currency_button()
        self.assertTrue(self.navigation_p.is_visible_currency_header())

    def test_4_click_commodities(self):
        self.navigation_p.click_on_commodities()
        self.assertTrue(self.navigation_p.is_visible_commodities_header())

    def test_5_click_fixed_income(self):
        self.navigation_p.click_on_fixed_income()
        self.assertTrue(self.navigation_p.is_visible_fixed_income_header())

    def test_5_click_futures(self):
        self.navigation_p.click_on_futures()
        self.assertTrue(self.navigation_p.is_visible_future_header())

    def test_6_click_trump_effect(self):
        self.navigation_p.click_on_trump_effect()
        self.assertTrue(self.navigation_p.is_visible_trump_header())
