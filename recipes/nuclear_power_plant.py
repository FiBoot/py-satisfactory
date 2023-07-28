from data import ERessource
from recipe import Recipe, RecipeOutput, RecipeInput

NUCLEAR_POWER_PLANT_RECIPES = [
    Recipe(
		'Uranium Waste',
        [RecipeOutput(ERessource.URANIUM_WASTE, 10)],
		[
            RecipeInput(ERessource.URANIUM_FUEL_ROD, 0.2),
            RecipeInput(ERessource.WATER, 240),
        ],
	),
    Recipe(
		'Plutonium Waste',
        [RecipeOutput(ERessource.PLUTONIUM_WASTE, 1)],
		[
            RecipeInput(ERessource.PLUTONIUM_FUEL_ROD, 0.2),
            RecipeInput(ERessource.WATER, 240),
        ],
	),
]