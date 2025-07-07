import random
import json

class Shop:
    def __init__(self, create_product_per_tick):
        self.data = self.load_data()
        self.raw_material_catalog = self.data["Raw Materials"]
        self.available_products = {}
        self.create_product_per_tick = create_product_per_tick

    def load_data(self):
        with open("Datas.json", "r") as file:
            return json.load(file)

    def generate_random_raw_materials(self, n):
        if n is None:
            n = self.create_product_per_tick
        selected_materials = {}
        for _ in range(n):
            name = random.choice(list(self.raw_material_catalog.keys()))
            quantity = random.randint(1, 10)
            price = self.raw_material_catalog[name]["Price"]

            selected_materials[name] = {
                "Name": name,
                "Quantity": quantity,
                "Price": price
            }

        sliced_materials = [{name: details} for name, details in selected_materials.items()]
        return sliced_materials

    def add_raw_materials_to_inventory(self, n=None):
        new_materials = self.generate_random_raw_materials(n)

        for material in new_materials:
            name = next(iter(material))
            quantity = material[name]["Quantity"]
            price = material[name]["Price"]

            if name not in self.available_products:
                self.available_products[name] = {
                    "Name": name,
                    "Quantity": quantity,
                    "Price": price
                }
            else:
                self.available_products[name]["Quantity"] += quantity

            print(f"Added {quantity} of {name} at ${price} each.")

        return new_materials

    def buy_raw_materials(self, requested_materials):
        purchase_results = {}
        total_cost = 0

        print(f"Available inventory: {self.available_products}")

        for request in requested_materials:
            name = next(iter(request))
            requested_quantity = request[name]["Quantity"]

            if requested_quantity <= 0:
                print(f"Cannot buy {name} with invalid quantity: {requested_quantity}.")
                purchase_results[name] = False
                continue

            if name not in self.available_products:
                print(f"{name} is not available in the shop.")
                purchase_results[name] = False
                continue

            available_quantity = self.available_products[name]["Quantity"]
            price_per_unit = self.available_products[name]["Price"]

            if requested_quantity > available_quantity:
                print(f"Not enough {name} in stock: requested {requested_quantity}, available {available_quantity}.")
                purchase_results[name] = False
                continue

            # Proceed with purchase
            self.available_products[name]["Quantity"] -= requested_quantity
            if self.available_products[name]["Quantity"] <= 0:
                del self.available_products[name]

            cost = price_per_unit * requested_quantity
            total_cost += cost
            purchase_results[name] = True

            print(f"Bought {requested_quantity} of {name} at ${price_per_unit} each. Cost: ${cost}")

        print(f"Total cost: ${total_cost}")
        return total_cost
    def tick(self): # here we'll generate new products and make other things
        print("Tick: Generating new products and updating inventory.")
        new_products = self.generate_random_raw_materials(self.create_product_per_tick)
        for product in new_products:
            name = next(iter(product))
            quantity = product[name]["Quantity"]
            price = product[name]["Price"]

            if name not in self.available_products:
                self.available_products[name] = {
                    "Name": name,
                    "Quantity": quantity,
                    "Price": price
                }
            else:
                self.available_products[name]["Quantity"] += quantity

            print(f"Generated {quantity} of {name} at ${price} each.")

if __name__ == "__main__":
    shop = Shop(20)
    shop.add_raw_materials_to_inventory()
    materials_to_buy = shop.generate_random_raw_materials(5)
    shop.buy_raw_materials(materials_to_buy)
