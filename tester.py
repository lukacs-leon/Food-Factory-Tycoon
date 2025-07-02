import random
import string
# Import the Recipe, RawMaterial and Machine objects to test
import Recipe as Recipe
import RawMaterial as RawMaterial
import Machine as Machine

if __name__ == "__main__":
    materials = {}
    def create_materials(materials_list: list):
        for mat_name in materials_list:
            material_obj = RawMaterial(mat_name)
            materials[mat_name] = material_obj
        print(materials)
    reciptes = {}
    def create_reciptes(reciptes_list: list):
        for i in reciptes_list:
            name = i["name"]
            inputs = i["inputs"]
            outputs = i["outputs"]
            machine = i["machine"]
            time = i["time"]
            reciptes_object = Recipe(name, inputs, outputs, machine, time)
            reciptes[name] = reciptes_object
        print(reciptes)
    machins = {}
    def create_machine(name: str):
        machine = Machine(name, "turmix")
        machins[name] = machine
    ''' example calls of the full project
    create_materials(["egg", "water", "wheat"])
    create_reciptes([{"name": "bread", "inputs": ["egg", "water", "wheat"], "outputs": "bread", "machine": "oven", "time": 2}])
    create_machine("oven1")
    oven1 = machins["oven1"]
    oven1.start_recipe(reciptes["bread"])
    '''
    def generate_random_materials(n: int):
        materials_list = ["egg", "wheat", "bread", "water", "honey", "pancake", "choclet powder"]
        name = ''.join(random.sample(materials_list, k=n))
        materials_list.append(name)
        return materials_list
    
    for i in range(5):
        for key, value in machins.items():
            value.tick()
            print(f"{key} has ticked")