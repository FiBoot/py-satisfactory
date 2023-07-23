from data import ERessource
from recipe import Recipe, RecipeInput, RecipeOutput

FOUNDRY_RECIPES = [
    Recipe(
        'Aluminum Ingot',
        inputs=[
            RecipeInput(ERessource.ALUMINUM_SCRAP, 90),
            RecipeInput(ERessource.SILICA, 75)
        ],
        outputs=[RecipeOutput(ERessource.ALUMINUM_INGOT, 60)]
    ),
    Recipe(
        'Steel Ingot',
        inputs=[
            RecipeInput(ERessource.IRON_ORE, 45),
            RecipeInput(ERessource.COAL, 45)
        ],
        outputs=[RecipeOutput(ERessource.STEEL_INGOT, 45)]
    ),
    Recipe(
        'Alternate: Coke Steel Ingot',
        inputs=[
            RecipeInput(ERessource.IRON_ORE, 75),
            RecipeInput(ERessource.PETROLEUM_COKE, 75)
        ],
        outputs=[RecipeOutput(ERessource.STEEL_INGOT, 100)]
    ),
    Recipe(
        'Alternate: Copper Alloy Ingot',
        inputs=[
            RecipeInput(ERessource.COPPER_ORE, 50),
            RecipeInput(ERessource.IRON_ORE, 20)
        ],
        outputs=[RecipeOutput(ERessource.COPPER_INGOT, 100)]
    ),
    Recipe(
        'Alternate: Iron Alloy Ingot',
        inputs=[
            RecipeInput(ERessource.IRON_ORE, 20),
            RecipeInput(ERessource.COPPER_ORE, 20)
        ],
        outputs=[RecipeOutput(ERessource.IRON_INGOT, 50)]
    ),
    Recipe(
        'Alternate: Solid Steel Ingot',
        inputs=[
            RecipeInput(ERessource.IRON_INGOT, 40),
            RecipeInput(ERessource.COAL, 40)
        ],
        outputs=[RecipeOutput(ERessource.STEEL_INGOT, 60)]
    ),
    Recipe(
        'Alternate: Compacted Steel Ingot',
        inputs=[
            RecipeInput(ERessource.IRON_ORE, 22.5),
            RecipeInput(ERessource.COMPACTED_COAL, 11.25)
        ],
        outputs=[RecipeOutput(ERessource.STEEL_INGOT, 37.5)]
    ),
]