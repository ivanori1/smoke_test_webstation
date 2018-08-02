from webstation.base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

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
    _alert_button = ".navigation-vertical [href='personal_notifications.aspx']"
    _economic_data_button = ".navigation-vertical [href='economic_calendar.aspx']"
    _trump_effect_button = ".navigation-vertical [href='trump_effect.aspx']"
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
    _trump_effect_header = ".main-pages-header.trumpEfect"
    _economic_data_header = ".main-pages-header.economicCalendar"
    _back_tester_header = ".backtester-header.back-tester"
    _screener_header = ".main-pages-header.screenerHeader"
    _etf_header = ".main-pages-header.etf"
    _real_time_header = ".main-pages-header.realtimeIn"

