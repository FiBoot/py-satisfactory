from data import ERessource
from recipe import Recipe, RecipeOutput

RESSOURCEWELL_EXTRACTOR_RECIPES = [
    Recipe('Nitrogen Gas', outputs=[RecipeOutput(ERessource.NITROGEN_GAS, 30)]),
    Recipe('Nitrogen Gas', outputs=[RecipeOutput(ERessource.NITROGEN_GAS, 60)]),
    Recipe('Nitrogen Gas', outputs=[RecipeOutput(ERessource.NITROGEN_GAS, 120)]),
    
    Recipe('Water', outputs=[RecipeOutput(ERessource.WATER, 30)]),
    Recipe('Water', outputs=[RecipeOutput(ERessource.WATER, 60)]),
    Recipe('Water', outputs=[RecipeOutput(ERessource.WATER, 120)]),
    
    Recipe('Crude Oil', outputs=[RecipeOutput(ERessource.CRUDE_OIL, 30)]),
    Recipe('Crude Oil', outputs=[RecipeOutput(ERessource.CRUDE_OIL, 60)]),
    Recipe('Crude Oil', outputs=[RecipeOutput(ERessource.CRUDE_OIL, 120)]),
]