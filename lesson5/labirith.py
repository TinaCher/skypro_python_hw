from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://labirint.ru")

input = "input#search-field"
search_input=driver.find_element(By.CSS_SELECTOR, input)
search_input.send_keys("Python")
search_input.send_keys(Keys.RETURN)

books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

for book in books:
    author = book.find_element(By.CSS_SELECTOR, "div.product-card__author").text
    title = book.find_element(By.CSS_SELECTOR, "a.product-card__name").text
    price = book.find_element(By.CSS_SELECTOR, "div.product-card__price-current").text
    print (author + "\t" + title + "\t" + price )
sleep(10)