from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.chitai-gorod.ru/")

    def search(self, value):
        self.browser.find_element(By.CSS_SELECTOR, ".header-search__input").send_keys(value)
    
    def submit(self):
        self.browser.find_element(By.CSS_SELECTOR, ".header-search__button").click()

    def no_result_msg(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".catalog-empty-result__description h4.catalog-empty-result__header").text
    
    def buy_click(self):
        self.browser.find_element(By.XPATH, "//span[text()='Купить']")[0].click()

    def go_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, ".header-cart__icon header-cart__icon--desktop").click()

    def delete_from_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, ".button cart-item__actions-button cart-item__actions-button--delete light-blue")[0].click()