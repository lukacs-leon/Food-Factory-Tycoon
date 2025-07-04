class Recipe:
    def __init__(self, name, inputs, outputs, machine, time):
        """
        name:  string [name of the recipe]
        inputs: list [[RawMaterial, amount]]
        outputs: string [RawMaterial, amounte]
        machine: string [name of the machine that can process this recipe]
        time: baking time in ticks
        """
        self.name = name
        self.inputs = inputs
        self.outputs = outputs
        self.machine = machine
        self.time = time