"""
Creating statistics aboute the recipes.
"""
import json
class Statistics():
    def __init__(self, recipes_path):
        # Load recipes from the provided path
        with open(recipes_path, 'r') as file:
            data = json.load(file)
        self.recipes = data.get("Recipes", [])

    def get_total_recipes(self):
        return len(self.recipes)

    def get_recipe_names(self):
        recipes = self.recipes.keys()
        return recipes

    def get_average_time(self, rounding = 2):
        time = 0
        if not self.recipes:
            return 0
        names = self.get_recipe_names()
        for name in names:
            time += self.recipes[name].get("time", 0)
        return round(time / len(self.recipes), rounding)

    def get_most_common_machine(self):
        machine_count = {}
        for recipe in self.recipes:
            machine_name = recipe[2]
            if machine_name in machine_count:
                machine_count[machine_name] += 1
            else:
                machine_count[machine_name] = 1
        return max(machine_count, key=machine_count.get)
    
    def get_most_used_raw_materials(self, top=False, topelements=5, reverse=True):
        raw_material_count = {}
    
        # Loop through all recipe objects
        for recipe in self.recipes:
            # Get the input dictionary: {RawMaterial: amount}
            for raw_material, amount in recipe.inputs.items():
                name = raw_material.name
                if name in raw_material_count:
                    raw_material_count[name] += amount
                else:
                    raw_material_count[name] = amount
    
        # Return either the sorted top N materials or the full dictionary
        return sorted(raw_material_count.items(), key=lambda x: x[1], reverse=reverse)[:topelements] if top else raw_material_count
if __name__ == "__main__":
    Statistics = Statistics("Recipes.json")
    print(f"total recipes: {Statistics.get_total_recipes()}")
    # print(f"recipe names: {Statistics.get_recipe_names()}")
    print(f"average time: {Statistics.get_average_time()}")
    print(f"most common machine: {Statistics.get_most_common_machine()}")
    # print(f"most used raw materials: {Statistics.get_most_used_raw_materials()}")
    print(f"most used raw materials: {Statistics.get_most_used_raw_materials(top=True, topelements=5, reverse=True)}")
