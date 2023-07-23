from data import ERessource
from recipe import Recipe, RecipeOutput

MINERMK2_RECIPES = [
    Recipe('Iron Ore Impure', outputs=[RecipeOutput(ERessource.COAL, 60)]),
    Recipe('Iron Ore Normal', outputs=[RecipeOutput(ERessource.COAL, 120)]),
    Recipe('Iron Ore Pure', outputs=[RecipeOutput(ERessource.COAL, 240)]),
    
    Recipe('Copper Ore Impure', outputs=[RecipeOutput(ERessource.COAL, 60)]),
    Recipe('Copper Ore Normal', outputs=[RecipeOutput(ERessource.COAL, 120)]),
    Recipe('Copper Ore Pure', outputs=[RecipeOutput(ERessource.COAL, 240)]),
    
    Recipe('Limestone Impure', outputs=[RecipeOutput(ERessource.COAL, 60)]),
    Recipe('Limestone Normal', outputs=[RecipeOutput(ERessource.COAL, 120)]),
    Recipe('Limestone Pure', outputs=[RecipeOutput(ERessource.COAL, 240)]),
    
    Recipe('Coal Impure', outputs=[RecipeOutput(ERessource.COAL, 60)]),
    Recipe('Coal Normal', outputs=[RecipeOutput(ERessource.COAL, 120)]),
    Recipe('Coal Pure', outputs=[RecipeOutput(ERessource.COAL, 240)]),
    
    Recipe('Caterium Ore Impure', outputs=[RecipeOutput(ERessource.COAL, 60)]),
    Recipe('Caterium Ore Normal', outputs=[RecipeOutput(ERessource.COAL, 120)]),
    Recipe('Caterium Ore Pure', outputs=[RecipeOutput(ERessource.COAL, 240)]),
    
    Recipe('Raw Quartz Impure', outputs=[RecipeOutput(ERessource.COAL, 60)]),
    Recipe('Raw Quartz Normal', outputs=[RecipeOutput(ERessource.COAL, 120)]),
    Recipe('Raw Quartz Pure', outputs=[RecipeOutput(ERessource.COAL, 240)]),
    
    Recipe('Sulfur Impure', outputs=[RecipeOutput(ERessource.COAL, 60)]),
    Recipe('Sulfur Normal', outputs=[RecipeOutput(ERessource.COAL, 120)]),
    Recipe('Sulfur Pure', outputs=[RecipeOutput(ERessource.COAL, 240)]),
    
    Recipe('Bauxite Impure', outputs=[RecipeOutput(ERessource.COAL, 60)]),
    Recipe('Bauxite Normal', outputs=[RecipeOutput(ERessource.COAL, 120)]),
    Recipe('Bauxite Pure', outputs=[RecipeOutput(ERessource.COAL, 240)]),
    
    Recipe('Uranium Impure', outputs=[RecipeOutput(ERessource.COAL, 60)]),
    Recipe('Uranium Normal', outputs=[RecipeOutput(ERessource.COAL, 120)]),
    Recipe('Uranium Pure', outputs=[RecipeOutput(ERessource.COAL, 240)]),
]