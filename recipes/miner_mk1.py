from data import ERessource
from recipe import Recipe, RecipeOutput

MINER_MK1_RECIPES = [
    Recipe('Iron Ore Impure', outputs=[RecipeOutput(ERessource.IRON_ORE, 30)]),
    Recipe('Iron Ore Normal', outputs=[RecipeOutput(ERessource.IRON_ORE, 60)]),
    Recipe('Iron Ore Pure', outputs=[RecipeOutput(ERessource.IRON_ORE, 120)]),
    
    Recipe('Copper Ore Impure', outputs=[RecipeOutput(ERessource.COPPER_ORE, 30)]),
    Recipe('Copper Ore Normal', outputs=[RecipeOutput(ERessource.COPPER_ORE, 60)]),
    Recipe('Copper Ore Pure', outputs=[RecipeOutput(ERessource.COPPER_ORE, 120)]),
    
    Recipe('Limestone Impure', outputs=[RecipeOutput(ERessource.LIMESTONE, 30)]),
    Recipe('Limestone Normal', outputs=[RecipeOutput(ERessource.LIMESTONE, 60)]),
    Recipe('Limestone Pure', outputs=[RecipeOutput(ERessource.LIMESTONE, 120)]),
    
    Recipe('Coal Impure', outputs=[RecipeOutput(ERessource.COAL, 30)]),
    Recipe('Coal Normal', outputs=[RecipeOutput(ERessource.COAL, 60)]),
    Recipe('Coal Pure', outputs=[RecipeOutput(ERessource.COAL, 120)]),
    
    Recipe('Caterium Ore Impure', outputs=[RecipeOutput(ERessource.CATERIUM_ORE, 30)]),
    Recipe('Caterium Ore Normal', outputs=[RecipeOutput(ERessource.CATERIUM_ORE, 60)]),
    Recipe('Caterium Ore Pure', outputs=[RecipeOutput(ERessource.CATERIUM_ORE, 120)]),
    
    Recipe('Raw Quartz Impure', outputs=[RecipeOutput(ERessource.RAW_QUARTZ, 30)]),
    Recipe('Raw Quartz Normal', outputs=[RecipeOutput(ERessource.RAW_QUARTZ, 60)]),
    Recipe('Raw Quartz Pure', outputs=[RecipeOutput(ERessource.RAW_QUARTZ, 120)]),
    
    Recipe('Sulfur Impure', outputs=[RecipeOutput(ERessource.SULFUR, 30)]),
    Recipe('Sulfur Normal', outputs=[RecipeOutput(ERessource.SULFUR, 60)]),
    Recipe('Sulfur Pure', outputs=[RecipeOutput(ERessource.SULFUR, 120)]),
    
    Recipe('Bauxite Impure', outputs=[RecipeOutput(ERessource.BAUXITE, 30)]),
    Recipe('Bauxite Normal', outputs=[RecipeOutput(ERessource.BAUXITE, 60)]),
    Recipe('Bauxite Pure', outputs=[RecipeOutput(ERessource.BAUXITE, 120)]),
    
    Recipe('Uranium Impure', outputs=[RecipeOutput(ERessource.URANIUM, 30)]),
    Recipe('Uranium Normal', outputs=[RecipeOutput(ERessource.URANIUM, 60)]),
    Recipe('Uranium Pure', outputs=[RecipeOutput(ERessource.URANIUM, 120)]),
]