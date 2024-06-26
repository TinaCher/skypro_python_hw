from gettext import Catalog
from smartphone import Smartphone

catalog = [
    Smartphone("Nokia", "3310", "+7925302315"),
    Smartphone("Samsung", "Galaxy S21", "+79266306667"),
    Smartphone("Apple", "iPhone 15 Pro", "+79104125546"),
    Smartphone("Huawei", "P40 Pro", "+79261112233"),
    Smartphone("Sony", "Xperia Z5", "+79334445566")
]

for phone in catalog:
    phone.print_full_char()
