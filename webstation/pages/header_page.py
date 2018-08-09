from webstation.base.selenium_driver import SeleniumDriver


class HeaderPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Elements
    _navigation_vertical_container = ".navigation-vertical-container"
    _logo_ws_image = "#logo-ws"
    _user_button = ".header_button#user-button"
    _logout_link = "[href='Logout.aspx']"
    _layout_button = ".layout-button"
    _full_vertical_navigation_button = "[data-layout-id='full-vertical-navigation']"
    _save_layout_button = "#saveLayout"

    def is_visible_logo(self):
        self.is_visible_element(self._logo_ws_image)

    def click_user_button(self):
        self.driver.implicitly_wait(5)
        self.click_on_element(self._user_button)

    def click_logout_link(self):
        self.click_on_element(self._logout_link)

    def click_layout_button(self):
        self.click_on_element(self._layout_button)

    def click_full_vertical_navigation(self):
        self.click_on_element(self._full_vertical_navigation_button)

    def click_save_layout_button(self):
        self.click_on_element(self._save_layout_button)

    def verify_success_login(self):
        result = HeaderPage.is_visible_logo
        return result

    def perform_logout(self):
        self.click_user_button()
        self.click_logout_link()

    def perform_change_layout_vertical(self):
        self.click_layout_button()
        self.click_full_vertical_navigation()
        self.click_save_layout_button()

    def is_navigation_visible(self):
        result = self.is_visible_element(self._navigation_vertical_container)
        if not result:
            self.perform_change_layout_vertical()