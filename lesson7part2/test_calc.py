from pages.CalcMain import Calc
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


def test_form():
    browser = webdriver.Chrome()
    browser.maximize_window()
    page = Calc(browser)

    page.click_digit("//span[text() = '7']")
    page.click_digit("//span[text() = '+']")
    page.click_digit("//span[text() = '8']")
    page.click_digit("//span[text() = '=']")

    page.slow("delay", "45")

    page.wait("15")

    sleep(5)