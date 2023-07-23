from connection import EConnectionLet

class RecipeComponent:
    def __init__(self, ressource, quantity, let = EConnectionLet.OUTLET):
        self.ressource = ressource
        self.quantity = quantity
        self.let = let

class RecipeOutput(RecipeComponent):
    def __init__(self, ressource, quantity):
        RecipeComponent.__init__(self, ressource, quantity)

class RecipeInput(RecipeComponent):
    def __init__(self, ressource, quantity):
        RecipeComponent.__init__(self, ressource, quantity, EConnectionLet.INLET)

class Recipe:
    def __init__(self, name, outputs, inputs = []):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs
        self.rate = 1