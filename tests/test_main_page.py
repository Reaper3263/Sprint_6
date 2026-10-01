import allure
import pytest

from test_data import SEARCH_DATA_MAIN_PAGE
from pages.main_page import MainPage


@pytest.mark.usefixtures("driver")
class TestMainPage:
    @allure.title("Тест кликов по вопросам")
    @pytest.mark.parametrize("search_value, expected_result", SEARCH_DATA_MAIN_PAGE)
    def test_click_questions(self, driver, search_value, expected_result):
        page = MainPage(driver)
        page.click_searched_text(search_value)
        assert page.is_text_on_page(expected_result)
