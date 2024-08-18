import pytest
import allure
from api_page import SearchApi

api = SearchApi('https://web-gate.chitai-gorod.ru/api/v1')

@allure.severity("Major")
@allure.id("T-1")
@allure.feature("Search")
@allure.title("Search by book name in russian")
def test_by_name_rus():
    body = api.by_name_rus()
    assert len(body) > 0

@allure.severity("Major")
@allure.id("T-2")
@allure.feature("Search")
@allure.title("Search by book name in english")
def test_by_name_eng():
    body = api.by_name_rus()
    assert len(body) > 0

@allure.severity("Major")
@allure.id("T-3")
@allure.feature("Search")
@allure.title("Search not existing name")
def test_not_existing():
    body = api.not_existing_name()
    assert len(body) < 0

@allure.severity("Normal")
@allure.id("T-4")
@allure.feature("Search")
@allure.title("Search by book id")
def test_by_id():
    body = api.by_id()
    assert len(body) > 0 


@allure.severity("Normal")
@allure.id("T-5")
@allure.feature("List of shops")
@allure.title("Display list of shops")
def test_shop_list():
    body = api.shop_cities()
    assert len(body) > 0 


def test_add_cart():
    body = api.cart()
    assert 