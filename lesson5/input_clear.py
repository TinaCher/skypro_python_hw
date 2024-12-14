from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")
input_field=driver.find_element(By.CSS_SELECTOR, "[type='number']")
input_field.send_keys("1000")
sleep(2)
input.clear()
input.send_keys("999")
sleep(10)