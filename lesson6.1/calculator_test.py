from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_slow_calculator():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    waiter = WebDriverWait(driver, 50, 0.1)
    
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        click_7 = driver.find_element(By.XPATH, "//span[contains(@class, 'btn btn-outline-primary') and text()='7']")
        click_7.click()

        click_add = driver.find_element(By.XPATH, "//span[contains(@class, 'btn btn-outline-success') and text()='+']")
        click_add.click()

        click_8 = driver.find_element(By.XPATH, "//span[contains(@class, 'btn btn-outline-primary') and text()='8']")
        click_8.click()

        click_result = driver.find_element(By.XPATH, "//span[contains(@class, 'btn btn-outline-warning') and text()='=']")
        click_result.click()

        slow = driver.find_element(By.CSS_SELECTOR, "#delay")
        slow.send_keys("45")

        waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))

        # Sleep to allow visual confirmation if needed
        sleep(3)

    finally:
        driver.quit()
