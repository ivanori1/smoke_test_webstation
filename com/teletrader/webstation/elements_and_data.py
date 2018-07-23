from selenium.webdriver.common.by import By


class Data:
    base_url = 'http://webstationtest3.ttweb.net/WebStation.aspx'
    base_title = 'TeleTrader WebStation'
    str_username = 'ivan.coric91'
    str_password = 'ictrader123'
    error_accept_eula = 'You have to accept the End User License Agreement in order to log in.'


class Elements:
    username = By.ID, 'userName'
    password = By.ID, 'password'
    login_button = By.ID, 'loginUser'
    error_container = By.CLASS_NAME, 'error_container_inner'
    eula_css = By.CSS_SELECTOR, "[for='eulaAccepted'].checkBoxLabel"
    eula_xpath = By.XPATH, "//*[@id='eulaAccepted']"
    auto_login = By.XPATH, "//*[@id='autologin']"
    logo_ws = By.ID, 'logo-ws'
    user_button = By.ID, 'user-button'
    account_settings = By.CSS_SELECTOR, "[href='personal_registration.aspx']"
    region_box = By.ID, 'regionBox'
    logout = By.CSS_SELECTOR, "[href='Logout.aspx']"

