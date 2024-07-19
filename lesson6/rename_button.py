from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

waiter = WebDriverWait(driver, 15, 0.1)

driver.get("http://uitestingplayground.com/textinput")

new_name = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
new_name.send_keys("SkyPRO")

waiter.until(
    EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, "#newButtonName"), "SkyPRO")
)

update_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
update_button.click()

driver.quit()
