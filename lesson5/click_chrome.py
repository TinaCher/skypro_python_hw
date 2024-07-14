from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for button in range(5):
    button="[onclick='addElement()']"
    add_button=driver.find_element(By.CSS_SELECTOR, button)
    add_button.send_keys(Keys.RETURN)

delete_buttons=driver.find_elements(By.CSS_SELECTOR, "[onclick='deleteElement()']")

print (len(delete_buttons))

sleep(10)