from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Calc():
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def click_digit(self, element):
         self.browser.find_element(By.XPATH, element).click()


    def slow(self, element, value):
        self.browser.find_element(By.ID, element).send_keys(value)

    def wait(self, value):
        WebDriverWait(self.browser, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), value))