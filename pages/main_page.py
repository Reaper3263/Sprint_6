from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import SEARCH_TEXT_LOCATOR, FIRST_ORDER_BTN


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def __scroll_and_click(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def is_text_on_page(self, text, timeout=5):
        dynamic_xpath = f"//*[contains(text(), '{text}')]"

        try:
            WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located((By.XPATH, dynamic_xpath))
            )
            return True
        except TimeoutException:
            return False

    def click_searched_text(self, search_value):
        element = self.driver.find_element(By.XPATH, SEARCH_TEXT_LOCATOR.format(search_value=search_value))
        self.__scroll_and_click(element)

    def click_order_btn(self):
        self.driver.find_element(By.XPATH, FIRST_ORDER_BTN).click()

    def click_ya_img(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//img[@alt='Yandex']"))
        ).click()

    def click_scooter_img(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//img[@alt='Scooter']"))
        ).click()

    def wait_for_link_to_open(self, expected_url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(expected_url))
