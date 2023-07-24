from data import ERessource
from recipe import Recipe, RecipeOutput

WATEREXTRACTOR_RECIPES = [
    Recipe('Water', outputs=[RecipeOutput(ERessource.WATER, 120)]),
]