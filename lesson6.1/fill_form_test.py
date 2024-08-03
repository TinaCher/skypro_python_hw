import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_form_submission():
    driver = webdriver.Chrome()
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        first_name = driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
        first_name.send_keys("Ivan")

        last_name = driver.find_element(By.CSS_SELECTOR, "[name='last-name']")
        last_name.send_keys("Petrov")

        address = driver.find_element(By.CSS_SELECTOR, "[name='address']")
        address.send_keys("Lenina,55-3")

        zip_code = driver.find_element(By.CSS_SELECTOR, "[name='zip-code']")
        zip_code.send_keys("")

        city = driver.find_element(By.CSS_SELECTOR, "[name='city']")
        city.send_keys("Moscow")

        country = driver.find_element(By.CSS_SELECTOR, "[name='country']")
        country.send_keys("Russia")

        email = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']")
        email.send_keys("test@skypro.com")

        phone = driver.find_element(By.CSS_SELECTOR, "[name='phone']")
        phone.send_keys("+7985899998787")

        job_position = driver.find_element(By.CSS_SELECTOR, "[name='job-position']")
        job_position.send_keys("QA")

        company = driver.find_element(By.CSS_SELECTOR, "[name='company']")
        company.send_keys("SkyPro")

        submit = driver.find_element(By.XPATH, '//button[text()="Submit"]')
        submit.click()

        zip_code_alert = driver.find_element(By.CSS_SELECTOR, "#zip-code")
        assert "alert-danger" in zip_code_alert.get_attribute("class")

        zip_code_color = zip_code_alert.value_of_css_property('color')
        expected_zip_code_color = 'rgba(132, 32, 41, 1)' 
        assert zip_code_color == expected_zip_code_color
        
        fields_to_check = [
        "#first-name", "#last-name", "#address", "#city", "#country", "#e-mail", "#phone", "#job-position", "#company"]

        for field in fields_to_check:
            assert "success" in driver.find_element(By.CSS_SELECTOR, field).get_attribute("class")

    finally:
        driver.quit
