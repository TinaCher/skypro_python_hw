from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import re


class Shop:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.saucedemo.com/")

    def login_fill(self, element, value):
        self.browser.find_element(By.ID, element).send_keys(value)

    def submit(self):
        self.browser.find_element(By.ID, "login-button").click()

    def choose_product(self, element):
        self.browser.find_element(By.ID, element).click()

    def go_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, "a.shopping_cart_link[data-test='shopping-cart-link']").click()
     
    def checkout(self):
        self.browser.find_element(By.ID, "checkout").click()

    def fill_form(self, element, value):
        self.browser.find_element(By.ID, element).send_keys(value)

    def  click_cont (self):
        self.browser.find_element(By.CSS_SELECTOR, "#continue").click()

    def total_value(self):
        total_text = self.browser.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        total_value = float(re.search(r"\$([0-9]+\.[0-9]{2})", total_text).group(1))
        return total_value
    