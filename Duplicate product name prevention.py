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

    def save_data(self):
        data = [product.to_dict() for product in self.product_list]

        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)

    def add_product(self):
        product_id = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        quantity = input("Enter Quantity: ")
        price = input("Enter Price: ")

        for product in self.product_list:
            if product.name.lower() == name.lower():
                print("Product Name Already Exists")
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
        product_id = input("Enter Product ID to Update: ")

        for product in self.product_list:
            if product.product_id == product_id:

                new_name = input("Enter New Product Name: ")

                for p in self.product_list:
                    if p.name.lower() == new_name.lower() and p.product_id != product_id:
                        print("Product Name Already Exists")
                        return

                product.name = new_name
                product.quantity = input("Enter New Quantity: ")
                product.price = input("Enter New Price: ")

                self.save_data()

                print("Product Updated Successfully")
                return

        print("Product Not Found")

    def delete_product(self):
        product_id = input("Enter Product ID to Delete: ")

        for product in self.product_list:
            if product.product_id == product_id:
                self.product_list.remove(product)

                self.save_data()

                print("Product Deleted Successfully")
                return

        print("Product Not Found")


system = InventorySystem()

while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")

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
        print("Exiting Program")
        break

    else:
        print("Invalid Choice")
