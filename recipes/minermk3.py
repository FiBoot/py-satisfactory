from data import ERessource
from recipe import Recipe, RecipeOutput

MINERMK3_RECIPES = [
    Recipe('Iron Ore Impure', outputs=[RecipeOutput(ERessource.COAL, 120)]),
    Recipe('Iron Ore Normal', outputs=[RecipeOutput(ERessource.COAL, 240)]),
    Recipe('Iron Ore Pure', outputs=[RecipeOutput(ERessource.COAL, 480)]),
    
    Recipe('Copper Ore Impure', outputs=[RecipeOutput(ERessource.COAL, 120)]),
    Recipe('Copper Ore Normal', outputs=[RecipeOutput(ERessource.COAL, 240)]),
    Recipe('Copper Ore Pure', outputs=[RecipeOutput(ERessource.COAL, 480)]),
    
    Recipe('Limestone Impure', outputs=[RecipeOutput(ERessource.COAL, 120)]),
    Recipe('Limestone Normal', outputs=[RecipeOutput(ERessource.COAL, 240)]),
    Recipe('Limestone Pure', outputs=[RecipeOutput(ERessource.COAL, 480)]),
    
    Recipe('Coal Impure', outputs=[RecipeOutput(ERessource.COAL, 120)]),
    Recipe('Coal Normal', outputs=[RecipeOutput(ERessource.COAL, 240)]),
    Recipe('Coal Pure', outputs=[RecipeOutput(ERessource.COAL, 480)]),
    
    Recipe('Caterium Ore Impure', outputs=[RecipeOutput(ERessource.COAL, 120)]),
    Recipe('Caterium Ore Normal', outputs=[RecipeOutput(ERessource.COAL, 240)]),
    Recipe('Caterium Ore Pure', outputs=[RecipeOutput(ERessource.COAL, 480)]),
    
    Recipe('Raw Quartz Impure', outputs=[RecipeOutput(ERessource.COAL, 120)]),
    Recipe('Raw Quartz Normal', outputs=[RecipeOutput(ERessource.COAL, 240)]),
    Recipe('Raw Quartz Pure', outputs=[RecipeOutput(ERessource.COAL, 480)]),
    
    Recipe('Sulfur Impure', outputs=[RecipeOutput(ERessource.COAL, 120)]),
    Recipe('Sulfur Normal', outputs=[RecipeOutput(ERessource.COAL, 240)]),
    Recipe('Sulfur Pure', outputs=[RecipeOutput(ERessource.COAL, 480)]),
    
    Recipe('Bauxite Impure', outputs=[RecipeOutput(ERessource.COAL, 120)]),
    Recipe('Bauxite Normal', outputs=[RecipeOutput(ERessource.COAL, 240)]),
    Recipe('Bauxite Pure', outputs=[RecipeOutput(ERessource.COAL, 480)]),
    
    Recipe('Uranium Impure', outputs=[RecipeOutput(ERessource.COAL, 120)]),
    Recipe('Uranium Normal', outputs=[RecipeOutput(ERessource.COAL, 240)]),
    Recipe('Uranium Pure', outputs=[RecipeOutput(ERessource.COAL, 480)]),
]