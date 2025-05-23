import json


class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {'name': self.name, 'price': self.price, 'quantity': self.quantity}


def main():
    input_file = "products.txt"
    output_file = "products.json"
    products = []

    try:
        with open(input_file, 'r') as file:
            for line in file:
                if not line.strip():
                    continue
                parts = line.strip().split(',')
                if len(parts) != 3:
                    raise ValueError(f"Invalid format in line: '{line.strip()}'")
                name = parts[0].strip()
                price_str = parts[1].strip()
                quantity_str = parts[2].strip()

                price = float(price_str)
                quantity = int(quantity_str)

                products.append(Product(name, price, quantity))
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return
    except ValueError as ve:
        print(f"Data error: {ve}")
        return

    try:
        with open(output_file, 'w') as json_file:
            json.dump([p.to_dict() for p in products], json_file, indent=2)
        print(f"Successfully wrote {len(products)} products to '{output_file}'.")
    except IOError as ioe:
        print(f"File write error: {ioe}")


if __name__ == "__main__":
    main()
