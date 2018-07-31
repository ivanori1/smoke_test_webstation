from selenium.webdriver.common.by import By


class SeleniumDriver:
    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        if locator_type == "css":
            return By.CSS_SELECTOR
        else:
            print("Unknown selector")

    def get_element(self, locator, locator_type="css"):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
        except:
            print("element not found")
        return element

    def click_on_element(self, locator, locator_type="css"):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
        except:
            print("click action not performed")

    def text_of_element(self, inner_text, locator, locator_type="css"):
        element_text = self.get_element(locator, locator_type).text
        if element_text == inner_text:
            return True
        else:
            print("Compared text do not match")
            return False

    def send_keys_to_element(self, data, locator, locator_type="css"):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(data)
        except:
            print("send keys not performed")

    def is_visible_element(self, locator, locator_type="css"):
        element_visible = self.get_element(locator, locator_type).is_displayed()
        if element_visible:
            return True
        else:
            return False
