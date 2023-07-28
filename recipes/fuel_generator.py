from data import ERessource
from recipe import Recipe, RecipeInput

FUEL_GENERATOR_RECIPES = [
    Recipe('Coal', inputs=[RecipeInput(ERessource.FUEL, 12)]),
    Recipe('Compacted Coal', inputs=[RecipeInput(ERessource.LIQUID_BIOFUEL, 12)]),
    Recipe('Petroleum Coke', inputs=[RecipeInput(ERessource.TURBOFUEL, 4.5)]),
]