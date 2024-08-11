from ui_page import MainPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def test_search_rus():
    browser = webdriver.Chrome()
    browser.maximize_window()
    page = MainPage(browser)

    page.search("рецепты")
    page.submit()


def test_search_eng():
    browser = webdriver.Chrome()
    browser.maximize_window()
    page = MainPage(browser)

    page.search("python")
    page.submit()

def test_no_result_msg():
    browser = webdriver.Chrome()
    browser.maximize_window()
    page = MainPage(browser)

    page.search("mnsfdfhgogb")
    page.submit()
    assert page.no_result_msg() == "Похоже, у нас такого нет"

def test_buy_click():
    browser = webdriver.Chrome()
    browser.maximize_window()
    page = MainPage(browser)

    page.search("python")
    page.submit()
    WebDriverWait(browser, 5)    
    page.buy_click()


def test_delete_from_cart():
    browser = webdriver.Chrome()
    browser.maximize_window()
    page = MainPage(browser)

    page.search("python")
    page.submit()
    WebDriverWait(browser, 5)    
    page.buy_click()
    page.go_cart() 
    page.delete_from_cart()
