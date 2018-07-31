from webstation.base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Elements
    _login_button = "#loginUser"
    _error_box = ".error_container_inner"

    # Errors
    _accept_eula_error = "You have to accept the End User License Agreement in order to log in."

    def click_login_button(self):
        self.click_on_element(self._login_button)

    def open_start_page(self):
        self.driver.maximize_window()
        self.driver.get("http://webstationtest3.ttweb.net/WebStation.aspx")

    def test_failed_login(self):
        self.click_login_button()

    def verify_failed_login(self):
        result = self.text_of_element(self._accept_eula_error, self._error_box)
        return result
