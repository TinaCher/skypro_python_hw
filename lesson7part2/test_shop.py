from pages.Shop import Shop
from selenium import webdriver
from time import sleep


def test_shop():
    browser = webdriver.Chrome()
    browser.maximize_window()
    page = Shop(browser)

    page.login_fill("user-name", "standard_user")
    page.login_fill("password", "secret_sauce")
    page.submit()

    page.choose_product("add-to-cart-sauce-labs-backpack")
    page.choose_product("add-to-cart-sauce-labs-bolt-t-shirt")
    page.choose_product("add-to-cart-sauce-labs-onesie")
    page.go_cart()
    page.checkout()

    page.fill_form("first-name", "Tina")
    page.fill_form("last-name", "Che")
    page.fill_form("postal-code", "111555")
    page.click_cont()

    assert page.total_value() == 58.29
       