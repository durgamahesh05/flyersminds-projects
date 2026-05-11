import json
import os


class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def display_info(self):
        print(f"Product ID : {self.product_id}")
        print(f"Name : {self.name}")
        print(f"Quantity : {self.quantity}")
        print(f"Price : {self.price}")
        print("-" * 30)

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }


class InventorySystem:
    def __init__(self):
        self.file_name = "inventory.json"
        self.product_list = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, "r") as file:
                    data = json.load(file)

                    for product in data:
                        obj = Product(
                            product["product_id"],
                            product["name"],
                            product["quantity"],
                            product["price"]
                        )

                        self.product_list.append(obj)

            except:
                print("Error Loading Data")

    def save_data(self):
        data = [product.to_dict() for product in self.product_list]

        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)

    def add_product(self):
        product_id = input("Enter Product ID: ").strip()
        name = input("Enter Product Name: ").strip()

        if not product_id or not name:
            print("Fields Cannot Be Empty")
            return

        for product in self.product_list:
            if product.product_id == product_id:
                print("Product ID Already Exists")
                return

            if product.name.lower() == name.lower():
                print("Product Name Already Exists")
                return

        try:
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))

            if quantity < 0 or price < 0:
                print("Negative Values Not Allowed")
                return

        except:
            print("Invalid Quantity or Price")
            return

        product = Product(product_id, name, quantity, price)

        self.product_list.append(product)

        self.save_data()

        print("Product Added Successfully")

    def view_products(self):
        if not self.product_list:
            print("No Products Found")
            return

        for product in self.product_list:
            product.display_info()

    def update_product(self):
        product_id = input("Enter Product ID to Update: ").strip()

        for product in self.product_list:
            if product.product_id == product_id:

                new_name = input("Enter New Product Name: ").strip()

                if not new_name:
                    print("Name Cannot Be Empty")
                    return

                for p in self.product_list:
                    if p.name.lower() == new_name.lower() and p.product_id != product_id:
                        print("Product Name Already Exists")
                        return

                try:
                    new_quantity = int(input("Enter New Quantity: "))
                    new_price = float(input("Enter New Price: "))

                    if new_quantity < 0 or new_price < 0:
                        print("Negative Values Not Allowed")
                        return

                except:
                    print("Invalid Quantity or Price")
                    return

                product.name = new_name
                product.quantity = new_quantity
                product.price = new_price

                self.save_data()

                print("Product Updated Successfully")
                return

        print("Product Not Found")

    def delete_product(self):
        product_id = input("Enter Product ID to Delete: ").strip()

        for product in self.product_list:
            if product.product_id == product_id:
                self.product_list.remove(product)

                self.save_data()

                print("Product Deleted Successfully")
                return

        print("Product Not Found")

    def sell_product(self):
        product_id = input("Enter Product ID to Sell: ").strip()

        try:
            sell_quantity = int(input("Enter Quantity to Sell: "))

            if sell_quantity <= 0:
                print("Quantity Must Be Greater Than Zero")
                return

        except:
            print("Invalid Quantity")
            return

        for product in self.product_list:
            if product.product_id == product_id:

                if sell_quantity > product.quantity:
                    print("Insufficient Stock")
                    return

                product.quantity -= sell_quantity

                self.save_data()

                print("Product Sold Successfully")
                print(f"Current Stock : {product.quantity}")
                return

        print("Product Not Found")


system = InventorySystem()

while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Sell Product")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        system.add_product()

    elif choice == "2":
        system.view_products()

    elif choice == "3":
        system.update_product()

    elif choice == "4":
        system.delete_product()

    elif choice == "5":
        system.sell_product()

    elif choice == "6":
        print("Exiting Program")
        break

    else:
        print("Invalid Choice")