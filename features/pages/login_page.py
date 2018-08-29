from features.base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):
    # Elements
    _username_placeholder = "#userName"
    _password_placeholder = "#password"
    _eula_checkbox = "[for='eulaAccepted'].checkBoxLabel"
    _eula_checkbox_xpath = "//*[@id='eulaAccepted']"
    _autologin_checkbox = "[for='autologin'].checkBoxLabel"
    _autologin_checkbox_xpath = "//*[@id='autologin']"
    _login_button = "#loginUser"
    _error_box = ".error_container_inner"
    _language_box = "#langButton1"
    _language_box_en = "#langNavien"
    _language_box_de = "#langNavide"
    _logo_image = "#logo-ws"
    _home_button = "#appIcon"

    def select_language(self, language):
        self.click_on_element(self._language_box)
        if language == "English":
            self.click_on_element(self._language_box_en)
        elif language == "Deutch":
            self.click_on_element(self._language_box_de)

    def type_username_placeholder(self, username):
        self.send_keys_to_element(username, self._username_placeholder)

    def type_password_placeholder(self, password):
        self.send_keys_to_element(password, self._password_placeholder)

    def is_eula_checked(self):
        eula_TF = self.is_selected_element(self._eula_checkbox_xpath)
        return eula_TF

    def check_eula(self, status):
        if status == "checked":
            if not self.is_eula_checked():
                self.click_on_element(self._eula_checkbox)
        elif status == "unchecked":
            if self.is_eula_checked():
                self.click_on_element(self._eula_checkbox)

    def is_autologin_checked(self):
        autologinTF = self.is_selected_element(self._autologin_checkbox_xpath)
        return autologinTF

    def check_autologin(self, status):
        if status == "checked":
            if not self.is_autologin_checked():
                self.click_on_element(self._autologin_checkbox)
        elif status == "unchecked":
            if self.is_autologin_checked():
                self.click_on_element(self._autologin_checkbox)

    def click_login_button(self):
        self.click_on_element(self._login_button)

    def open_start_page(self):
        self.driver.maximize_window()
        self.driver.get("https://demo-biq.dev.tradecore.io/#/")

    def test_failed_login(self):
        self.click_login_button()

    def verify_failed_login(self, error):
        result = self.text_of_element(error, self._error_box)
        return result

    def verify_auto_login_and_eula_checked(self):
        result = self.is_autologin_checked() and self.is_eula_checked()
        return result

    def home_button_appear(self):
        self.wait_for_element_to_be_clickable(self._home_button)
        result = self.is_visible_element(self._home_button)
        return result
