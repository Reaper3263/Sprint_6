import pytest
from selenium import webdriver

from config import MAIN_URL


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Firefox()
    driver.get(MAIN_URL)

    yield driver
    driver.quit()
