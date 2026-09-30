import allure
import pytest

from test_data import GOOD_ORDER_TEST_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.mark.usefixtures("driver")
class TestMainPage:
    driver = None
    main_page = None
    order_page = None

    @allure.title("Тест успешного заказа")
    @pytest.mark.parametrize(
        "first_name, last_name, address, metro_station, phone, delivery_date, rental_period, color, comment",
        GOOD_ORDER_TEST_DATA
    )
    def test_good_order(
            self,
            driver,
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
        self.main_page = MainPage(driver)
        self.order_page = OrderPage(driver)

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
