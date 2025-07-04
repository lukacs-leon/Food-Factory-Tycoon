"""
Creating statistics aboute the recipes.
"""
class Statistics():
    def __init__(self, recipes):
        self.recipes = recipes

    def get_total_recipes(self):
        return len(self.recipes)

    def get_recipe_names(self):
        return [recipe.name for recipe in self.recipes]

    def get_average_time(self):
        if not self.recipes:
            return 0
        total_time = sum(recipe.time for recipe in self.recipes)
        return total_time / len(self.recipes)

    def get_most_common_machine(self):
        machine_count = {}
        for recipe in self.recipes:
            if recipe.machine in machine_count:
                machine_count[recipe.machine] += 1
            else:
                machine_count[recipe.machine] = 1
        return max(machine_count, key=machine_count.get)
    
    def get_most_used_raw_materials(self, top = False, topelements = 5, reverse = True, ):
        raw_material_count = {}
        for recipe in self.recipes:
            for input_item in recipe.inputs:
                if input_item.name in raw_material_count:
                    raw_material_count[input_item.name] += input_item.amount
                else:
                    raw_material_count[input_item.name] = input_item.amount
        return sorted(raw_material_count.items(), key=lambda x: x[1], reverse=True)