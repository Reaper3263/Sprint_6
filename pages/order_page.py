from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import SEARCH_INPUT_BY_PLACEHOLDER_LOCATOR, SEARCH_TEXT_LOCATOR, CONTINUE_BTN, ORDER_BTN, TEXTBOX_BTN, \
    YES_BTN, CHECK_STATUS_BTN


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def set_text_to_input(self, text_to_find, text_to_set):
        element = self.driver.find_element(By.XPATH, SEARCH_INPUT_BY_PLACEHOLDER_LOCATOR.format(search_value=text_to_find))
        element.send_keys(text_to_set)
        element.send_keys(Keys.ESCAPE)

    def set_text_to_dropdown_input(self, text_to_find, text_to_set):
        try:
            element = self.driver.find_element(By.XPATH, SEARCH_INPUT_BY_PLACEHOLDER_LOCATOR.format(search_value=text_to_find))
        except NoSuchElementException:
            element = self.driver.find_element(By.XPATH, SEARCH_TEXT_LOCATOR.format(search_value=text_to_find))
        element.click()
        self.driver.find_element(By.XPATH, SEARCH_TEXT_LOCATOR.format(search_value=text_to_set)).click()

    def set_textbox_value(self, check_box_value):
        self.driver.find_element(By.XPATH, TEXTBOX_BTN.format(check_box_value=check_box_value)).click()

    def click_continue_btn(self):
        self.driver.find_element(By.XPATH, CONTINUE_BTN).click()

    def submit_order(self):
        self.driver.find_element(By.XPATH, ORDER_BTN).click()
        self.driver.find_element(By.XPATH, YES_BTN).click()

    def close_order(self):
        self.driver.find_element(By.XPATH, CHECK_STATUS_BTN).click()

    def is_text_on_page(self, text, timeout=5):
        dynamic_xpath = f"//*[contains(text(), '{text}')]"

        try:
            WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located((By.XPATH, dynamic_xpath))
            )
            return True
        except TimeoutException:
            return False
        