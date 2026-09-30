import allure

from config import MAIN_URL, YA_URL
from pages.main_page import MainPage


class TestMainPage:
    @allure.title("Тест клика на Самокат")
    def test_scooter_page(self, driver):
        page = MainPage(driver)
        page.click_order_btn()
        page.click_scooter_img()
        assert page.get_current_url() == MAIN_URL

    @allure.title("Тест клика на логотип Яндекс")
    def test_ya_page(self, driver):
        page = MainPage(driver)
        page.click_ya_img()
        page.switch_to_window(-1)
        page.wait_for_link_to_open(YA_URL)
        assert page.get_current_url() == YA_URL
