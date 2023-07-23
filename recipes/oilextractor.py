from data import ERessource
from recipe import Recipe, RecipeOutput

OILEXTRACTOR_RECIPES = [
    Recipe('Crude Oil Impure', outputs=[RecipeOutput(ERessource.CRUDE_OIL, 60)]),
    Recipe('Crude Oil Normal', outputs=[RecipeOutput(ERessource.CRUDE_OIL, 120)]),
    Recipe('Crude Oil Pure', outputs=[RecipeOutput(ERessource.CRUDE_OIL, 240)]),
]