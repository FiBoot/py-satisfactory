from data import ERessource
from recipe import Recipe, RecipeInput, RecipeOutput

PARTICULE_ACCELERATOR_RECIPES = [
	Recipe(
		'Plutonium Pellet',
		inputs=[
			RecipeInput(ERessource.NONFISSILE_URANIUM, 100),
			RecipeInput(ERessource.URANIUM_WASTE, 25)
		],
		outputs=[RecipeOutput(ERessource.PLUTONIUM_PELLET, 30)]
	),
	Recipe(
		'Nuclear Pasta',
		inputs=[
			RecipeInput(ERessource.COPPER_POWDER, 100),
			RecipeInput(ERessource.PRESSURE_CONVERSION_CUBE, 0.5)
		],
		outputs=[RecipeOutput(ERessource.NUCLEAR_PASTA, 1)]
	),
	Recipe(
		'Alternate: Instant Plutonium Cell',
		inputs=[
			RecipeInput(ERessource.NONFISSILE_URANIUM, 75),
			RecipeInput(ERessource.ALUMINUM_CASING, 10)
		],
		outputs=[RecipeOutput(ERessource.ENCASED_PLUTONIUM_CELL, 20)]
	),
]