class RawMaterial:
    def __init__(self, name):
        self.name = name
class Recipe:
    def __init__(self, name, inputs, outputs, machine, time):
        """
        inputs: dict {RawMaterial: mennyiség}
        outputs: dict {RawMaterial: mennyiség}
        time: gyártási idő tickben vagy más egységben
        """
        self.name = name
        self.inputs = inputs
        self.outputs = outputs
        self.machine = machine
        self.time = time
    def get_atributes(self):
        atributes = {
            "name": self.name,
            "inputs": self.inputs,
            "outputs": self.outputs,
            "machine": self.machine,
            "time": self.time
        }
        return
class Machine:
    def __init__(self, name, machine_type):
        self.machine_type = machine_type
        self.name = name
        self.current_recipe = None
        self.progress = 0

    def start_recipe(self, recipe):
        if recipe.machine == self.machine_type:
            self.current_recipe = recipe
            self.progress = 0
        else:
            print(f"error! couldn't make this recipe ({recipe.name}) with this machine: {self.name} (type: {self.machine_type})")

    def tick(self):
        if self.current_recipe is not None:
            self.progress += 1
            if self.progress >= self.current_recipe.time:
                print(f"{self.name} had made the {self.current_recipe.name}")
                self.current_recipe = None
                self.progress = 0
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

    create_materials(["egg", "water", "wheat"])
    create_reciptes([{"name": "bread", "inputs": ["egg", "water", "wheat"], "outputs": "bread", "machine": "oven", "time": 2}])
    create_machine("oven1")
    oven1 = machins["oven1"]
    oven1.start_recipe(reciptes["bread"])
    for i in range(5):
        for key, value in machins.items():
            value.tick()
            print(f"{key} has ticked")