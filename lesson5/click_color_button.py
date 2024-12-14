#Откройте страницу http://uitestingplayground.com/classattr.
#Кликните на синюю кнопку.
#Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/classattr")

blue_button = driver.find_element(
    "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
blue_button.click()

sleep(10)
