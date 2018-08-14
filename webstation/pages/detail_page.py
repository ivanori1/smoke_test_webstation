from webstation.base.selenium_driver import SeleniumDriver


class DetailPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Elements
    _market_tab_button = "#market-tab-link"
    _detail_page_menu = "#leftDiv .detail-pages-icon "
    _new_window_icon = ".new-window"

    def click_detail_page_menu(self):
        self.click_on_element(self._detail_page_menu)