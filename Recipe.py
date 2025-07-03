class Recipe:
    def __init__(self, name, inputs, outputs, machine, time):
        """
        inputs: list [RawMaterial]
        outputs: string "RawMaterial"
        time: baking time in ticks
        """
        self.name = name
        self.inputs = inputs
        self.outputs = outputs
        self.machine = machine
        self.time = time