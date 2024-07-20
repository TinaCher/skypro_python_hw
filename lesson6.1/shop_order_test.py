from time import sleep
import re
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_sauce_demo_cart_total():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    try:
        driver.get("https://www.saucedemo.com/")

        username = driver.find_element(By.CSS_SELECTOR, "#user-name")
        username.send_keys("standard_user")

        password = driver.find_element(By.CSS_SELECTOR, "#password")
        password.send_keys("secret_sauce")

        login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")
        login_button.click()

        sleep(1)  # Small delay to allow page to load

        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

        cart = driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link[data-test='shopping-cart-link']")
        cart.click()
        
        sleep(1)  # Small delay to allow page to load

        checkout = driver.find_element(By.CSS_SELECTOR, "#checkout")
        checkout.click()

        sleep(1)  # Small delay to allow page to load

        first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
        first_name.send_keys("Tina")

        last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
        last_name.send_keys("Che")

        zip_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
        zip_code.send_keys("111555")

        click_cont = driver.find_element(By.CSS_SELECTOR, "#continue")
        click_cont.click()

        sleep(1)  # Small delay to allow page to load

        subtotal_element = driver.find_element(By.CSS_SELECTOR, ".summary_subtotal_label[data-test='subtotal-label']")
        subtotal_text = subtotal_element.text
        subtotal_value = float(re.search(r"\$([0-9]+\.[0-9]{2})", subtotal_text).group(1))

        expected_value = 58.29
        assert subtotal_value == expected_value, f"Expected subtotal to be {expected_value}, but got {subtotal_value}"
    finally:
        sleep(3)
        driver.quit()

if __name__ == "__main__":
    pytest.main()
