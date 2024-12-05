class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        print(self.name, self.weight, self.category)


class Shop():
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        a = file.read()
        file.close()
        return a

    def add(self, *products):
        list_ = self.get_products()
        for i in list_:
            if self.





s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())