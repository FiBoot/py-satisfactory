from data import ERessource
from recipe import Recipe, RecipeInput, RecipeOutput

PACKAGER_RECIPES = [
	Recipe(
		'Packaged Fuel',
		inputs=[
			RecipeInput(ERessource.FUEL, 40),
			RecipeInput(ERessource.EMPTY_CANISTER, 40)
		],
		outputs=[RecipeOutput(ERessource.PACKAGED_FUEL, 40)]
	),
	Recipe(
		'Packaged Alumina Solution',
		inputs=[
			RecipeInput(ERessource.ALUMINA_SOLUTION, 120),
			RecipeInput(ERessource.EMPTY_CANISTER, 120)
		],
		outputs=[RecipeOutput(ERessource.PACKAGED_ALUMINA_SOLUTION, 120)]
	),
	Recipe(
		'Packaged Liquid Biofuel',
		inputs=[
			RecipeInput(ERessource.LIQUID_BIOFUEL, 40),
			RecipeInput(ERessource.EMPTY_CANISTER, 40)
		],
		outputs=[RecipeOutput(ERessource.PACKAGED_LIQUID_BIOFUEL, 40)]
	),
	Recipe(
		'Packaged Oil',
		inputs=[
			RecipeInput(ERessource.CRUDE_OIL, 30),
			RecipeInput(ERessource.EMPTY_CANISTER, 30)
		],
		outputs=[RecipeOutput(ERessource.PACKAGED_OIL, 30)]
	),
	Recipe(
		'Packaged Nitric Acid',
		inputs=[
			RecipeInput(ERessource.NITRIC_ACID, 30),
			RecipeInput(ERessource.EMPTY_FLUID_TANK, 30)
		],
		outputs=[RecipeOutput(ERessource.PACKAGED_NITRIC_ACID, 30)]
	),
	Recipe(
		'Packaged Nitrogen Gas',
		inputs=[
			RecipeInput(ERessource.NITROGEN_GAS, 240),
			RecipeInput(ERessource.EMPTY_FLUID_TANK, 60)
		],
		outputs=[RecipeOutput(ERessource.PACKAGED_NITROGEN_GAS, 60)]
	),
	Recipe(
		'Packaged Heavy Oil Residue',
		inputs=[
			RecipeInput(ERessource.HEAVY_OIL_RESIDUE, 30),
			RecipeInput(ERessource.EMPTY_CANISTER, 30)
		],
		outputs=[RecipeOutput(ERessource.PACKAGED_HEAVY_OIL_RESIDUE, 30)]
	),
	Recipe(
		'Packaged Sulfuric Acid',
		inputs=[
			RecipeInput(ERessource.SULFURIC_ACID, 40),
			RecipeInput(ERessource.EMPTY_CANISTER, 40)
		],
		outputs=[RecipeOutput(ERessource.PACKAGED_SULFURIC_ACID, 40)]
	),
	Recipe(
		'Packaged Turbofuel',
		inputs=[
			RecipeInput(ERessource.TURBOFUEL, 20),
			RecipeInput(ERessource.EMPTY_CANISTER, 20)
		],
		outputs=[RecipeOutput(ERessource.PACKAGED_TURBOFUEL, 20)]
	),
	Recipe(
		'Packaged Water',
		inputs=[
			RecipeInput(ERessource.WATER, 60),
			RecipeInput(ERessource.EMPTY_CANISTER, 60)
		],
		outputs=[RecipeOutput(ERessource.PACKAGED_WATER, 60)]
	),
    Recipe(
		'Unpackage Alumina Solution',
		inputs=[RecipeInput(ERessource.PACKAGED_ALUMINA_SOLUTION, 120)],
		outputs=[
			RecipeOutput(ERessource.ALUMINA_SOLUTION, 120),
			RecipeOutput(ERessource.EMPTY_CANISTER, 120)
		]
	),
	Recipe(
		'Unpackage Liquid Biofuel',
		inputs=[RecipeInput(ERessource.PACKAGED_LIQUID_BIOFUEL, 60)],
		outputs=[
			RecipeOutput(ERessource.LIQUID_BIOFUEL, 60),
			RecipeOutput(ERessource.EMPTY_CANISTER, 60)
		]
	),
	Recipe(
		'Unpackage Fuel',
		inputs=[RecipeInput(ERessource.PACKAGED_FUEL, 60)],
		outputs=[
			RecipeOutput(ERessource.FUEL, 60),
			RecipeOutput(ERessource.EMPTY_CANISTER, 60)
		]
	),
	Recipe(
		'Unpackage Nitric Acid',
		inputs=[RecipeInput(ERessource.PACKAGED_NITRIC_ACID, 20)],
		outputs=[
			RecipeOutput(ERessource.NITRIC_ACID, 20),
			RecipeOutput(ERessource.EMPTY_FLUID_TANK, 20)
		]
	),
	Recipe(
		'Unpackage Nitrogen Gas',
		inputs=[RecipeInput(ERessource.PACKAGED_NITROGEN_GAS, 60)],
		outputs=[
			RecipeOutput(ERessource.NITROGEN_GAS, 240),
			RecipeOutput(ERessource.EMPTY_FLUID_TANK, 60)
		]
	),
	Recipe(
		'Unpackage Heavy Oil Residue',
		inputs=[RecipeInput(ERessource.PACKAGED_HEAVY_OIL_RESIDUE, 20)],
		outputs=[
			RecipeOutput(ERessource.HEAVY_OIL_RESIDUE, 20),
			RecipeOutput(ERessource.EMPTY_CANISTER, 20)
		]
	),
	Recipe(
		'Unpackage Oil',
		inputs=[RecipeInput(ERessource.PACKAGED_OIL, 60)],
		outputs=[
			RecipeOutput(ERessource.CRUDE_OIL, 60),
			RecipeOutput(ERessource.EMPTY_CANISTER, 60)
		]
	),
	Recipe(
		'Unpackage Sulfuric Acid',
		inputs=[RecipeInput(ERessource.PACKAGED_SULFURIC_ACID, 60)],
		outputs=[
			RecipeOutput(ERessource.SULFURIC_ACID, 60),
			RecipeOutput(ERessource.EMPTY_CANISTER, 60)
		]
	),
	Recipe(
		'Unpackage Turbofuel',
		inputs=[RecipeInput(ERessource.PACKAGED_TURBOFUEL, 20)],
		outputs=[
			RecipeOutput(ERessource.TURBOFUEL, 20),
			RecipeOutput(ERessource.EMPTY_CANISTER, 20)
		]
	),
	Recipe(
		'Unpackage Water',
		inputs=[RecipeInput(ERessource.PACKAGED_WATER, 120)],
		outputs=[
			RecipeOutput(ERessource.WATER, 120),
			RecipeOutput(ERessource.EMPTY_CANISTER, 120)
		]
	),
]