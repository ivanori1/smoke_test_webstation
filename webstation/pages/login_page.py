from webstation.base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Elements
    _username_placeholder = "#userName"
    _password_placeholder = "#password"
    _eula_checkbox = "[for='eulaAccepted'].checkBoxLabel"
    _eula_checkbox_xpath = "//*[@id='eulaAccepted']"
    _autologin_checkbox = "[for='autologin'].checkBoxLabel"
    _autologin_checkbox_xpath = "//*[@id='autologin']"
    _login_button = "#loginUser"
    _error_box = ".error_container_inner"
    # Errors
    _accept_eula_error = "You have to accept the End User License Agreement in order to log in."

    def type_username_placeholder(self, username):
        print(self.attribute_value_of_element("placeholder", self._username_placeholder))
        self.send_keys_to_element(username, self._username_placeholder)

    def type_password_placeholder(self, password):
        self.send_keys_to_element(password, self._password_placeholder)

    def is_eula_checked(self):
        eula_TF = self.is_selected_element(self._eula_checkbox_xpath)
        return eula_TF

    def check_eula(self):
        if not self.is_eula_checked():
            self.click_on_element(self._eula_checkbox)

    def is_autologin_checked(self):
        autologinTF = self.is_selected_element(self._autologin_checkbox_xpath)
        return autologinTF
    def check_autologin(self):
        if not self.is_autologin_checked():
            self.click_on_element(self._autologin_checkbox)

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

    def test_success_login(self, username="ivan.coric91", password="ictrader123"):
        self.type_username_placeholder(username)
        self.type_password_placeholder(password)
        self.check_eula()
        self.click_login_button()

    def verify_auto_login_and_eula_checked(self):
        result = self.is_autologin_checked() and self.is_eula_checked()
        return result

