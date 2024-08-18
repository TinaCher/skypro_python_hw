import requests
import allure

class SearchApi:
    def __init__(self, url):
        self.url = url

    @allure.step('Search for books in russian')
    def by_name_rus(self):
        resp = requests.get(self.url + '/recommend/semantic?phrase=Рецепты&perPage=48')
        return resp.json()
    
    @allure.step('Search for books in endlish')
    def by_name_eng(self):
        resp = requests.get(self.url + '/recommend/semantic?phrase=English&perPage=48')
        return resp.json()
    
    @allure.step('Search by not existing name')
    def not_existing_name(self):
        resp = requests.get(self.url + '/recommend/semantic?phrase=mnsfdfhgogb&perPage=48')
        return resp.json()

    @allure.step('Search by book id')
    def by_id(self):
        resp = requests.get(self.url + '/recommend/semantic?phrase=recepty-na-kazhdyy-den-3026718&perPage=48')
        return resp.json()
    
    @allure.step('Display list of shops')
    def shop_cities(self):
        resp = requests.get(self.url + '/shops-cities')
        return resp.json()

    def cart(self):
        resp = requests.post(self.url + '/cart/product')
        return resp.json()
