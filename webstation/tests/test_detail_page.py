import unittest
from selenium import webdriver
from webstation.pages.login_page import LoginPage
from webstation.pages.header_page import HeaderPage
from webstation.pages.navigation_page import NavigationPage
from webstation.pages.detail_page import DetailPage


class TestDetailPage(unittest.TestCase):
    driver = webdriver.Chrome()
    login_p = LoginPage(driver)
    header_p = HeaderPage(driver)
    navigation_p = NavigationPage(driver)
    detail_p = DetailPage(driver)

    def test_1_success_login(self):
        self.login_p.open_start_page()
        self.login_p.test_success_login()
        self.assertTrue(self.header_p.verify_success_login())

    def test_2_check_overivew_visible(self):
        self.header_p.is_left_div_visible()

    def test_3_click_on_detail_page_menu(self):
        self.detail_p.click_detail_page_menu()
