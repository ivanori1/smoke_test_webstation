from webstation.base.selenium_driver import SeleniumDriver


class NavigationPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Navigation Elements
    _market_button = ".navigation-vertical [href='securities_overview.aspx']"
    _currencies_button = ".navigation-vertical [href='currencies_Currencies.aspx']"
    _commodities_button = ".navigation-vertical [href='commodities.aspx']"
    _fixed_income_button = ".navigation-vertical [href='bonds_governmentyields.aspx']"
    _funds_button = ".navigation-vertical [href='funds_topperformerOverview.aspx']"
    _futures_button = ".navigation-vertical [href*='Futures']"
    _news_button = "[class*='navigation'][href*='news']"
    _calendar_button = ".navigation-vertical [href*='company_calendar']"
    _analyzer_button = ".navigation-vertical [href='analyzer.aspx']"
    _portfolio_button = ".navigation-vertical [href='personal_portfolioDetail.aspx']"
    _watchlist_button = ".navigation-vertical [href='personal_watchlist.aspx']"
    _alert_button = ".navigation-vertical [hregf='personal_notifications.aspx']"
    _economic_data_button = ".navigation-vertical [href='economic_calendar.aspx']"
    _trump_effect_button = ".navigation-vertical [href='trump_effect.aspx']"
    _personal_page_button = ".icon-container [href='personal_dashboardreact.aspx']"
    _back_tester_button = ".navigation-vertical [href='portfolio_backtester.aspx']"
    _screener_button = ".navigation-vertical [href='screener_overview.aspx']"
    _etf_button = ".navigation-vertical [href='funds_etfOverview.aspx']"
    _real_time_button = ".navigation-vertical [href='realtime_Indications.aspx']"

    # Detail page headers
    _market_header = ".main-pages-header.markets"
    _currencies_header = ".main-pages-header.currencies"
    _fixedIncome_header = ".main-pages-header.fixedIncome"
    _commodities_header = ".main-pages-header.commodities"
    _futures_header = ".main-pages-header.futures"
    _funds_header = ".main-pages-header.funds"
    _news_header = ".main-pages-header.news-header"
    _calendar_header = ".main-pages-header.companyCalendar"
    _analyzer_header = ".main-pages-header.analyzerHeader"
    _portfolio_header = ".main-pages-header.portfolio"
    _watchlist_header = ".main-pages-header.watchlist"
    _alert_header = ".main-pages-header.alerts"
    _personal_page_header = ".main-pages-header.personal-pages"
    _trump_effect_header = ".main-pages-header.trumpEfect"
    _economic_data_header = ".main-pages-header.economicCalendar"
    _back_tester_header = ".backtester-header.back-tester"
    _screener_header = ".main-pages-header.screenerHeader"
    _etf_header = ".main-pages-header.etf"
    _real_time_header = ".main-pages-header.realtimeIn"

    def click_markets_button(self):
        self.click_on_element(self._market_button)

    def is_visible_markets_header(self):
        self.wait_for_element(self._market_header)
        result = self.is_visible_element(self._market_header)
        return result

    def click_currency_button(self):
        self.click_on_element(self._currencies_button)

    def is_visible_currency_header(self):
        self.wait_for_element(self._currencies_header)
        result = self.is_visible_element(self._currencies_header)
        return result

    def click_on_commodities(self):
        self.click_on_element(self._commodities_button)

    def is_visible_commodities_header(self):
        self.wait_for_element(self._commodities_header)
        result = self.is_visible_element(self._commodities_header)
        return result

    def click_on_fixed_income(self):
        self.click_on_element(self._fixed_income_button)

    def is_visible_fixed_income_header(self):
        self.wait_for_element(self._fixedIncome_header)
        result = self.is_visible_element(self.is_visible_fixed_income_header())
        return result

    def click_on_futures(self):
        self.click_on_element(self._futures_button)

    def is_visible_future_header(self):
        self.wait_for_element(self._futures_header)
        result = self.is_visible_element(self._futures_header)
        return result

    def click_on_trump_effect(self):
        self.click_on_element(self._trump_effect_button)

    def is_visible_trump_header(self):
        self.wait_for_element(self._trump_effect_header)
        result = self.is_visible_element(self._trump_effect_header)
        return result

    def click_personal_page(self):
        self.click_on_element(self._personal_page_button)

    def is_visible_personal_page_header(self):
        self.wait_for_element(self._personal_page_header)
        result = self.is_visible_element(self._personal_page_header)
        return result

    def click_on_smart_backtester(self):
        self.click_on_element(self._back_tester_button)

    def is_visible_smart_backtester(self):
        self.wait_for_element(self._back_tester_header)
        result = self.is_visible_element(self._back_tester_header)
        return result

    def click_screener(self):
        self.click_on_element(self._screener_button)

    def is_visible_screener_header(self):
        self.wait_for_element(self._screener_header)
        result = self.is_visible_element(self._screener_header)
        return result

    def click_funds(self):
        self.click_on_element(self._funds_button)

    def is_visible_funds_header(self):
        self.wait_for_element(self._futures_header)
        result = self.is_visible_element(self._futures_header)
        return result

    def click_news(self):
        self.click_on_element(self._news_button)

    def is_visible_news_header(self):
        self.wait_for_element(self._news_header)
        result = self.is_visible_element(self._news_header)
        return result

    def click_portfolio(self):
        self.click_on_element(self._portfolio_button)

    def is_visible_portfolio_header(self):
        self.wait_for_element(self._portfolio_header)
        result = self.is_visible_element(self._portfolio_header)
        return result

    def click_watchlist(self):
        self.click_on_element(self._watchlist_button)

    def is_visible_watchlist_header(self):
        self.wait_for_element(self._watchlist_header)
        result = self.is_visible_element(self._watchlist_header)
        return result
    def click_calendar(self):
        self.click_on_element(self._calendar_button)

    def is_visible_calendar_header(self):
        self.wait_for_element(self._calendar_header)
        result = self.is_visible_element(self._calendar_header)
        return result

    def click_analyzer(self):
        self.click_on_element(self._analyzer_button)

    def is_visible_analyzer_header(self):
        self.wait_for_element(self._analyzer_header)
        result = self.is_visible_element(self._analyzer_header)
        return result

    def click_alerts(self):
        self.click_on_element(self._alert_button)

    def is_visible_alert_header(self):
        self.wait_for_element(self._alert_header)
        result = self.is_visible_element(self._alert_header)
        return result

    def click_economic_data(self):
        self.click_economic_data()

    def is_visible_economic_data_header(self):
        self.wait_for_element(self._economic_data_header)
        result = self.is_visible_element(self._economic_data_header)
        return result

    def click_etf(self):
        self.click_on_element(self._etf_button)

    def is_visible_etf_header(self):
        self.wait_for_element(self._etf_header)
        result = self.is_visible_element(self._etf_header)
        return result

    def click_real_time(self):
        self.click_on_element(self._real_time_button)

    def is_visible_real_time_header(self):
        self.wait_for_element(self._real_time_header)
        result = self.is_visible_element(self._real_time_header)
        return result
