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


class User(Password):
    next_id = 1

    def __init__(self, username, password):
        super().__init__(password)
        self.id = User.next_id
        User.next_id += 1
        self.__username = username
        self.cart = Cart()

    #def __init__(self, username, password):
        #     self.id = User.next_id
        #     User.next_id += 1
        #     self.__username = username
        #     self.__password = self.hash_password(password)
        #     self.cart = Cart()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return 'password1'

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

    def __init__(self, name, price, brand, category, product_id):
        self.name = name
        self.price = price
        self.brand = brand
        self.category = category
        self.product_id = product_id

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

