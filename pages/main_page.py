from locators import FIRST_ORDER_BTN, YANDEX_IMG, SCOOTER_IMG
from pages.base_page import BasePage


class MainPage(BasePage):
    def click_order_btn(self):
        self.click(FIRST_ORDER_BTN)

    def click_ya_img(self):
        self.click(YANDEX_IMG)

    def click_scooter_img(self):
        self.click(SCOOTER_IMG)
