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
            # print(recipe_data) # for debugging
            print(f"Recipe data: {recipe_data}")  # for debugging
            # Create a Recipe object using the data
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
    def create_machine(name: str, type: str):
        machine = Machine.Machine(name, type)
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
    
    def main(n: int = 5, rounds: int = 10):
        materials_list = [] # e.g. ["flour", "sugar", "egg", "milk"]
        # Create random recipes
        random_recipes = generate_random_recipes(n)
        # Start recipes on machines
        for counter in range(n):
            # create materials to be used in recipes
            test_materials_list = random_recipes[counter]["inputs"]
            for material in test_materials_list:
                if material not in materials_list:
                    materials_list.append(material)
        # Create materials
        create_materials(materials_list)
        # Create recipes
        create_reciptes(random_recipes)
        # Create machines to each recipe
        for recipe in random_recipes:
            # generate a machine for each recipe and checking the machins dictionary to avoid reuse of serial number
            machine_type = recipe["machine"]
            machine_name = machine_type
            last_index_of_searching_type = 0
            last_serial_number = 0
            if machins != {}:
                for i in range(len(machins)):
                    if list(machins.keys())[i].startswith(machine_type):
                        last_index_of_searching_type = i-1
                        last_serial_number = int(list(machins.keys())[i].split("_")[-1])
                machine_name = f"{machine_type}_{last_serial_number + 1}"
            else:
                machine_name = f"{machine_type}_1"
            create_machine(machine_name, machine_type)
        # Add raw materials to machines
        for key, value in machins.items():
            print(f"key: {key} \n value: {value}")
            for material_name, material_obj in materials.items():
                value.add_RawMaterial([material_obj], 10)
        # Start recipes on machines
        for key, value in machins.items():
            recipe_name = random.choice(list(reciptes.keys()))
            recipe_obj = reciptes[recipe_name]
            if value.start_recipe(recipe_obj):
                print(f"{key} has started the recipe: {recipe_name}")
            else:
                print(f"{key} could not start the recipe: {recipe_name}")
        # Simulate the machines ticking
        print("Starting the simulation...")
        for i in range(rounds):
            for key, value in machins.items():
                value.tick()
                print(f"{key} has ticked")
    main(5, 10)