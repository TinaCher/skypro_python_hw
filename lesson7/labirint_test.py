from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

cookie = {"name": "cookie_policy", "value": "1"}

browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))

    # Перейти на сайт «Лабиринта»
def open_labirint():
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)
    sleep(5)

    # Найти все книги по слову Python
def search(term):
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

    # Переключиться на таблицу
    # Добавить все книги в корзину и посчитать
def add_books():
    buy_buttons = browser.find_elements(
        By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1
    return counter
    # Перейти в корзину
def go_to_cart():
    browser.get("https://www.labirint.ru/cart/")

    # Проверить счетчик товаров. Должен быть равен числу нажатий
    # Получить текущее значение
def get_cart_counter():
    txt = browser.find_element(
        By.CSS_SELECTOR, "a[data-event-label='myCart']").find_element(By.CSS_SELECTOR, 'b').text
    return int(txt)

def close_driver():
    browser.quit()

def test_cart_counter():
    open_labirint() # Открываем сайт
    search("Python") # Ищем книги по слову 
    added = add_books() # Добавляем книги и сохраняем результат в переменную 
    go_to_cart() # Идем в корзину 
    cart_counter = get_cart_counter() # Забираем значение счетчика из корзины
    assert added == cart_counter # Сравниваем counter со счетчиком корзины
