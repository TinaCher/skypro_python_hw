from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    def fill_fields(self, element, value):
        self.browser.find_element(By.NAME, element).send_keys(value)

    def submit(self):
        WebDriverWait(self.browser,40,0.1).until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()

    def check(self, element):
         return self.browser.find_element(By.ID, element).get_attribute("class")
