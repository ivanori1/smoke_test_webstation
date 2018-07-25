import unittest
from selenium import webdriver
from com.teletrader.webstation.elements_and_data import Elements, Data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class TestNavigationButtons(unittest.TestCase):
    """
    This test cases check if every navigation button show corespondent detail page.
    NOTE: this is primitive solution, code is repeating every time, plan to do for loop in future
    """

    # TEST
    def test_nav_buttons(self):
        # Instance of Chrome browser
        driver = webdriver.Chrome()
        driver.maximize_window()
        wait = WebDriverWait(driver, 20)
        # Opens test branch
        driver.get(Data.base_url)
        # Test Case: Assert Title is TeleTrader WebStation
        assert Data.base_title == driver.title
        # Login
        driver.find_element(*Elements.username).send_keys(Data.str_username)
        driver.find_element(*Elements.password).send_keys(Data.str_password)
        driver.find_element(*Elements.eula_css).click()
        driver.find_element(*Elements.login_button).click()
        wait.until(EC.presence_of_element_located(Elements.logo_ws))
        # Test Case:Currency button
        driver.find_element(*Elements.currencies_button).click()
        # Test Outcome: Currency Detail page header
        wait.until(EC.presence_of_element_located(Elements.currencies_header))
        self.assertTrue(driver.find_element(*Elements.currencies_header).is_displayed())

        # Test Case:Market button
        driver.find_element(*Elements.market_button).click()
        # Test Outcome: Market Detail page header
        wait.until(EC.presence_of_element_located(Elements.market_header))
        self.assertTrue(driver.find_element(*Elements.market_header).is_displayed())

        # Test Case: Commodities button
        driver.find_element(*Elements.commodities_button).click()
        # Test Outcome: Commodities Detail page header
        wait.until(EC.presence_of_element_located(Elements.commodities_header))
        self.assertTrue(driver.find_element(*Elements.commodities_header).is_displayed())

        # Test Case:Fixed Income button
        driver.find_element(*Elements.fixed_income_button).click()
        # Test Outcome: Fixed Income Detail page header
        wait.until(EC.presence_of_element_located(Elements.fixedIncome_header))
        self.assertTrue(driver.find_element(*Elements.fixedIncome_header).is_displayed())

        # Test Case: Futures button
        driver.find_element(*Elements.futures_button).click()
        # Test Outcome: Futures Detail page header
        wait.until(EC.presence_of_element_located(Elements.futures_header))
        self.assertTrue(driver.find_element(*Elements.futures_header).is_displayed())

        # Test Case: Trump Effect button
        driver.find_element(*Elements.trump_effect_button).click()
        # Test Outcome: Trump Effect Detail page header
        wait.until(EC.presence_of_element_located(Elements.trump_effect_header))
        self.assertTrue(driver.find_element(*Elements.trump_effect_header).is_displayed())

        # Test Case: Screener button
        driver.find_element(*Elements.screener_button).click()
        # Test Outcome: Screener Detail page header
        wait.until(EC.presence_of_element_located(Elements.screener_header))
        self.assertTrue(driver.find_element(*Elements.screener_header).is_displayed())

        # Test Case: Funds button
        driver.find_element(*Elements.funds_button).click()
        # Test Outcome: Funds Detail page header
        wait.until(EC.presence_of_element_located(Elements.funds_header))
        self.assertTrue(driver.find_element(*Elements.funds_header).is_displayed())

        # Test Case: News button
        driver.find_element(*Elements.news_button).click()
        # Test Outcome: News Detail page header
        wait.until(EC.presence_of_element_located(Elements.news_header))
        self.assertTrue(driver.find_element(*Elements.news_header).is_displayed())

        # Test Case: Calendar button
        driver.find_element(*Elements.calendar_button).click()
        # Test Outcome: Calendar Detail page header
        wait.until(EC.presence_of_element_located(Elements.calendar_header))
        self.assertTrue(driver.find_element(*Elements.calendar_header).is_displayed())

        # Test Case: Portfolio button
        driver.find_element(*Elements.portfolio_button).click()
        # Test Outcome: Portfolio Detail page header
        wait.until(EC.presence_of_element_located(Elements.portfolio_header))
        self.assertTrue(driver.find_element(*Elements.portfolio_header).is_displayed())
        # TODO if no portfolio scenario
        # Test Case: Watchlist button
        driver.find_element(*Elements.watchlist_button).click()
        # Test Outcome: Watchlist Detail page header
        wait.until(EC.presence_of_element_located(Elements.watchlist_header))
        # TODO if no watchlist scenario
        # Test Case: Analyzer button
        driver.find_element(*Elements.analyzer_button).click()
        # Test Outcome: Analyzer Detail page header
        wait.until(EC.presence_of_element_located(Elements.analyzer_header))
        self.assertTrue(driver.find_element(*Elements.analyzer_header).is_displayed())

        # Test Case: Alerts button
        driver.find_element(*Elements.alert_button).click()
        # Test Outcome: Alert Detail page header
        wait.until(EC.presence_of_element_located(Elements.alert_header))
        self.assertTrue(driver.find_element(*Elements.alert_button).is_displayed())

        # Test Case: Economic Data button
        driver.find_element(*Elements.economic_data_button).click()
        # Test Outcome: Economic Data Detail page header
        wait.until(EC.presence_of_element_located(Elements.economic_data_header))
        self.assertTrue(driver.find_element(*Elements.economic_data_header).is_displayed())


        # Test Case: ETFs button
        driver.find_element(*Elements.etf_button).click()
        # Test Outcome: ETFs Detail page header
        wait.until(EC.presence_of_element_located(Elements.etf_header))
        self.assertTrue(driver.find_element(*Elements.etf_header).is_displayed())

        # Test Case: Real Time button
        driver.find_element(*Elements.real_time_button).click()
        # Test Outcome: Real Time Detail page header
        wait.until(EC.presence_of_element_located(Elements.real_time_header))
        self.assertTrue(driver.find_element(*Elements.real_time_header).is_displayed())

