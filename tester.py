import random
import json

# Import the Recipe, RawMaterial and Machine objects to test
import Recipe as Recipe
import RawMaterial as RawMaterial
import Machine as Machine

if __name__ == "__main__":
    materials = {}
    def create_materials(materials_list: list):
        for mat_name in materials_list:
            material_obj = RawMaterial.RawMaterial(mat_name)
            materials[mat_name] = material_obj
        # print(materials) for debugging
    reciptes = {}
    def create_reciptes(reciptes_list: list):
        for recipe_data in reciptes_list:
            # print(recipe_data) for debugging
            recipe_data = recipe_data["Pancake"]
            recipe = Recipe.Recipe(
                recipe_data["name"],
                recipe_data["inputs"],
                recipe_data["outputs"],
                recipe_data["machine"],
                recipe_data["time"]
            )
        reciptes[recipe.name] = recipe
        # print the reciptes dictionary to see if it works
        print("Recipes created:")
        for key, value in reciptes.items():
            print(f"{key}: {value}")
    machins = {}
    def create_machine(name: str):
        machine = Machine.Machine(name, "Oven")
        machins[name] = machine

    def generate_random_recipes(n: int):
        # Load recipe data from file
        with open("Recipes.json", "r") as file:
            data = json.load(file)
    
        # Get the dictionary under the "Recipes" key
        recipes_dict = data.get("Recipes", {})
    
        # Get the list of only the recipe values (we don't need the keys here)
        all_recipes = list(recipes_dict.values())
    
        # Validate count
        if n > len(all_recipes):
            raise ValueError(f"Requested {n} recipes, but only {len(all_recipes)} available.")
    
        # Shuffle and pick first n
        random.shuffle(all_recipes)
        selected_recipes = all_recipes[:n]
    
        print(f"Selected {n} random recipes:")
        for recipe in selected_recipes:
            print(f"- {recipe.get('name', 'Unnamed')}")
    
        return selected_recipes
    
    def main(n: int = 5, rounds: int = 5):
        # Create materials
        create_materials(["Wheat", "Egg", "Water", "Sugar", "Milk"])
        # Create recipes
        create_reciptes(generate_random_recipes(n))
        # Create machines
        for i in range(n):
            create_machine(f"Oven_{i+1}")
        # Add raw materials to machines
        for key, value in machins.items():
            value.add_RawMaterial([materials["Wheat"], materials["Egg"], materials["Water"]], 5)
            print(f"{key} has added raw materials")
        # Start recipes on machines
        for key, value in machins.items():
            value.start_recipe(reciptes["Pancake"])
            print(f"{key} has started a recipe")
        for i in range(rounds):
            for key, value in machins.items():
                value.tick()
                print(f"{key} has ticked")
    main(1, 2)
print
