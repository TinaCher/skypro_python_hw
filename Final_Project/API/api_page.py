import requests
import allure

class ChitaiGorodApi:
    
    def __init__(self, url, token):
        self.url = url
        self.token = token

    def _get_headers(self):
        return {'Authorization': f"Bearer {self.token}"}

    @allure.step('Search for books')
    def by_name(self, value):
        headers = self._get_headers()
        params = {"phrase": value}
        resp = requests.get(self.url + '/recommend/semantic', headers=headers, params=params)
        return resp

    @allure.step('Add book to cart')
    def add_cart(self):
        headers = self._get_headers()
        data = {
            "id": 2676103,
            "adData": {
            "item_list_name": "product-page"
        }}
        resp = requests.post(self.url + '/cart/product', headers=headers, json=data)
        return resp

    @allure.step('Check books in cart')
    def check_cart(self):
        headers = self._get_headers()
        resp_cart = requests.get(self.url + '/cart', headers=headers)
        return resp_cart
    
    @allure.step('Clear cart')
    def clear_cart(self):
        headers = self._get_headers()
        resp_cart = requests.delete(self.url + '/cart', headers=headers)
        return resp_cart