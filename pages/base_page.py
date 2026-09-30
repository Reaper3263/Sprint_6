from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import get_search_text_locator


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_and_click(self, element, timeout=5):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(element)
        )
        element.click()

    def click_searched_text(self, search_value):
        element = self.driver.find_element(*get_search_text_locator(search_value))
        self.scroll_and_click(element)

    def is_text_on_page(self, text, timeout=5):
        dynamic_xpath = f"//*[contains(text(), '{text}')]"

        try:
            WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located((By.XPATH, dynamic_xpath))
            )
            return True
        except TimeoutException:
            return False

    def wait_for_link_to_open(self, expected_url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(expected_url))

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_window(self, window_num):
        self.driver.switch_to.window(self.driver.window_handles[window_num])
