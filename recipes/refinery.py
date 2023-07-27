from data import ERessource
from recipe import Recipe, RecipeInput, RecipeOutput

REFINERY_RECIPES = [
	Recipe(
		'Alternate: Coated Cable',
		inputs=[
			RecipeInput(ERessource.WIRE, 37.5),
			RecipeInput(ERessource.HEAVY_OIL_RESIDUE, 15)
		],
		outputs=[RecipeOutput(ERessource.CABLE, 67.5)]
	),
	Recipe(
		'Alternate: Diluted Packaged Fuel',
		inputs=[
			RecipeInput(ERessource.HEAVY_OIL_RESIDUE, 30),
			RecipeInput(ERessource.PACKAGED_WATER, 60)
		],
		outputs=[RecipeOutput(ERessource.PACKAGED_FUEL, 60)]
	),
	Recipe(
		'Alternate: Electrode Aluminum Scrap',
		inputs=[
			RecipeInput(ERessource.ALUMINA_SOLUTION, 180),
			RecipeInput(ERessource.PETROLEUM_COKE, 60)
		],
		outputs=[
			RecipeOutput(ERessource.ALUMINUM_SCRAP, 300),
			RecipeOutput(ERessource.WATER, 105)
		]
	),
	Recipe(
		'Alternate: Heavy Oil Residue',
		inputs=[RecipeInput(ERessource.CRUDE_OIL, 30)],
		outputs=[
			RecipeOutput(ERessource.HEAVY_OIL_RESIDUE, 40),
			RecipeOutput(ERessource.POLYMER_RESIN, 20)
		]
	),
	Recipe(
		'Alternate: Recycled Plastic',
		inputs=[
			RecipeInput(ERessource.RUBBER, 30),
			RecipeInput(ERessource.FUEL, 30)
		],
		outputs=[RecipeOutput(ERessource.PLASTIC, 60)]
	),
	Recipe(
		'Alternate: Polyester Fabric',
		inputs=[
			RecipeInput(ERessource.POLYMER_RESIN, 80),
			RecipeInput(ERessource.WATER, 50)
		],
		outputs=[RecipeOutput(ERessource.FABRIC, 5)]
	),
	Recipe(
		'Alternate: Polymer Resin',
		inputs=[RecipeInput(ERessource.CRUDE_OIL, 60)],
		outputs=[
			RecipeOutput(ERessource.POLYMER_RESIN, 130),
			RecipeOutput(ERessource.HEAVY_OIL_RESIDUE, 20)
		]
	),
	Recipe(
		'Alternate: Pure Caterium Ingot',
		inputs=[
			RecipeInput(ERessource.CATERIUM_ORE, 24),
			RecipeInput(ERessource.WATER, 24)
		],
		outputs=[RecipeOutput(ERessource.CATERIUM_INGOT, 12)]
	),
	Recipe(
		'Alternate: Pure Copper Ingot',
		inputs=[
			RecipeInput(ERessource.COPPER_ORE, 15),
			RecipeInput(ERessource.WATER, 10)
		],
		outputs=[RecipeOutput(ERessource.COPPER_INGOT, 37.5)]
	),
	Recipe(
		'Alternate: Pure Iron Ingot',
		inputs=[
			RecipeInput(ERessource.IRON_ORE, 35),
			RecipeInput(ERessource.WATER, 20)
		],
		outputs=[RecipeOutput(ERessource.IRON_INGOT, 65)]
	),
	Recipe(
		'Alternate: Pure Quartz Crystal',
		inputs=[
			RecipeInput(ERessource.RAW_QUARTZ, 67.5),
			RecipeInput(ERessource.WATER, 37.5)
		],
		outputs=[RecipeOutput(ERessource.QUARTZ_CRYSTAL, 52.5)]
	),
	Recipe(
		'Alternate: Recycled Rubber',
		inputs=[
			RecipeInput(ERessource.PLASTIC, 30),
			RecipeInput(ERessource.FUEL, 30)
		],
		outputs=[RecipeOutput(ERessource.RUBBER, 60)]
	),
	Recipe(
		'Alternate: Sloppy Alumina',
		inputs=[
			RecipeInput(ERessource.BAUXITE, 200),
			RecipeInput(ERessource.WATER, 200)
		],
		outputs=[RecipeOutput(ERessource.ALUMINA_SOLUTION, 240)]
	),
	Recipe(
		'Alternate: Steamed Copper Sheet',
		inputs=[
			RecipeInput(ERessource.COPPER_INGOT, 22.5),
			RecipeInput(ERessource.WATER, 22.5)
		],
		outputs=[RecipeOutput(ERessource.COPPER_SHEET, 22.5)]
	),
	Recipe(
		'Alternate: Turbo Heavy Fuel',
		inputs=[
			RecipeInput(ERessource.HEAVY_OIL_RESIDUE, 37.5),
			RecipeInput(ERessource.COMPACTED_COAL, 30)
		],
		outputs=[RecipeOutput(ERessource.TURBOFUEL, 30)]
	),
	Recipe(
		'Turbofuel',
		inputs=[
			RecipeInput(ERessource.FUEL, 22.5),
			RecipeInput(ERessource.COMPACTED_COAL, 15)
		],
		outputs=[RecipeOutput(ERessource.TURBOFUEL, 18.75)]
	),
	Recipe(
		'Alternate: Wet Concrete',
		inputs=[
			RecipeInput(ERessource.LIMESTONE, 120),
			RecipeInput(ERessource.WATER, 100)
		],
		outputs=[RecipeOutput(ERessource.CONCRETE, 80)]
	),
	Recipe(
		'Alumina Solution',
		inputs=[
			RecipeInput(ERessource.BAUXITE, 120),
			RecipeInput(ERessource.WATER, 180)
		],
		outputs=[
			RecipeOutput(ERessource.ALUMINA_SOLUTION, 120),
			RecipeOutput(ERessource.SILICA, 50)
		]
	),
	Recipe(
		'Aluminum Scrap',
		inputs=[
			RecipeInput(ERessource.ALUMINA_SOLUTION, 240),
			RecipeInput(ERessource.COAL, 120)
		],
		outputs=[
			RecipeOutput(ERessource.ALUMINUM_SCRAP, 360),
			RecipeOutput(ERessource.WATER, 120)
		]
	),
	Recipe(
		'Liquid Biofuel',
		inputs=[
			RecipeInput(ERessource.SOLID_BIOFUEL, 90),
			RecipeInput(ERessource.WATER, 45)
		],
		outputs=[RecipeOutput(ERessource.LIQUID_BIOFUEL, 60)]
	),
	Recipe(
		'Fuel',
		inputs=[RecipeInput(ERessource.CRUDE_OIL, 60)],
		outputs=[
			RecipeOutput(ERessource.FUEL, 40),
			RecipeOutput(ERessource.POLYMER_RESIN, 30)
		]
	),
	Recipe(
		'Petroleum Coke',
		inputs=[RecipeInput(ERessource.HEAVY_OIL_RESIDUE, 40)],
		outputs=[RecipeOutput(ERessource.PETROLEUM_COKE, 120)]
	),
	Recipe(
		'Plastic',
		inputs=[
			RecipeInput(ERessource.CRUDE_OIL, 30),
			RecipeInput(ERessource.PLASTIC, 20)
		],
		outputs=[RecipeOutput(ERessource.HEAVY_OIL_RESIDUE, 10)]
	),
	Recipe(
		'Residual Fuel',
		inputs=[RecipeInput(ERessource.HEAVY_OIL_RESIDUE, 60)],
		outputs=[RecipeOutput(ERessource.FUEL, 40)]
	),
	Recipe(
		'Residual Plastic',
		inputs=[
			RecipeInput(ERessource.POLYMER_RESIN, 60),
			RecipeInput(ERessource.WATER, 20)
		],
		outputs=[RecipeOutput(ERessource.PLASTIC, 20)]
	),
	Recipe(
		'Residual Rubber',
		inputs=[
			RecipeInput(ERessource.POLYMER_RESIN, 40),
			RecipeInput(ERessource.WATER, 40)
		],
		outputs=[RecipeOutput(ERessource.RUBBER, 20)]
	),
	Recipe(
		'Rubber',
		inputs=[RecipeInput(ERessource.CRUDE_OIL, 30)],
		outputs=[
			RecipeInput(ERessource.RUBBER, 20),
			RecipeOutput(ERessource.HEAVY_OIL_RESIDUE, 20)
		]
	),
	Recipe(
		'Sulfuric Acid',
		inputs=[
			RecipeInput(ERessource.SULFUR, 50),
			RecipeInput(ERessource.WATER, 50)
		],
		outputs=[RecipeOutput(ERessource.SULFURIC_ACID, 50)]
	)
]