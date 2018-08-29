from features.base.selenium_driver import SeleniumDriver


class HeaderPage(SeleniumDriver):
    # Header buttons
    vertical_navigation_bar = ".navigation-vertical-container"
    layout_button = ".layout-button"
    vertical_navigation_layout_button = "[data-layout-id='full-vertical-navigation']"
    save_layout_button = "#saveLayout"
    costomize_and_control_button = "#user-button"

    # Navigation Buttons
    news_button = "[data-button='ne']"

    def change_layout_nav_vertical(self):
        self.click_on_element(self.layout_button)
        self.click_on_element(self.vertical_navigation_layout_button)
        self.click_on_element(self.save_layout_button)

    def navigation_box_is_visible(self):
        nav_box_visible = self.is_visible_element(self.vertical_navigation_bar)
        if not nav_box_visible:
            self.change_layout_nav_vertical()

    def click_news_navigation(self):
        self.click_on_element(self.news_button)

    def click_on_costomize_and_control(self):
        self.click_on_element(self.costomize_and_control_button)
