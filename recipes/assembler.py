from data import ERessource
from recipe import Recipe, RecipeInput, RecipeOutput

ASSEMBLER_RECIPES = [
    Recipe(
		'AI_Limiter',
		inputs=[
			RecipeInput(ERessource.COPPER_SHEET, 25),
			RecipeInput(ERessource.QUICKWIRE, 100)
		],
		outputs=[RecipeOutput(ERessource.AI_LIMITER, 5)]
	),
	Recipe(
		'Alternate:_Adhered_Iron_Plate',
		inputs=[
			RecipeInput(ERessource.IRON_PLATE, 11.25),
			RecipeInput(ERessource.RUBBER, 3.75)
		],
		outputs=[RecipeOutput(ERessource.REINFORCED_IRON_PLATE, 3.75)]
	),
	Recipe(
		'Alternate:_Alclad_Casing',
		inputs=[
			RecipeInput(ERessource.ALUMINUM_INGOT, 150),
			RecipeInput(ERessource.COPPER_INGOT, 75)
		],
		outputs=[RecipeOutput(ERessource.ALUMINUM_CASING, 112.5)]
	),
	Recipe(
		'Alternate:_Bolted_Frame',
		inputs=[
			RecipeInput(ERessource.REINFORCED_IRON_PLATE, 7.5),
			RecipeInput(ERessource.SCREW, 140)
		],
		outputs=[RecipeOutput(ERessource.MODULAR_FRAME, 5)]
	),
	Recipe(
		'Alternate:_Insulated_Cable',
		inputs=[
			RecipeInput(ERessource.WIRE, 45),
			RecipeInput(ERessource.RUBBER, 30)
		],
		outputs=[RecipeOutput(ERessource.CABLE, 100)]
	),
	Recipe(
		'Alternate:_Quickwire_Cable',
		inputs=[
			RecipeInput(ERessource.QUICKWIRE, 7.5),
			RecipeInput(ERessource.RUBBER, 5)
		],
		outputs=[RecipeOutput(ERessource.CABLE, 27.5)]
	),
	Recipe(
		'Alternate:_Silicon_Circuit_Board',
		inputs=[
			RecipeInput(ERessource.COPPER_SHEET, 27.5),
			RecipeInput(ERessource.SILICA, 27.5)
		],
		outputs=[RecipeOutput(ERessource.CIRCUIT_BOARD, 12.5)]
	),
	Recipe(
		'Alternate:_Caterium_Circuit_Board',
		inputs=[
			RecipeInput(ERessource.PLASTIC, 12.5),
			RecipeInput(ERessource.QUICKWIRE, 37.5)
		],
		outputs=[RecipeOutput(ERessource.CIRCUIT_BOARD, 8.75)]
	),
	Recipe(
		'Alternate:_Coated_Iron_Canister',
		inputs=[
			RecipeInput(ERessource.IRON_PLATE, 30),
			RecipeInput(ERessource.COPPER_SHEET, 15)
		],
		outputs=[RecipeOutput(ERessource.EMPTY_CANISTER, 60)]
	),
	Recipe(
		'Alternate:_Coated_Iron_Plate',
		inputs=[
			RecipeInput(ERessource.IRON_INGOT, 50),
			RecipeInput(ERessource.PLASTIC, 10)
		],
		outputs=[RecipeOutput(ERessource.IRON_PLATE, 75)]
	),
	Recipe(
		'Alternate:_Crystal_Computer',
		inputs=[
			RecipeInput(ERessource.CIRCUIT_BOARD, 7.5),
			RecipeInput(ERessource.CRYSTAL_OSCILLATOR, 2.8125)
		],
		outputs=[RecipeOutput(ERessource.COMPUTER, 2.8125)]
	),
	Recipe(
		'Alternate:_Fine_Concrete',
		inputs=[
			RecipeInput(ERessource.SILICA, 7.5),
			RecipeInput(ERessource.LIMESTONE, 30)
		],
		outputs=[RecipeOutput(ERessource.CONCRETE, 25)]
	),
	Recipe(
		'Alternate:_Copper_Rotor',
		inputs=[
			RecipeInput(ERessource.COPPER_SHEET, 22.5),
			RecipeInput(ERessource.SCREW, 195)
		],
		outputs=[RecipeOutput(ERessource.ROTOR, 11.25)]
	),
	Recipe(
		'Alternate:_Electric_Motor',
		inputs=[
			RecipeInput(ERessource.ELECTROMAGNETIC_CONTROL_ROD, 3.75),
			RecipeInput(ERessource.ROTOR, 7.5)
		],
		outputs=[RecipeOutput(ERessource.MOTOR, 7.5)]
	),
	Recipe(
		'Alternate:_Electrode_Circuit_Board',
		inputs=[
			RecipeInput(ERessource.RUBBER, 30),
			RecipeInput(ERessource.PETROLEUM_COKE, 45)
		],
		outputs=[RecipeOutput(ERessource.CIRCUIT_BOARD, 5)]
	),
	Recipe(
		'Alternate:_Electromagnetic_Connection_Rod',
		inputs=[
			RecipeInput(ERessource.STATOR, 8),
			RecipeInput(ERessource.HIGHSPEED_CONNECTOR, 4)
		],
		outputs=[RecipeOutput(ERessource.ELECTROMAGNETIC_CONTROL_ROD, 8)]
	),
	Recipe(
		'Alternate:_Encased_Industrial_Pipe',
		inputs=[
			RecipeInput(ERessource.STEEL_PIPE, 28),
			RecipeInput(ERessource.CONCRETE, 20)
		],
		outputs=[RecipeOutput(ERessource.ENCASED_INDUSTRIAL_BEAM, 4)]
	),
	Recipe(
		'Alternate:_Compacted_Coal',
		inputs=[
			RecipeInput(ERessource.COAL, 25),
			RecipeInput(ERessource.SULFUR, 25)
		],
		outputs=[RecipeOutput(ERessource.COMPACTED_COAL, 25)]
	),
	Recipe(
		'Alternate:_Fused_Wire',
		inputs=[
			RecipeInput(ERessource.COPPER_INGOT, 12),
			RecipeInput(ERessource.CATERIUM_INGOT, 3)
		],
		outputs=[RecipeOutput(ERessource.WIRE, 90)]
	),
	Recipe(
		'Alternate:_Fine_Black_Powder',
		inputs=[
			RecipeInput(ERessource.SULFUR, 7.5),
			RecipeInput(ERessource.COMPACTED_COAL, 3.75)
		],
		outputs=[RecipeOutput(ERessource.BLACK_POWDER, 15)]
	),
	Recipe(
		'Alternate:_Heat_Exchanger',
		inputs=[
			RecipeInput(ERessource.ALUMINUM_CASING, 30),
			RecipeInput(ERessource.RUBBER, 30)
		],
		outputs=[RecipeOutput(ERessource.HEAT_SINK, 10)]
	),
	Recipe(
		'Alternate:_Steeled_Frame',
		inputs=[
			RecipeInput(ERessource.REINFORCED_IRON_PLATE, 2),
			RecipeInput(ERessource.STEEL_PIPE, 10)
		],
		outputs=[RecipeOutput(ERessource.MODULAR_FRAME, 3)]
	),
	Recipe(
		'Alternate:_OC_Supercomputer',
		inputs=[
			RecipeInput(ERessource.RADIO_CONTROL_UNIT, 9),
			RecipeInput(ERessource.COOLING_SYSTEM, 9)
		],
		outputs=[RecipeOutput(ERessource.SUPERCOMPUTER, 3)]
	),
	Recipe(
		'Alternate:_Plutonium_Fuel_Unit',
		inputs=[
			RecipeInput(ERessource.ENCASED_PLUTONIUM_CELL, 10),
			RecipeInput(ERessource.PRESSURE_CONVERSION_CUBE, 0.5)
		],
		outputs=[RecipeOutput(ERessource.PLUTONIUM_FUEL_ROD, 0.5)]
	),
	Recipe(
		'Alternate:_Fused_Quickwire',
		inputs=[
			RecipeInput(ERessource.CATERIUM_INGOT, 7.5),
			RecipeInput(ERessource.COPPER_INGOT, 37.5)
		],
		outputs=[RecipeOutput(ERessource.QUICKWIRE, 90)]
	),
	Recipe(
		'Alternate:_Bolted_Iron_Plate',
		inputs=[
			RecipeInput(ERessource.IRON_PLATE, 90),
			RecipeInput(ERessource.SCREW, 250)
		],
		outputs=[RecipeOutput(ERessource.REINFORCED_IRON_PLATE, 15)]
	),
	Recipe(
		'Alternate:_Stitched_Iron_Plate',
		inputs=[
			RecipeInput(ERessource.IRON_PLATE, 18.75),
			RecipeInput(ERessource.WIRE, 37.5)
		],
		outputs=[RecipeOutput(ERessource.REINFORCED_IRON_PLATE, 5.625)]
	),
	Recipe(
		'Alternate:_Steel_Rotor',
		inputs=[
			RecipeInput(ERessource.STEEL_PIPE, 10),
			RecipeInput(ERessource.WIRE, 30)
		],
		outputs=[RecipeOutput(ERessource.ROTOR, 5)]
	),
	Recipe(
		'Alternate:_Rubber_Concrete',
		inputs=[
			RecipeInput(ERessource.LIMESTONE, 50),
			RecipeInput(ERessource.RUBBER, 10)
		],
		outputs=[RecipeOutput(ERessource.CONCRETE, 45)]
	),
	Recipe(
		'Alternate:_Cheap_Silica',
		inputs=[
			RecipeInput(ERessource.RAW_QUARTZ, 11.25),
			RecipeInput(ERessource.LIMESTONE, 18.75)
		],
		outputs=[RecipeOutput(ERessource.SILICA, 26.25)]
	),
	Recipe(
		'Alternate:_Quickwire_Stator',
		inputs=[
			RecipeInput(ERessource.STEEL_PIPE, 16),
			RecipeInput(ERessource.QUICKWIRE, 60)
		],
		outputs=[RecipeOutput(ERessource.STATOR, 8)]
	),
	Recipe(
		'Alternate:_Steel_Coated_Plate',
		inputs=[
			RecipeInput(ERessource.STEEL_INGOT, 7.5),
			RecipeInput(ERessource.PLASTIC, 5)
		],
		outputs=[RecipeOutput(ERessource.IRON_PLATE, 45)]
	),
	Recipe(
		'Alclad_Aluminum_Sheet',
		inputs=[
			RecipeInput(ERessource.ALUMINUM_INGOT, 30),
			RecipeInput(ERessource.COPPER_INGOT, 10)
		],
		outputs=[RecipeOutput(ERessource.ALCLAD_ALUMINUM_SHEET, 30)]
	),
	Recipe(
		'Circuit_Board',
		inputs=[
			RecipeInput(ERessource.COPPER_SHEET, 15),
			RecipeInput(ERessource.PLASTIC, 30)
		],
		outputs=[RecipeOutput(ERessource.CIRCUIT_BOARD, 7.5)]
	),
	Recipe(
		'Electromagnetic_Control_Rod',
		inputs=[
			RecipeInput(ERessource.STATOR, 6),
			RecipeInput(ERessource.AI_LIMITER, 4)
		],
		outputs=[RecipeOutput(ERessource.ELECTROMAGNETIC_CONTROL_ROD, 4)]
	),
	Recipe(
		'Encased_Industrial_Beam',
		inputs=[
			RecipeInput(ERessource.STEEL_BEAM, 24),
			RecipeInput(ERessource.CONCRETE, 30)
		],
		outputs=[RecipeOutput(ERessource.ENCASED_INDUSTRIAL_BEAM, 6)]
	),
	Recipe(
		'Fabric',
		inputs=[
			RecipeInput(ERessource.MYCELIA, 15),
			RecipeInput(ERessource.BIOMASS, 75)
		],
		outputs=[RecipeOutput(ERessource.FABRIC, 15)]
	),
	Recipe(
		'Black_Powder',
		inputs=[
			RecipeInput(ERessource.COAL, 7.5),
			RecipeInput(ERessource.SULFUR, 15)
		],
		outputs=[RecipeOutput(ERessource.BLACK_POWDER, 7.5)]
	),
	Recipe(
		'Heat_Sink',
		inputs=[
			RecipeInput(ERessource.ALCLAD_ALUMINUM_SHEET, 37.5),
			RecipeInput(ERessource.COPPER_SHEET, 22.5)
		],
		outputs=[RecipeOutput(ERessource.HEAT_SINK, 7.5)]
	),
	Recipe(
		'Reinforced_Iron_Plate',
		inputs=[
			RecipeInput(ERessource.IRON_PLATE, 30),
			RecipeInput(ERessource.SCREW, 60)
		],
		outputs=[RecipeOutput(ERessource.REINFORCED_IRON_PLATE, 5)]
	),
	Recipe(
		'Modular_Frame',
		inputs=[
			RecipeInput(ERessource.REINFORCED_IRON_PLATE, 3),
			RecipeInput(ERessource.IRON_ROD, 12)
		],
		outputs=[RecipeOutput(ERessource.MODULAR_FRAME, 2)]
	),
	Recipe(
		'Motor',
		inputs=[
			RecipeInput(ERessource.ROTOR, 10),
			RecipeInput(ERessource.STATOR, 10)
		],
		outputs=[RecipeOutput(ERessource.MOTOR, 5)]
	),
	Recipe(
		'Nobelisk',
		inputs=[
			RecipeInput(ERessource.BLACK_POWDER, 15),
			RecipeInput(ERessource.STEEL_PIPE, 30)
		],
		outputs=[RecipeOutput(ERessource.NOBELISK, 3)]
	),
	Recipe(
		'Encased_Plutonium_Cell',
		inputs=[
			RecipeInput(ERessource.PLUTONIUM_PELLET, 10),
			RecipeInput(ERessource.CONCRETE, 20)
		],
		outputs=[RecipeOutput(ERessource.ENCASED_PLUTONIUM_CELL, 5)]
	),
	Recipe(
		'Pressure_Conversion_Cube',
		inputs=[
			RecipeInput(ERessource.FUSED_MODULAR_FRAME, 1),
			RecipeInput(ERessource.RADIO_CONTROL_UNIT, 2)
		],
		outputs=[RecipeOutput(ERessource.PRESSURE_CONVERSION_CUBE, 1)]
	),
	Recipe(
		'Rotor',
		inputs=[
			RecipeInput(ERessource.IRON_ROD, 20),
			RecipeInput(ERessource.SCREW, 100)
		],
		outputs=[RecipeOutput(ERessource.ROTOR, 4)]
	),
	Recipe(
		'Smart_Plating',
		inputs=[
			RecipeInput(ERessource.REINFORCED_IRON_PLATE, 2),
			RecipeInput(ERessource.ROTOR, 2)
		],
		outputs=[RecipeOutput(ERessource.SMART_PLATING, 2)]
	),
	Recipe(
		'Versatile_Framework',
		inputs=[
			RecipeInput(ERessource.MODULAR_FRAME, 2.5),
			RecipeInput(ERessource.STEEL_BEAM, 30)
		],
		outputs=[RecipeOutput(ERessource.VERSATILE_FRAMEWORK, 5)]
	),
	Recipe(
		'Automated_Wiring',
		inputs=[
			RecipeInput(ERessource.STATOR, 2.5),
			RecipeInput(ERessource.CABLE, 50)
		],
		outputs=[RecipeOutput(ERessource.AUTOMATED_WIRING, 2.5)]
	),
	Recipe(
		'Assembly_Director_System',
		inputs=[
			RecipeInput(ERessource.ADAPTIVE_CONTROL_UNIT, 1.5),
			RecipeInput(ERessource.SUPERCOMPUTER, 0.75)
		],
		outputs=[RecipeOutput(ERessource.ASSEMBLY_DIRECTOR_SYSTEM, 0.75)]
	),
	Recipe(
		'Stator',
		inputs=[
			RecipeInput(ERessource.STEEL_PIPE, 15),
			RecipeInput(ERessource.WIRE, 40)
		],
		outputs=[RecipeOutput(ERessource.STATOR, 5)]
	)
]