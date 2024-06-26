class Smartphone:
    def __init__(self, brand, model, number):
        self.brand = brand  
        self.model = model
        self.number = number       

    def print_full_char(self):
        print(f"{self.brand}-{self.model}.{self.number}")