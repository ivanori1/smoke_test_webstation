from webstation.base.selenium_driver import SeleniumDriver


class HeaderPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Elements
    _logo_ws_image = "#logo-ws"
    _user_button = ".header_button#user-button"
    _logout_link = "[href='Logout.aspx']"

    def is_visible_logo(self):
        self.is_visible_element(self._logo_ws_image)

    def click_user_button(self):
        self.driver.implicitly_wait(5)
        self.click_on_element(self._user_button)

    def click_logout_link(self):
        self.click_on_element(self._logout_link)

    def verify_success_login(self):
        result = HeaderPage.is_visible_logo
        return result

    def perform_logout(self):
        self.click_user_button()
        self.click_logout_link()
