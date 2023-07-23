from data import ERessource
from recipe import Recipe, RecipeInput, RecipeOutput

SMELTER_RECIPES = [
    Recipe('Iron Ingot', inputs=[RecipeInput(ERessource.IRON_ORE, 30)], outputs=[RecipeOutput(ERessource.IRON_INGOT, 30)]),
    Recipe('Copper Ingot', inputs=[RecipeInput(ERessource.COPPER_ORE, 30)], outputs=[RecipeOutput(ERessource.COPPER_INGOT, 30)]),
    Recipe('Caterium Ingot', inputs=[RecipeInput(ERessource.CATERIUM_ORE, 45)], outputs=[RecipeOutput(ERessource.CATERIUM_INGOT, 15)]),
    Recipe('Pure Aliminum Ingot', inputs=[RecipeInput(ERessource.ALUMINUM_SCRAP, 60)], outputs=[RecipeOutput(ERessource.ALUMINUM_INGOT, 1)]),
]