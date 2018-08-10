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

    def test_click_funds(self):
        self.navigation_p.click_funds()
        self.navigation_p.is_visible_funds_header()

    def test_click_news(self):
        self.navigation_p.click_news()
        self.navigation_p.is_visible_news_header()

    def test_click_portfolio(self):
        self.navigation_p.click_portfolio()
        self.navigation_p.is_visible_portfolio_header()

    def test_click_watchlist(self):
        self.navigation_p.click_watchlist()
        self.navigation_p.is_visible_watchlist_header()

    def test_click_calendar(self):
        self.navigation_p.click_calendar()
        self.navigation_p.is_visible_calendar_header()

    def test_click_analyzer(self):
        self.navigation_p.click_analyzer()
        self.navigation_p.is_visible_analyzer_header()

    def test_click_alerts(self):
        self.navigation_p.click_alerts()
        self.navigation_p.is_visible_alert_header()

    def test_click_economic_data(self):
        self.navigation_p.click_economic_data()
        self.navigation_p.is_visible_economic_data_header()

    def test_click_etf(self):
        self.navigation_p.click_etf()
        self.navigation_p.is_visible_etf_header()

    def test_click_real_time(self):
        self.navigation_p.click_real_time()
        self.navigation_p.is_visible_real_time_header()

    def test_click_smart_backtester(self):
        self.navigation_p.click_on_smart_backtester()
        self.navigation_p.is_visible_smart_backtester()
