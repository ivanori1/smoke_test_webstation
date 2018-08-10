import unittest
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

    def test_2_check_navigation_visible(self):
        self.header_p.is_navigation_visible()

    def test_click_markets(self):
        self.navigation_p.click_markets_button()
        self.assertTrue(self.navigation_p.is_visible_markets_header())

    def test_click_currency(self):
        self.navigation_p.click_currency_button()
        self.assertTrue(self.navigation_p.is_visible_currency_header())

    def test_click_commodities(self):
        self.navigation_p.click_on_commodities()
        self.assertTrue(self.navigation_p.is_visible_commodities_header())

    def test_click_fixed_income(self):
        self.navigation_p.click_on_fixed_income()
        self.assertTrue(self.navigation_p.is_visible_fixed_income_header())

    def test_click_futures(self):
        self.navigation_p.click_on_futures()
        self.assertTrue(self.navigation_p.is_visible_future_header())

    def test_click_trump_effect(self):
        self.navigation_p.click_on_trump_effect()
        self.assertTrue(self.navigation_p.is_visible_trump_header())

    def test_click_personal_page(self):
        self.navigation_p.click_personal_page()
        self.assertTrue(self.navigation_p.is_visible_personal_page_header())

    def test_click_screener(self):
        self.navigation_p.click_screener()
        self.assertTrue(self.navigation_p.is_visible_screener_header())

    def test_clik_funds(self):
        self.navigation_p.click_funds()
        self.navigation_p.is_visible_funds_header()