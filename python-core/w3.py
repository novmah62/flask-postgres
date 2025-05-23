import sqlite3

def setup_database():

    conn = sqlite3.connect(':memory:')
    conn.execute('PRAGMA foreign_keys = ON;')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            product TEXT NOT NULL,
            amount REAL NOT NULL,
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        )
    ''')
    conn.commit()
    return conn

def insert_sample_data(conn):

    cursor = conn.cursor()
    customers = [
        (1, "Alice Smith",   "alice@example.com"),
        (2, "Bob Johnson",   "bob@example.com"),
        (3, "Carol Lee",     "carol@example.com"),
        (4, "David Brown",   "david@example.com"),
        (5, "Eve Davis",     "eve@example.com")
    ]

    orders = [
        (1, 1, "Widget",        19.99),
        (2, 1, "Gadget",        29.99),
        (3, 2, "Thingamajig",   9.99),
        (4, 2, "Whatsit",       14.99),
        (5, 2, "Doodad",        4.99),
        (6, 3, "Gizmo",         49.99),
        (7, 3, "Contraption",   24.99),
        (8, 4, "Doohickey",     12.49),
        (9, 4, "Gadget Pro",    99.99),
        (10, 1, "Widget Plus",  39.99)
    ]

    cursor.executemany("INSERT INTO customers VALUES (?, ?, ?)", customers)
    cursor.executemany("INSERT INTO orders    VALUES (?, ?, ?, ?)", orders)
    conn.commit()

def query_orders_with_customers(conn):

    cursor = conn.cursor()
    query = '''
        SELECT orders.id, customers.name, orders.product, orders.amount
        FROM orders
        JOIN customers ON orders.customer_id = customers.id
    '''
    cursor.execute(query)
    rows = cursor.fetchall()
    print("All orders with customer names:")
    for row in rows:
        order_id, customer_name, product, amount = row
        print(f"Order {order_id}: {product} (${amount:.2f}) by {customer_name}")

def query_total_amount_by_customer(conn):

    cursor = conn.cursor()
    query = '''
        SELECT c.name, COALESCE(SUM(o.amount), 0) AS total_amount
        FROM customers AS c
        LEFT JOIN orders AS o ON o.customer_id = c.id
        GROUP BY c.id
    '''
    cursor.execute(query)
    rows = cursor.fetchall()
    print("\nTotal order amount per customer:")
    for row in rows:
        name, total = row
        print(f"{name}: ${total:.2f}")

def main():
    conn = setup_database()
    insert_sample_data(conn)

    query_orders_with_customers(conn)
    query_total_amount_by_customer(conn)
    conn.close()

if __name__ == "__main__":
    main()
