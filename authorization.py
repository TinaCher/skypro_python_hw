#Откройте страницу http://the-internet.herokuapp.com/login.
#В поле username введите значение tomsmith
#В поле password введите значение SuperSecretPassword!
#Нажмите кнопку Login

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

username=driver.find_element(By.CSS_SELECTOR, "input#username")
username.send_keys("tomsmith")
username=driver.find_element(By.CSS_SELECTOR, "input#password")
username.send_keys("SuperSecretPassword!")
login_click=driver.find_element(By.CSS_SELECTOR, "[type='submit']")
login_click.click()

sleep(10)