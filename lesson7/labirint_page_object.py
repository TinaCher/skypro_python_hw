from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage

def test_cart_counter(): 
    browser = webdriver.Chrome() #Открываем браузер
    main_page = MainPage(browser) #Переменная хранит экземпляр класса MainPage
    main_page.set_cookie_policy() #Вызываем метод set_cookie_policy из MainPage

    result_page = ResultPage(browser)
    # result_page.switch_to_table()  #Используем только в видео
    to_be = result_page.add_books()

    cart_page = CartPage(browser)
    cart_page.get() #Переход на страницу с корзиной
    as_is = cart_page.get_counter() #Текущее значение счетчика на странице 

    assert as_is == to_be #Сравниваем значения счетчика с вернувшимся кол-вом книг
    browser.quit()