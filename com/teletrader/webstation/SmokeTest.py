import unittest
from selenium import webdriver

class SmokeTest(unittest.TestCase):

    def test(self):
        # Instance of Chrome browser
        self.driver = webdriver.Chrome()
        # Opens test branch
        self.driver.get("http://webstationtest3.ttweb.net/WebStation.aspx")
        self.assertIn('TeleTrader WebStation', self.driver.title)

run = SmokeTest()
run.test()