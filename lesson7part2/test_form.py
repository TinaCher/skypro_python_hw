from pages.MainPage import MainPage
from selenium import webdriver
from time import sleep


def test_form():
    browser = webdriver.Chrome()
    browser.maximize_window()
    page = MainPage(browser)

    page.fill_fields("first-name", "Ivan")
    page.fill_fields("last-name", "Petrov")
    page.fill_fields("address", "Lenina,55-3")
    page.fill_fields("zip-code", "")
    page.fill_fields("city", "Moscow")
    page.fill_fields("country", "Russia")
    page.fill_fields("e-mail", "test@skypro.com")
    page.fill_fields("phone", "+7985899998787")
    page.fill_fields("job-position", "QA")
    page.fill_fields("company", "SkyPro")

    page.submit()

    assert "success" in page.check("first-name")
    assert "success" in page.check("last-name")
    assert "success" in page.check("address")
    assert "danger" in page.check("zip-code")
    assert "success" in page.check("city")
    assert "success" in page.check("country")
    assert "success" in page.check("e-mail")
    assert "success" in page.check("phone")
    assert "success" in page.check("phone")
    assert "success" in page.check("job-position")
    assert "success" in page.check("company")

    sleep(5)