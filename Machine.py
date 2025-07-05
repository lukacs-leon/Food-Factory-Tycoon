class Machine:
    def __init__(self, name, machine_type):
        self.machine_type = machine_type
        self.name = name
        self.current_recipe = None
        self.progress = 0
        self.RawMaterials_list = []
        print(f"{self.name} has been created with type {self.machine_type}")

    def start_recipe(self, recipe):
        if recipe is not None:
            can_start = True
            print(f"{self.name} is trying to start the recipe: {recipe.name}")
        else:
            print(f"error! {self.name} cannot start a recipe because the recipe is None.")
            exit()
        for raw_material in recipe.inputs:
            for item in self.RawMaterials_list:
                if item.name == raw_material.name and item.amount >= raw_material.amount:
                    continue
                else:
                    can_start = False
                    break
        if not can_start:
            print(f"error! {self.name} doesn't have enough raw materials to make this recipe ({recipe.name})")
            return False
        elif recipe is not None and self.progress > 0:
            print(f"error! {self.name} is already making {self.current_recipe.name} and can't start a new recipe until it's done.")
            return False
        elif recipe.machine != self.machine_type:
            print(f"error! {self.name} is not the right machine for this recipe ({recipe.name})")
            return False
        else:
            self.current_recipe = recipe
            self.progress = 0
            print(f"{self.name} has started making {self.current_recipe.name}")
            return True
    
    def add_RawMaterial(self, RawMaterial_to_add: list, amount: int = 1):
        for item in RawMaterial_to_add:
            for raw_material in self.RawMaterials_list:
                if raw_material[0] == item:
                    raw_material[1] += amount
                    print(f"{self.name} has added {amount} of {item.name} to its raw materials list.")
                    return True
                else:
                    self.RawMaterials_list.append([item, amount])
                    print(f"{self.name} has added {amount} of {item.name} to its raw materials list.")
                    return True
        print(f"error! {self.name} cannot add raw materials because the list is empty.")
    
    def remove_RawMaterial(self, RawMaterail_to_remove: list, amount: int = 1):
        for item in RawMaterail_to_remove:
            try:
                raw_material_index = self.RawMaterials_list.index(item)
                if self.RawMaterials_list[raw_material_index][2] >= amount:
                    self.RawMaterials_list[raw_material_index][2] -= amount
                if self.RawMaterials_list[raw_material_index][2] < amount:
                    print(f"error! {self.name} doesn't have enough {item.name} to remove {amount} of it.")
                    return False
                if self.RawMaterials_list[raw_material_index][2] == 0:
                    self.RawMaterials_list.pop(raw_material_index)
                    print(f"{self.name} has removed {item.name} from its raw materials list.")
                    return True
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
                return True
            else:
                print(f"{self.name} is making {self.current_recipe.name} and has made {self.progress} out of {self.current_recipe.time}")
                return False
        else:
            print(f"{self.name} is not making anything right now.")
            return False