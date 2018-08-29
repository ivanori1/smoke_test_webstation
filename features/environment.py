from features.base.selenium_driver import SeleniumDriver
from features.pages.login_page import LoginPage
from features.pages.header_page import HeaderPage


def before_all(context):
    context.selenium_driver = SeleniumDriver()
    context.login_page = LoginPage()
    context.header_page = HeaderPage()


def after_all(context):
    context.selenium_driver.close()
