
# 19-m
class Product:
    def __init__(self, name, price, brand):
        self.name = name
        self.price = price
        self.brand = brand


class Laptop(Product):
    def __init__(self, name, price, brand, ram, cpu, storage):
        super().__init__(name, price, brand)
        self.ram = ram
        self.cpu = cpu
        self.storage = storage

    def show_info(self):
        print(self.name, self.price, self.brand, self.ram, self.cpu, self.storage)


l = Laptop("HP", 800, "HP", "8GB", "i5", "256GB")
l.show_info()

