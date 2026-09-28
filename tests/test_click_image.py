from selenium import webdriver

from config import MAIN_URL, YA_URL
from pages.main_page import MainPage


class TestMainPage:
    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(MAIN_URL)
        cls.page = MainPage(cls.driver)

    def test_scooter_page(self):
        self.page.click_order_btn()
        self.page.click_scooter_img()
        self.page.wait_for_link_to_open(MAIN_URL)
        assert self.driver.current_url == MAIN_URL

    def test_ya_page(self):
        self.page.click_ya_img()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.page.wait_for_link_to_open(YA_URL)
        assert self.driver.current_url == YA_URL

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
