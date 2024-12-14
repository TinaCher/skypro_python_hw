from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,  TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure

class MainPage:

    def set_cookie_policy(self):
        cookie = {"name": "Cookie_policy", "value": "1"}
        self.browser.add_cookie(cookie)

    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.chitai-gorod.ru/")

    @allure.step('Search for books')
    def search(self, value):
        self.browser.find_element(By.CSS_SELECTOR, ".header-search__input").send_keys(value, Keys.ENTER)

    @allure.step('Check no result message')
    def no_result_msg(self):
        WebDriverWait(self.browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h4.catalog-empty-result__header"))
    )
        return self.browser.find_element(By.CSS_SELECTOR, "h4.catalog-empty-result__header").text
        
    @allure.step('Add to cart')
    def buy_click(self):
        WebDriverWait(self.browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.button.action-button.blue"))
        )
        button = self.browser.find_element(By.CSS_SELECTOR, "div.button.action-button.blue")
        self.browser.execute_script("arguments[0].click();", button)

    @allure.step('Open cart')
    def go_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, ".header-cart__icon.header-cart__icon--desktop").click()

    @allure.step('Open cart')
    def delete_from_cart(self):
        WebDriverWait(self.browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".button.cart-item__actions-button.cart-item__actions-button--delete.light-blue"))
        )
        self.browser.find_element(By.CSS_SELECTOR, ".button.cart-item__actions-button.cart-item__actions-button--delete.light-blue").click()
    
    @allure.step('Check search result')
    def get_result(self, value):
        WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.product-title__head"), value))
        return self.browser.find_element(
            By.CSS_SELECTOR, 'div.product-title__head').text
    
    @allure.step('Check cart')
    def check_cart(self) -> bool:
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.product-title__head')))
        except TimeoutException:
            return False
        return True
       