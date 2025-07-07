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
            material_quantity = material[material_name]["Quantity"]
            if material_name not in self.AvailableProducts:
                self.AvailableProducts[material_name] = {
                    "Name": material_name,
                    "Quantity": material_quantity,
                    "Price": material[material_name]["Price"]
                }
            else:
                avaible_material_quantity = self.AvailableProducts["Quantity"]
                avaible_material_quantity += material_quantity
                if avaible_material_quantity <= 0:
                    del self.AvailableProducts[material_name]
            print(f"Added {material_quantity} {material_name} at ${material[material_name]["Price"]} each.")

        return raw_materials
    def buy_raw_materials(self, materials):
        can_buy = {}
        print(f"Avaible: {self.AvailableProducts}")
        for material in materials:
            material_name = next(iter(material))
            material_name = material_name
            material_quantity = material[material_name]["Quantity"]
            if material_name in self.AvailableProducts:
                avaible_material_quantity = self.AvailableProducts[material_name]["Quantity"]
                material_price = self.AvailableProducts[material_name]["Price"]
            print(f"Actual material: {material} expected: {material_quantity}")
            print(f"Test: {material_name}")
            # print(f"test 0: {material[material_name][0]}")
            if material_quantity <= 0:
                print(f"Cannot buy {material_name} with quantity {material_quantity}.")
                can_buy[material_name] = False
                continue
            elif material_name not in self.AvailableProducts:
                print(f"{material_name} is not available in the shop.")
                can_buy[material_name] = False
                continue
            elif avaible_material_quantity < material_quantity:
                print(f"{material_name} is not available enough from {material_name} (excepted {material_quantity} but only {self.AvailableProducts[material_name]["Quantity"]} available) in the shop.")
                can_buy[material_name] = False
                continue
            else:
                avaible_material_quantity -= material_quantity
                if avaible_material_quantity <= 0:
                    del self.AvailableProducts[material_name]
                can_buy[material_name] = True
                print(f"Buying {material_quantity} of {material_name} at ${self.AvailableProducts[material_name]["Price"]} price.")
        total_cost = 0
        for material_name, can in can_buy.items():
            print(f"Materials: {materials}")
            print(f"Materials 0: {materials[0]}")
            if not can:
                print(f"Cannot buy {material_name}.")
            else:
                print(f"Successfully bought {material_name}.")
                print(materials[0])
                total_cost += self.AvailableProducts[material_name]["Price"] * material_quantity
        print(f"Total cost for buying raw materials: ${total_cost}")
        return total_cost
if __name__ == "__main__":
    Shop = Shop()
    Shop.add_raw_materials()
    Shop.buy_raw_materials(Shop.generate_raw_materials(5))