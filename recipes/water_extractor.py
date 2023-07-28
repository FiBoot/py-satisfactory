from data import ERessource
from recipe import Recipe, RecipeOutput

WATER_EXTRACTOR_RECIPES = [
    Recipe('Water', outputs=[RecipeOutput(ERessource.WATER, 120)]),
]