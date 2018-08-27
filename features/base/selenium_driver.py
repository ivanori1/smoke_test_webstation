from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class SeleniumDriver:
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(context):
        context.driver.close()

    def navigate(self, address):
        self.driver.get(address)

    def get_page_url(self):
        return self.driver.current_url

    def get_page_title(self):
        return self.driver.title

    def get_by_type(self, locator_type):
        if locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "xpath":
            return By.XPATH
        else:
            print("Unknown selector")

    def get_element(self, locator, locator_type="css"):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
        except:
            print("element not found " + locator.upper())
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
            element.clear()
            element.send_keys(data)
        except:
            print("send keys not performed")

    def is_visible_element(self, locator, locator_type="css"):
        element_visible = self.get_element(locator, locator_type).is_displayed()
        return element_visible

    def is_selected_element(self, locator, locator_type="xpath"):
        element_is_selected = self.get_element(locator, locator_type).is_selected()
        return element_is_selected

    def wait_for_element(self, locator, locator_type="css"):
        by_type = self.get_by_type(locator_type)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((by_type, locator)))
        return element

    def wait_for_element_to_be_clickable(self, locator, locator_type="css"):
        by_type = self.get_by_type(locator_type)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((by_type, locator)))
        return element

    def attribute_value_of_element(self, attribute_name, locator, locator_type="css"):
        try:
            element = self.get_element(locator, locator_type)
            element_attribute = element.get_attribute(attribute_name)
            return element_attribute
        except:
            print("value of atribute not found")

    def select_from_dropdown(self, text, locator, locator_type="css"):
        try:
            select_dropdown = Select(self.get_element(locator, locator_type))
            select_dropdown.select_by_visible_text(text)
            print("Selected element is: " + text)

        except:

            print("element not found " + locator)