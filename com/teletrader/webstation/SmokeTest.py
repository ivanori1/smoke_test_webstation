import unittest
from selenium import webdriver


class SmokeTest(unittest.TestCase):
    # Instance of Chrome browser
    driver = webdriver.Chrome()

    # CheckBoxes

    def test(self):
        # Opens test branch
        self.driver.get('http://webstationtest3.ttweb.net/WebStation.aspx')
        # Assert Title is TeleTrader WebStation
        self.assertIn('TeleTrader WebStation', self.driver.title)
        # Uncheck eula
        self.driver.find_element_by_id("userName").send_keys("ivan.coric91")
        self.driver.find_element_by_id("password").send_keys("ictrader123")
        self.driver.find_element_by_id("loginUser").click()
        # Assert eula error
        self.assertEqual("You have to accept the End User License Agreement in order to log in."
                         , self.driver.find_element_by_class_name("error_container_inner").text)
        # Successful login
        self.driver.find_element_by_id("userName").clear()
        self.driver.find_element_by_id("userName").send_keys("ivan.coric91")
        self.driver.find_element_by_id("password").send_keys("ictrader123")
        self.driver.find_element_by_css_selector("[for='eulaAccepted'].checkBoxLabel").click()
        self.driver.find_element_by_id("loginUser").click()
        # TODO Assertation for logo-ws.is_displayed

run = SmokeTest()
run.test()
