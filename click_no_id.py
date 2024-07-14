from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/dynamicid")

button_locator = "[class='btn btn-primary']"
click_button = driver.find_element(By.CSS_SELECTOR, button_locator)
click_button.send_keys(Keys.RETURN)

sleep(10)
