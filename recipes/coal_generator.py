from data import ERessource
from recipe import Recipe, RecipeInput

COAL_GENERATOR_RECIPES = [
    Recipe('Coal', inputs=[RecipeInput(ERessource.COAL, 15)]),
    Recipe('Compacted Coal', inputs=[RecipeInput(ERessource.COMPACTED_COAL, 7.142857)]),
    Recipe('Petroleum Coke', inputs=[RecipeInput(ERessource.PETROLEUM_COKE, 25)]),
]