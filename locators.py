from selenium.webdriver.common.by import By

CONTINUE_BTN = (By.XPATH, "//button[text()='Далее']")
FIRST_ORDER_BTN = (By.XPATH, ".//button[text()='Заказать']")
ORDER_BTN = (By.XPATH, "//div[contains(@class, 'Order_Content')]//button[text()='Заказать']")
YES_BTN = (By.XPATH, "//button[text()='Да']")
CHECK_STATUS_BTN = (By.XPATH, "//button[text()='Посмотреть статус']")

YANDEX_IMG = (By.XPATH, "//img[@alt='Yandex']")
SCOOTER_IMG = (By.XPATH, "//img[@alt='Scooter']")


def get_search_text_locator(search_value):
    return By.XPATH, f"//div[text()='{search_value}']"


def get_search_input_by_placeholder_locator(search_value):
    return By.XPATH, f"//input[@placeholder='{search_value}']"


def get_search_input_by_text_locator(search_value):
    return By.XPATH, f"//input[text()='{search_value}']"


def get_textbox_btn_locator(check_box_value):
    return By.XPATH, f"//label[contains(text(), '{check_box_value}')]/input"
