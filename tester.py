class RawMaterial:
    def __init__(self, name):
        self.name = name
class Recipe:
    def __init__(self, name, inputs, outputs, time):
        """
        inputs: dict {RawMaterial: mennyiség}
        outputs: dict {RawMaterial: mennyiség}
        time: gyártási idő tickben vagy más egységben
        """
        self.name = name
        self.inputs = inputs
        self.outputs = outputs
        self.time = time
class Machine:
    def __init__(self, name):
        self.name = name
        self.current_recipe = None
        self.progress = 0  # gyártás állapota

    def start_recipe(self, recipe):
        self.current_recipe = recipe
        self.progress = 0

    def tick(self):
        if self.current_recipe is not None:
            self.progress += 1
            if self.progress >= self.current_recipe.time:
                # kész a termék
                print(f"{self.name} elkészült a {self.current_recipe.name}")
                self.current_recipe = None
                self.progress = 0
if __name__ == "__main__":
    materials = {}
    def create_materials(materiasl: list): 
        for i in materials:
            memory_address_of_material = RawMaterial(i)
            materials[i]= memory_address_of_materials
        print(materials)
    create_materials(["egg", "water", "wheat"])
