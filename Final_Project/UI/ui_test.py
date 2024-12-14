from ui_page import MainPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import allure

@pytest.fixture
def browser():
    with allure.step("Open browser"):
        browser = webdriver.Chrome()
        browser.implicitly_wait(4)
        browser.maximize_window()
        yield browser

@allure.id("T-1")
@allure.epic("Chitai-Gorod")
@allure.severity("Major")
@allure.feature("Search")
@allure.title("Searching a book in russian")
def test_search_rus(browser):
    book = "Рецепт"
    page = MainPage(browser)
    page.search(book)
    assert book in page.get_result(book)

@allure.id("T-2")
@allure.epic("Chitai-Gorod")
@allure.severity("Major")
@allure.feature("Search")
@allure.title("Searching a book in english")
def test_search_eng(browser):
    book = "English"
    page = MainPage(browser)
    page.search(book)
    assert book in page.get_result(book)

@allure.id("T-3")
@allure.epic("Chitai-Gorod")
@allure.severity("Major")
@allure.feature("Search")
@allure.title("Searching non-existing request")
def test_no_result_msg(browser):
    page = MainPage(browser)
    page.search("mnsfdfhgogb")
    with allure.step('The message appears'):
        assert page.no_result_msg() == "Похоже, у нас такого нет"

@allure.id("T-4")
@allure.epic("Chitai-Gorod")
@allure.severity("Major")
@allure.feature("Adding to cart")
@allure.title("Adding a book to the cart")
def test_buy_click(browser):
    page = MainPage(browser)
    page.search("english")   
    page.buy_click()
    page.go_cart()
    page.check_cart() == True

@allure.id("T-5")
@allure.epic("Chitai-Gorod")
@allure.severity("Major")
@allure.feature("Delete")
@allure.title("Deleting a book from the cart")
def test_delete_from_cart(browser):
    page = MainPage(browser)
    page.search("english")  
    page.buy_click()
    page.go_cart() 
    page.delete_from_cart()
    page.check_cart() == False
