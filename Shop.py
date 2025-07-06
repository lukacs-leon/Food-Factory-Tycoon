import random
import json
class Shop():
    def __init__(self):
        self.data = self.get_data()
        self.RawMaterials = self.data["Raw Materials"]
        self.AvailableProducts = {}
    def get_data(self):
        with open("Datas.json", "r") as file:
            data = json.load(file)
        return data
    def generate_raw_materials(self, n):
        raw_materials = {}
        for _ in range(n):
            material = random.choice(list(self.RawMaterials.keys()))
            quantity = random.randint(1, 10)
            raw_materials[material] = {
                "Name": material,
                "Quantity": quantity,
                "Price": self.data["Raw Materials"][material]["Price"]
            }
        sliced = []
        for key, value in raw_materials.items():
            pair = {key: value}
            sliced.append(pair)
        return list(sliced)
    def add_raw_materials(self):
        raw_materials = self.generate_raw_materials(5)
        for material in raw_materials:
            material_name = next(iter(material))
            if material_name not in self.AvailableProducts:
                self.AvailableProducts[material_name] = {
                    "Name": material[material_name]["Name"],
                    "Quantity": material[material_name]["Quantity"],
                    "Price": material[material_name]["Price"]
                }
            else:
                self.AvailableProducts[material_name]["Quantity"] += material[material_name]["Quantity"]
            if self.AvailableProducts[material_name]["Quantity"] <= 0:
                del self.AvailableProducts[material_name]
            print(f"Added {material[material_name]["Quantity"]} {material[material_name]["Name"]} at ${material[material_name]["Price"]} each.")

        return raw_materials
    def buy_raw_materials(self, materials):
        can_buy = {}
        print(f"Avaible: {self.AvailableProducts}")
        for material in materials:
            material_name = next(iter(material))
            print(f"Actual material: {material} expected: {material[material_name]["Quantity"]}")
            print(f"Test: {material[material_name]["Name"]}")
            if material[material_name]["Quantity"] <= 0:
                print(f"Cannot buy {material[material_name]["Name"]} with quantity {material[material_name]["Quantity"]}.")
                can_buy[material[material_name]["Name"]] = False
                continue
            if material[material_name]["Name"] not in self.AvailableProducts:
                print(f"{material[material_name]["Name"]} is not available in the shop.")
                can_buy[material[material_name]["Name"]] = False
                continue
            if self.AvailableProducts[material[material_name]["Name"]]["Quantity"] < material[material_name]["Quantity"]:
                print(f"{material[material_name]["Name"]} is not available enough from {material[material_name]["Name"]} (excepted {material[material_name]["Quantity"]} but only {self.AvailableProducts[material[material_name]["Name"]["Quantity"]]} available) in the shop.")
                can_buy[material[material_name]["Name"]] = False
                continue
            else:
                self.AvailableProducts[material[material_name]["Name"]]["Quantity"] -= material[material_name]["Quantity"]
                if self.AvailableProducts[material[material_name]["Name"]]["Quantity"] <= 0:
                    del self.AvailableProducts[material[material_name]["Name"]]
                can_buy[material[material_name]["Name"]] = True
                print(f"Buying {material[material_name]["Quantity"]} of {material[material_name]["Name"]} at ${self.AvailableProducts[material[material_name]["Name"]]["Price"]} price.")
        total_cost = 0
        for material_name, can in can_buy.items():
            print(f"Materials: {materials}")
            print(f"Materials 0: {materials[0]}")
            if not can:
                print(f"Cannot buy {material_name}.")
            else:
                print(f"Successfully bought {material_name}.")
                total_cost += self.AvailableProducts[material_name]["Price"] * materials[0][material_name]["Quantity"]
        print(f"Total cost for buying raw materials: ${total_cost}")
        return total_cost
if __name__ == "__main__":
    Shop = Shop()
    Shop.add_raw_materials()
    Shop.buy_raw_materials(Shop.generate_raw_materials(5))