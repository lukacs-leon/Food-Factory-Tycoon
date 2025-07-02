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