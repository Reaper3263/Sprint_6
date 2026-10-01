from selenium.webdriver import Keys
from locators import CONTINUE_BTN, ORDER_BTN, YES_BTN, CHECK_STATUS_BTN, get_textbox_btn_locator,\
    get_search_text_locator, get_search_input_by_placeholder_locator
from pages.base_page import BasePage


class OrderPage(BasePage):
    def set_text_to_input(self, text_to_find, text_to_set):
        locator = get_search_input_by_placeholder_locator(text_to_find)
        self.enter_text(locator, text_to_set, key_to_send=Keys.ESCAPE)

    def set_text_to_dropdown_input(self, text_to_find, text_to_set):
        input_locator = get_search_input_by_placeholder_locator(text_to_find)
        text_locator = get_search_text_locator(text_to_find)

        if self.is_element_present(input_locator):
            self.click(input_locator)
        else:
            self.click(text_locator)

        self.click_searched_text(text_to_set)

    def set_textbox_value(self, check_box_value):
        self.click(get_textbox_btn_locator(check_box_value))

    def click_continue_btn(self):
        self.click(CONTINUE_BTN)

    def submit_order(self):
        self.click(ORDER_BTN)
        self.click(YES_BTN)

    def close_order(self):
        self.click(CHECK_STATUS_BTN)
        