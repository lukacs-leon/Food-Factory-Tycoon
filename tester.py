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
    def create_materials(materials_list: list):
        for mat_name in materials_list:  # itt a bemeneti listán megyünk végig!
            material_obj = RawMaterial(mat_name)
            materials[mat_name] = material_obj
        print(materials)
    create_materials(["egg", "water", "wheat"])
