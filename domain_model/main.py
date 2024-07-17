class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def apply_discount(self, discount):
        self.price -= self.price * discount / 100


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def remove_item(self, product, quantity):
        self.items.remove((product, quantity))

    def total_price(self):
        return sum(item[0].price * item[1] for item in self.items)


product_1 = Product(1, "Banana", 100)
product_2 = Product(2, "Apple", 50)

cart = ShoppingCart()
# Add products
cart.add_item(product_1, 1)
cart.add_item(product_2, 2)

# Remove product
cart.remove_item(product_1, 1)

# Apply discount
product_2.apply_discount(10)

# Calculation total price
total_price = cart.total_price()
print(total_price)
