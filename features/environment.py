from features.base.selenium_driver import SeleniumDriver
from features.pages.login_page import LoginPage


def before_all(context):
    context.selenium_driver = SeleniumDriver()
    context.login_page = LoginPage()
