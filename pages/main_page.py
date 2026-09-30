from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import FIRST_ORDER_BTN, YANDEX_IMG, SCOOTER_IMG
from pages.base_page import BasePage


class MainPage(BasePage):
    def click_order_btn(self):
        self.driver.find_element(*FIRST_ORDER_BTN).click()

    def click_ya_img(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(YANDEX_IMG)
        ).click()

    def click_scooter_img(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(SCOOTER_IMG)
        ).click()
