import sqlite3


class ProductTable:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_table(self):
        with self.db_connection:
            self.db_connection.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    product_id INTEGER PRIMARY KEY,
                    name TEXT,
                    price REAL
                )
            ''')

    def add_product(self, name, price):
        with self.db_connection:
            self.db_connection.execute('''
            INSERT INTO products (name, price) VALUES (?,?)
            ''', (name, price))

    def apply_discount(self, product_id, discount):
        with self.db_connection:
            self.db_connection.execute('''
            UPDATE products
            SET price = price - (price * ? / 100)
            WHERE product_id = ?
            ''', (discount, product_id))

    def get_total_price(self):
        value = self.db_connection.execute('''
        SELECT SUM(price) FROM products
        ''')
        return value.fetchone()[0]


db_connection = sqlite3.connect(':memory:')
product_table = ProductTable(db_connection)
product_table.create_table()
product_table.add_product("Laptop", 1500)
product_table.add_product("Mouse", 50)
product_table.apply_discount(1, 10)

print(f"Total price: {product_table.get_total_price()}")  #
