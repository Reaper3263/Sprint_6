import pytest
from selenium import webdriver

from config import MAIN_URL, SEARCH_DATA_MAIN_PAGE
from pages.main_page import MainPage


class TestMainPage:
    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(MAIN_URL)
        cls.page = MainPage(cls.driver)

    @pytest.mark.parametrize("search_value, expected_result", SEARCH_DATA_MAIN_PAGE)
    def test_click_questions(self, search_value, expected_result):
        self.page.click_searched_text(search_value)
        assert self.page.is_text_on_page(expected_result)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
