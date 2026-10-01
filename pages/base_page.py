from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import get_search_text_locator


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.presence_of_element_located(locator),
        )

    def click(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            expected_conditions.element_to_be_clickable(locator),
        )
        element.click()

    def enter_text(self, locator, text, key_to_send=None, time=10):
        element = self.find_element(locator, time)
        element.clear()
        element.send_keys(text)
        if key_to_send:
            element.send_keys(key_to_send)

    def scroll_and_click(self, locator, timeout=5):
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        )
        element.click()

    def click_searched_text(self, search_value):
        locator = get_search_text_locator(search_value)
        self.scroll_and_click(locator)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

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
