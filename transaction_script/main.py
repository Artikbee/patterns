def apply_discount(product, discount):
    product['price'] -= product['price'] * discount / 100


def add_item(cart, product, quantity):
    cart.append((product, quantity))


def total_price(cart):
    return sum(item[0]['price'] * item[1] for item in cart)


product_1 = {"product_id": 1, "name": "Banana", "price": 100}
product_2 = {"product_id": 2, "name": "Apple", "price": 50}

cart = []
# Add products
add_item(cart, product_1, 1)
add_item(cart, product_2, 2)

# Apply discount
apply_discount(product_1, 10)

# Calculation total price
total_price = total_price(cart)
print(total_price)
