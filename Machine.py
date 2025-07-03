class Machine:
    def __init__(self, name, machine_type):
        self.machine_type = machine_type
        self.name = name
        self.current_recipe = None
        self.progress = 0
        self.RawMaterials_list = []

    def start_recipe(self, recipe):
        if recipe.machine == self.machine_type:
            self.current_recipe = recipe
            self.progress = 0
        else:
            print(f"error! couldn't make this recipe ({self.current_recipe.name}) with this machine: {self.name} (type: {self.machine_type})")
    
    def add_RawMaterial(self, RawMaterial: list):
        for item in RawMaterial:
            self.RawMaterials_list.append(item)
    
    def remove_RawMaterial(self, RawMaterail_to_remove: list):
        for item in RawMaterail_to_remove:
            try:
                self.RawMaterials_list.remove(item)
            except:
                print(f"Something went wrong with this item when tried to remove: {item}")
                exit()

    def tick(self):
        if self.current_recipe is not None:
            self.progress += 1
            if self.progress >= self.current_recipe.time:
                print(f"{self.name} had made the {self.current_recipe.name}")
                self.current_recipe = None
                self.progress = 0