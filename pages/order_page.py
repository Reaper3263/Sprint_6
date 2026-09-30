from selenium.common import NoSuchElementException

from selenium.webdriver import Keys
from locators import CONTINUE_BTN, ORDER_BTN, YES_BTN, CHECK_STATUS_BTN, get_textbox_btn_locator,\
    get_search_text_locator, get_search_input_by_placeholder_locator
from pages.base_page import BasePage


class OrderPage(BasePage):
    def set_text_to_input(self, text_to_find, text_to_set):
        element = self.driver.find_element(*get_search_input_by_placeholder_locator(text_to_find))
        element.send_keys(text_to_set)
        element.send_keys(Keys.ESCAPE)

    def set_text_to_dropdown_input(self, text_to_find, text_to_set):
        try:
            element = self.driver.find_element(*get_search_input_by_placeholder_locator(text_to_find))
        except NoSuchElementException:
            element = self.driver.find_element(*get_search_text_locator(text_to_find))
        element.click()
        self.driver.find_element(*get_search_text_locator(text_to_set)).click()

    def set_textbox_value(self, check_box_value):
        self.driver.find_element(*get_textbox_btn_locator(check_box_value)).click()

    def click_continue_btn(self):
        self.driver.find_element(*CONTINUE_BTN).click()

    def submit_order(self):
        self.driver.find_element(*ORDER_BTN).click()
        self.driver.find_element(*YES_BTN).click()

    def close_order(self):
        self.driver.find_element(*CHECK_STATUS_BTN).click()
        