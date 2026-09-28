import pytest
from selenium import webdriver

from config import MAIN_URL, GOOD_ORDER_TEST_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestMainPage:
    driver = None
    main_page = None
    order_page = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.main_page = MainPage(cls.driver)
        cls.order_page = OrderPage(cls.driver)
        cls.driver.get(MAIN_URL)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.mark.parametrize(
        "first_name, last_name, address, metro_station, phone, delivery_date, rental_period, color, comment",
        GOOD_ORDER_TEST_DATA
    )
    def test_good_order(
            self,
            first_name,
            last_name,
            address,
            metro_station,
            phone,
            delivery_date,
            rental_period,
            color,
            comment,
    ):
        self.main_page.click_order_btn()
        self.order_page.set_text_to_input("* Имя", first_name)
        self.order_page.set_text_to_input("* Фамилия", last_name)
        self.order_page.set_text_to_input(
            "* Адрес: куда привезти заказ", address
        )
        self.order_page.set_text_to_dropdown_input(
            "* Станция метро", metro_station
        )
        self.order_page.set_text_to_input(
            "* Телефон: на него позвонит курьер", phone
        )

        self.order_page.click_continue_btn()

        self.order_page.set_text_to_input(
            "* Когда привезти самокат", delivery_date
        )
        self.order_page.set_text_to_dropdown_input(
            "* Срок аренды", rental_period
        )
        self.order_page.set_textbox_value(color)
        self.order_page.set_text_to_input("Комментарий для курьера", comment)

        self.order_page.submit_order()

        assert self.order_page.is_text_on_page("Заказ оформлен")

        self.order_page.close_order()
