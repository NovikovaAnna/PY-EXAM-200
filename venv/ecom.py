import hashlib
import re
import random


class IdCounter:
    def __init__(self):
        self.counter = 0

    def get_id(self):
        self.counter += 1
        return self.counter


class Password:
    def __init__(self, password):
        self.password = password
        self.hash = None

    def get(self):
        if self._validate_password():
            self.hash = hashlib.sha256(self.password.encode()).hexdigest()
            return self.hash

    def check(self, password):
        if self._validate_password() and self.hash == hashlib.sha256(password.encode()).hexdigest():
            return True
        return False

    def _validate_password(self):
        if not isinstance(self.password, str):
            return False
        if len(self.password) < 8:
            return False
        if not re.search('[a-zA-Z]', self.password) or not re.search("[0-9]", self.password):
            return False
        return True


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)


class User:
    _id_counter =IdCounter()

    def __init__(self):
        self._id = self._id_counter.get_id()

    def __init__(self, username, password):
        self.__username = username
        self.__password = Password(password)

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    def __str__(self):
        return f"Username: {self.username}, Cart: {self.cart.products}"

    def __repr__(self):
        return f"User({self.username}, {self.password})"


class Store:
    def __init__(self):
        self.user_basket = {}

    def authenticate(self):
        login = input("Логин: ")
        password = hashlib.sha256(input("Пароль: ").encode()).hexdigest()
        self.user_basket[login] = []

    def add_to_basket(self, product):
        login = input("Логин: ")
        if login in self.user_basket:
            self.user_basket[login].append(product)
        else:
            print("Error: login not found")

        def show_basket(self, login):
            if login in self.user_basket:
                basket = self.user_basket[login]
                if basket:
                    print("Your basket:")
                    for i, item in enumerate(basket):
                        print(f"{i + 1}. {item}")
                else:
                    print("Your basket is empty.")
            else:
                print("Error: login not found")

class Product:
    _id_counter =IdCounter()

    def __init__(self):
        self._id = self._id_counter.get_id()

    def __init__(self, name, price: (int,float), brand, category, product_id:int):
        self.name = name
        self._price = price
        self.brand = brand
        self.category = category
        self._product_id = product_id

    @property
    def price(self) -> (int,float):
        return self._price
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Цена может быть только числом")
        if not  value > 0 :
            raise ValueError("Цена может быть только положительной")
        self._price= value

    @property
    def product_id(self) -> int:
        return self._product_id
    @product_id.setter
    def product_id(self, value):
        if not isinstance(value, int):
            raise TypeError("id продукта может быть только целым числом")
        if not  value > 0 :
            raise ValueError("id продукта может быть только положительным числом")
        self._product_id = value

    def __str__(self):
        return f"{self.name} ({self.brand}), {self.price}$"

product = [
    Product("Lipstick", 15, "Maybelline", "Makeup", 1),
    Product("Eyeliner", 12, "L'Oreal", "Makeup", 2),
    Product("Shampoo", 20, "Pantene", "Hair care", 3),
    Product("Conditioner", 18, "Pantene", "Hair care", 4),
    Product("Foundation", 25, "Nars", "Makeup", 5),
    Product("Blush", 20, "Nars", "Makeup", 6),
    Product("Lotion", 18, "Cetaphil", "Skin care", 7),
    Product("Sunscreen", 25, "Neutrogena", "Skin care", 8)
]

if __name__ == '__main__':
    store = Store()
    while True:
        print("1. Аунтификация")
        print("2. Добавьте продукт в корзину")
        print("3. Смотреть корзину")
        print("4. Выйти")
        choice = int(input("Сделайте свой выбор: "))
        if choice == 1:
            store.authenticate()
        elif choice == 2:
            # product = generate_product()
            product1 = random.choice(product)
            print(product1)
            store.add_to_basket(product1)
        elif choice == 3:
            # login = input("Enter login: ")
            # store.show_basket(login)
            print(product1)
        elif choice == 4:
            print("Спасибо за то, что выбрали нас, будем ждать снова!")
            #sys.exit()
        else:
            print("Invalid choice, try again.")

