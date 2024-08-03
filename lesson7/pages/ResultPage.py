from selenium.webdriver.common.by import By

class ResultPage:

    def __init__(self, driver):
        self.driver = driver

    def add_books(self):
        buy_buttons = self.driver.find_elements(
        By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")

        counter = 0
        for btn in buy_buttons:
            btn.click()
            counter += 1
        return counter