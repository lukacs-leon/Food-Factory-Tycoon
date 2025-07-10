# import the modules what we coded
from Shop import Shop
from Statistics import Statistics
from Machine import Machine
from Recipe import Recipe
# import the other modules
from json import load
import random
class Main():
    def __init__(self, rounds=100):
        self.shop = Shop(create_product_per_tick=5)
        self.statistics = Statistics("Recipes.json")
        self.machines_data = {}
        self.machines = {}
        self.recipes = {}
        self.recipes_names = []
        self.current_recipes = []
        self.raw_materials = {}
        self.rounds = rounds
        self.current_round = 0
        self.load_data()
        self.shop.add_raw_materials_to_inventory()  # Add initial raw materials to inventory
    
    def load_data(self):
        with open("Datas.json", "r") as file:
            data = load(file)
        
        # Load raw materials
        for name, details in data["Raw Materials"].items():
            self.raw_materials[name] = details
        
        # Load recipes
        with open("Recipes.json", "r") as file:
            recipe_data = load(file)
        for recipe_data in recipe_data["Recipes"].values():
            recipe_name = recipe_data["name"]
            recipe_inputs = recipe_data["inputs"]
            recipe_outputs = recipe_data["outputs"]
            recipe_machine = recipe_data["machine"]
            recipe_time = recipe_data["time"]
            recipe_price = recipe_data["price"]
            recipe_description = recipe_data["description"]
            recipe_category = recipe_data["category"]
            recipe_tags = recipe_data["tags"]
            recipe_link = recipe_data["link"]
            recipe = Recipe(recipe_name, recipe_inputs, recipe_outputs, recipe_machine, recipe_time, recipe_price, recipe_description, recipe_category, recipe_tags, recipe_link)
            self.recipes[recipe.name] = recipe
            self.recipes_names.append(recipe.name)
        
        # Load the machins
        for machine_name, machine_data in data["Machines"].items():
            self.machines_data[machine_name] = machine_data
        print("Data loaded successfully.")

    def create_machine_number(self, machine_type):
        if machine_type in self.machines:
            machine_name = f"{machine_type}_{len(self.machines[machine_type]) + 1}"
        else:
            machine_name = f"{machine_type}_1" 
        return self.create_machine(machine_name, machine_type)
    
    def create_machine(self, name, machine_type):
        if name in self.machines:
            print(f"Machine {name} already exists.")
            return False
        else:
            new_machine = Machine(name, machine_type)
            self.machines[name] = new_machine
            print(f"Machine {name} of type {machine_type} created successfully.")
            return True

    def run(self):
        if self.rounds <= 0:
            self.current_round = -1 # Infinite loop
        # print statistics
        print(f"Total recipes: {self.statistics.get_total_recipes()}")
        print(f"Average recipe time: {self.statistics.get_average_time()} ticks")
        print(f"Most common machine: {self.statistics.get_most_common_machine()[0]} used {self.statistics.get_most_common_machine()[1]} times")
        print("Most used raw materials:")
        most_used_raw_materials = self.statistics.get_most_used_raw_materials(top=True, topelements=5, reverse=True)
        for raw_material, amount in most_used_raw_materials:
            print(f"{raw_material}: {amount} times")
        while self.current_round < self.rounds:
            print(f"Round {self.current_round + 1}/{self.rounds}")
            self.current_round += 1
            # generate random recipes
            number = random.randint(1, 5)  # Randomly choose how many recipes to generate
            recipes = random.sample(self.recipes_names, k=number)
            self.current_recipes = recipes
            print(f"Current recipes: {self.current_recipes}")
            # Add raw materials to inventory
            for recipe_name in self.current_recipes:
                recipe = self.recipes[recipe_name]
                print(f"Processing recipe: {recipe.name}")
                # Check if we have enough raw materials
                enough_materials = True
                for input_material, amount in recipe.inputs.items():
                    print(f"input_material: {input_material}, amount: {amount}")
                    print(f"raw_materials[input_material]: {self.raw_materials}")
                    if input_material not in self.raw_materials or self.raw_materials[input_material]["Quantity"] < amount:
                        enough_materials = False
                        print(f"Not enough {input_material} for {recipe.name}.")
                        self.shop.buy_raw_materials([{input_material: {"Quantity": amount}}])
                        break
                if enough_materials:
                    # Start a machine for the recipe if there is no one available or start the recipe on the machine if there's an available
                    for machine_name, machine_address in self.machines.items():
                        if machine_address.working is False and machine_address.machine_type == recipe.machine:
                            print(f"Starting {recipe.name} on {machine_name}.")
                            machine_address.start_recipe(recipe)
                            break
                        else:
                            print(f"There is no available machine for {recipe.name} or the machines are already working so we have to genearte a new one.")
                            machine_name = self.create_machine_number(recipe.machine)
                            self.create_machine(machine_name, recipe.machine)
                    # Process the recipe
                    print(f"Processing {recipe.name}...")
                    for input_material, amount in recipe.inputs.items():
                        self.raw_materials[input_material]["Quantity"] -= amount
                    print(f"Produced {recipe.outputs} from {recipe.name}.")
                else:
                    print(f"Skipping {recipe.name} due to insufficient materials.")
if __name__ == "__main__":
    main = Main(rounds=10)  # Set the number of rounds to run
    main.run()
    print("Simulation completed.")