from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")

username=driver.find_element(By.CSS_SELECTOR, "#user-name")
username.send_keys("standard_user")

password=driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("secret_sauce")

login=driver.find_element(By.CSS_SELECTOR, "#login-button").click()


backpack=driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
t_shirt=driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
onsie=driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

cart=driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link[data-test='shopping-cart-link']").click()
checkout=driver.find_element(By.CSS_SELECTOR, "#checkout").click()

first_name=driver.find_element(By.CSS_SELECTOR, "#first-name")
first_name.send_keys("Tina")

last_name=driver.find_element(By.CSS_SELECTOR, "#last-name")
last_name.send_keys("Che")

zip=driver.find_element(By.CSS_SELECTOR, "#postal-code")
zip.send_keys("111555")

click_cont=driver.find_element(By.CSS_SELECTOR, "#continue").click()

subtotal_element = driver.find_element(By.CSS_SELECTOR, ".summary_subtotal_label[data-test='subtotal-label']")

subtotal_text = subtotal_element.text

subtotal_value = float(re.search(r"\$([0-9]+\.[0-9]{2})", subtotal_text).group(1))

expected_value = 58.29

assert subtotal_value == expected_value

sleep(10)