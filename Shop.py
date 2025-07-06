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
        for material_name, material_data in raw_materials.items():
            if material_name not in self.RawMaterials.keys():
                self.RawMaterials[raw_materials["Name"]] = {
                    "Name": raw_materials["Name"],
                    "Quantity": raw_materials["Quantity"],
                    "Price": raw_materials["Price"]
                }
        return list(raw_materials.values())
    def add_raw_materials(self):
        raw_materials = self.generate_raw_materials(5)
        for material in raw_materials:
            print(f"Added {material["Quantity"]} {material["Name"]} at ${material["Price"]} each.")
        return raw_materials
    def buy_raw_materials(self, materials):
        for material in materials:
            if material["Quantity"] <= 0:
                print(f"Cannot buy {material["Name"]} with quantity {material["Quantity"]}.")
                continue
            print(f"Avaible: {self.AvailableProducts}")
            if material["Name"] not in self.RawMaterials or material["Quantity"] > self.AvailableProducts[material["Name"]]["Quantity"]:
                print(f"{material["Name"]} is not available enough from {material["Name"]} (excepted {material["Quantity"]} but only {self.AvailableProducts[material["Name"]["Quantity"]]} available) in the shop.")
                continue
            print(f"Buying {material["Quantity"]} of {material["Name"]} at ${self.AvailableProducts[material["Name"]]["Price"]} price.")
        total_cost = sum(material["Price"] for material in materials)
        print(f"Total cost for buying raw materials: ${total_cost}")
        return total_cost
if __name__ == "__main__":
    Shop = Shop()
    Shop.add_raw_materials()
    Shop.buy_raw_materials(Shop.generate_raw_materials(5))