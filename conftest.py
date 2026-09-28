import pytest
from selenium import webdriver

from config import MAIN_URL


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(MAIN_URL)

    yield driver
    driver.quit()
