from data import ERessource
from recipe import Recipe, RecipeOutput

MINERMK3_RECIPES = [
    Recipe('Iron Ore Impure', outputs=[RecipeOutput(ERessource.IRON_ORE, 120)]),
    Recipe('Iron Ore Normal', outputs=[RecipeOutput(ERessource.IRON_ORE, 240)]),
    Recipe('Iron Ore Pure', outputs=[RecipeOutput(ERessource.IRON_ORE, 480)]),
    
    Recipe('Copper Ore Impure', outputs=[RecipeOutput(ERessource.COPPER_ORE, 120)]),
    Recipe('Copper Ore Normal', outputs=[RecipeOutput(ERessource.COPPER_ORE, 240)]),
    Recipe('Copper Ore Pure', outputs=[RecipeOutput(ERessource.COPPER_ORE, 480)]),
    
    Recipe('Limestone Impure', outputs=[RecipeOutput(ERessource.LIMESTONE, 120)]),
    Recipe('Limestone Normal', outputs=[RecipeOutput(ERessource.LIMESTONE, 240)]),
    Recipe('Limestone Pure', outputs=[RecipeOutput(ERessource.LIMESTONE, 480)]),
    
    Recipe('Coal Impure', outputs=[RecipeOutput(ERessource.COAL, 120)]),
    Recipe('Coal Normal', outputs=[RecipeOutput(ERessource.COAL, 240)]),
    Recipe('Coal Pure', outputs=[RecipeOutput(ERessource.COAL, 480)]),
    
    Recipe('Caterium Ore Impure', outputs=[RecipeOutput(ERessource.CATERIUM_ORE, 120)]),
    Recipe('Caterium Ore Normal', outputs=[RecipeOutput(ERessource.CATERIUM_ORE, 240)]),
    Recipe('Caterium Ore Pure', outputs=[RecipeOutput(ERessource.CATERIUM_ORE, 480)]),
    
    Recipe('Raw Quartz Impure', outputs=[RecipeOutput(ERessource.RAW_QUARTZ, 120)]),
    Recipe('Raw Quartz Normal', outputs=[RecipeOutput(ERessource.RAW_QUARTZ, 240)]),
    Recipe('Raw Quartz Pure', outputs=[RecipeOutput(ERessource.RAW_QUARTZ, 480)]),
    
    Recipe('Sulfur Impure', outputs=[RecipeOutput(ERessource.SULFUR, 120)]),
    Recipe('Sulfur Normal', outputs=[RecipeOutput(ERessource.SULFUR, 240)]),
    Recipe('Sulfur Pure', outputs=[RecipeOutput(ERessource.SULFUR, 480)]),
    
    Recipe('Bauxite Impure', outputs=[RecipeOutput(ERessource.BAUXITE, 120)]),
    Recipe('Bauxite Normal', outputs=[RecipeOutput(ERessource.BAUXITE, 240)]),
    Recipe('Bauxite Pure', outputs=[RecipeOutput(ERessource.BAUXITE, 480)]),
    
    Recipe('Uranium Impure', outputs=[RecipeOutput(ERessource.URANIUM, 120)]),
    Recipe('Uranium Normal', outputs=[RecipeOutput(ERessource.URANIUM, 240)]),
    Recipe('Uranium Pure', outputs=[RecipeOutput(ERessource.URANIUM, 480)]),
]