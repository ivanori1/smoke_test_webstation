import unittest
from com.teletrader.webstation.login_test import TestLogin
from com.teletrader.webstation.navigation_button_test import TestNavigationButtons
import logging

# Get all test cases
tc_login = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
tc_nav_b = unittest.TestLoader().loadTestsFromTestCase(TestNavigationButtons)

# Create test
smoke_test = unittest.TestSuite([tc_login, tc_nav_b])
unittest.TextTestRunner().run(smoke_test)
logging.basicConfig(filename='test.log', level=logging.DEBUG)
