from data import ERessource
from recipe import Recipe, RecipeInput, RecipeOutput

MANUFACTER_RECIPES = [
    Recipe(
		'Alternate: Automated_Miner',
		inputs=[
			RecipeInput(ERessource.MOTOR, 1),
			RecipeInput(ERessource.STEEL_PIPE, 4),
			RecipeInput(ERessource.IRON_ROD, 4),
			RecipeInput(ERessource.IRON_PLATE, 2)
		],
		outputs=[RecipeOutput(ERessource.PORTABLE_MINER, 1)]
	),
	Recipe(
		'Alternate: Crystal_Beacon',
		inputs=[
			RecipeInput(ERessource.STEEL_BEAM, 2),
			RecipeInput(ERessource.STEEL_PIPE, 8),
			RecipeInput(ERessource.CRYSTAL_OSCILLATOR, 0.5),
		],
		outputs=[RecipeOutput(ERessource.BEACON, 10)]
	),
	Recipe(
		'Alternate: Classic_Battery',
		inputs=[
			RecipeInput(ERessource.SULFUR, 45),
			RecipeInput(ERessource.ALCLAD_ALUMINUM_SHEET, 52.5),
			RecipeInput(ERessource.PLASTIC, 60),
			RecipeInput(ERessource.WIRE, 90)
		],
		outputs=[RecipeOutput(ERessource.BATTERY, 30)]
	),
	Recipe(
		'Alternate: Caterium_Computer',
		inputs=[
			RecipeInput(ERessource.CIRCUIT_BOARD, 26.25),
			RecipeInput(ERessource.QUICKWIRE, 105),
			RecipeInput(ERessource.RUBBER, 45),
		],
		outputs=[RecipeOutput(ERessource.COMPUTER, 3.75)]
	),
	Recipe(
		'Alternate: Insulated_Crystal_Oscillator',
		inputs=[
			RecipeInput(ERessource.QUARTZ_CRYSTAL, 18.75),
			RecipeInput(ERessource.RUBBER, 13.125),
			RecipeInput(ERessource.AI_LIMITER, 1.875),
		],
		outputs=[RecipeOutput(ERessource.CRYSTAL_OSCILLATOR, 1.875)]
	),
	Recipe(
		'Alternate: Flexible_Framework',
		inputs=[
			RecipeInput(ERessource.MODULAR_FRAME, 3.75),
			RecipeInput(ERessource.STEEL_BEAM, 22.5),
			RecipeInput(ERessource.RUBBER, 30),
		],
		outputs=[RecipeOutput(ERessource.VERSATILE_FRAMEWORK, 7.5)]
	),
	Recipe(
		'Alternate: Heavy_Flexible_Frame',
		inputs=[
			RecipeInput(ERessource.MODULAR_FRAME, 18.75),
			RecipeInput(ERessource.ENCASED_INDUSTRIAL_BEAM, 11.25),
			RecipeInput(ERessource.RUBBER, 75),
			RecipeInput(ERessource.SCREW, 390)
		],
		outputs=[RecipeOutput(ERessource.HEAVY_MODULAR_FRAME, 3.75)]
	),
	Recipe(
		'Alternate: Silicon_HighSpeed_Connector',
		inputs=[
			RecipeInput(ERessource.QUICKWIRE, 90),
			RecipeInput(ERessource.SILICA, 37.5),
			RecipeInput(ERessource.CIRCUIT_BOARD, 3),
		],
		outputs=[RecipeOutput(ERessource.HIGHSPEED_CONNECTOR, 3)]
	),
	Recipe(
		'Alternate: Automated_Speed_Wiring',
		inputs=[
			RecipeInput(ERessource.STATOR, 3.75),
			RecipeInput(ERessource.WIRE, 75),
			RecipeInput(ERessource.HIGHSPEED_CONNECTOR, 1.875),
		],
		outputs=[RecipeOutput(ERessource.AUTOMATED_WIRING, 7.5)]
	),
	Recipe(
		'Alternate: Heavy_Encased_Frame',
		inputs=[
			RecipeInput(ERessource.MODULAR_FRAME, 7.5),
			RecipeInput(ERessource.ENCASED_INDUSTRIAL_BEAM, 9.375),
			RecipeInput(ERessource.STEEL_PIPE, 33.75),
			RecipeInput(ERessource.CONCRETE, 20.625)
		],
		outputs=[RecipeOutput(ERessource.HEAVY_MODULAR_FRAME, 2.8125)]
	),
	Recipe(
		'Alternate: Rigour_Motor',
		inputs=[
			RecipeInput(ERessource.ROTOR, 3.75),
			RecipeInput(ERessource.STATOR, 3.75),
			RecipeInput(ERessource.CRYSTAL_OSCILLATOR, 1.25),
		],
		outputs=[RecipeOutput(ERessource.MOTOR, 7.5)]
	),
	Recipe(
		'Alternate: Seismic_Nobelisk',
		inputs=[
			RecipeInput(ERessource.BLACK_POWDER, 12),
			RecipeInput(ERessource.STEEL_PIPE, 12),
			RecipeInput(ERessource.CRYSTAL_OSCILLATOR, 1.5),
		],
		outputs=[RecipeOutput(ERessource.NOBELISK, 6)]
	),
	Recipe(
		'Alternate: Uranium_Fuel_Unit',
		inputs=[
			RecipeInput(ERessource.ENCASED_URANIUM_CELL, 20),
			RecipeInput(ERessource.ELECTROMAGNETIC_CONTROL_ROD, 2),
			RecipeInput(ERessource.CRYSTAL_OSCILLATOR, 0.6),
			RecipeInput(ERessource.BEACON, 1.2)
		],
		outputs=[RecipeOutput(ERessource.URANIUM_FUEL_ROD, 0.6)]
	),
	Recipe(
		'Alternate: Plastic_Smart_Plating',
		inputs=[
			RecipeInput(ERessource.REINFORCED_IRON_PLATE, 2.5),
			RecipeInput(ERessource.ROTOR, 2.5),
			RecipeInput(ERessource.PLASTIC, 7.5),
		],
		outputs=[RecipeOutput(ERessource.SMART_PLATING, 5)]
	),
	Recipe(
		'Alternate: Radio_Control_System',
		inputs=[
			RecipeInput(ERessource.CRYSTAL_OSCILLATOR, 1.5),
			RecipeInput(ERessource.CIRCUIT_BOARD, 15),
			RecipeInput(ERessource.ALUMINUM_CASING, 90),
			RecipeInput(ERessource.RUBBER, 45)
		],
		outputs=[RecipeOutput(ERessource.RADIO_CONTROL_UNIT, 4.5)]
	),
	Recipe(
		'Alternate: Radio_Connection_Unit',
		inputs=[
			RecipeInput(ERessource.HEAT_SINK, 15),
			RecipeInput(ERessource.HIGHSPEED_CONNECTOR, 7.5),
			RecipeInput(ERessource.QUARTZ_CRYSTAL, 45),
		],
		outputs=[RecipeOutput(ERessource.RADIO_CONTROL_UNIT, 3.75)]
	),
	Recipe(
		'Alternate: SuperState_Computer',
		inputs=[
			RecipeInput(ERessource.COMPUTER, 3.6),
			RecipeInput(ERessource.ELECTROMAGNETIC_CONTROL_ROD, 2.4),
			RecipeInput(ERessource.BATTERY, 24),
			RecipeInput(ERessource.WIRE, 54)
		],
		outputs=[RecipeOutput(ERessource.SUPERCOMPUTER, 2.4)]
	),
	Recipe(
		'Alternate: Turbo_Electric_Motor',
		inputs=[
			RecipeInput(ERessource.MOTOR, 6.5625),
			RecipeInput(ERessource.RADIO_CONTROL_UNIT, 8.4375),
			RecipeInput(ERessource.ELECTROMAGNETIC_CONTROL_ROD, 4.6875),
			RecipeInput(ERessource.ROTOR, 6.5625)
		],
		outputs=[RecipeOutput(ERessource.TURBO_MOTOR, 2.8125)]
	),
	Recipe(
		'Alternate: Turbo_Pressure_Motor',
		inputs=[
			RecipeInput(ERessource.MOTOR, 7.5),
			RecipeInput(ERessource.PRESSURE_CONVERSION_CUBE, 1.875),
			RecipeInput(ERessource.PACKAGED_NITROGEN_GAS, 45),
			RecipeInput(ERessource.STATOR, 15)
		],
		outputs=[RecipeOutput(ERessource.TURBO_MOTOR, 3.75)]
	),
	Recipe(
		'Alternate: Infused_Uranium_Cell',
		inputs=[
			RecipeInput(ERessource.URANIUM, 25),
			RecipeInput(ERessource.SILICA, 15),
			RecipeInput(ERessource.SULFUR, 25),
			RecipeInput(ERessource.QUICKWIRE, 75)
		],
		outputs=[RecipeOutput(ERessource.ENCASED_URANIUM_CELL, 20)]
	),
	Recipe(
		'Beacon',
		inputs=[
			RecipeInput(ERessource.IRON_PLATE, 22.5),
			RecipeInput(ERessource.IRON_ROD, 7.5),
			RecipeInput(ERessource.WIRE, 112.5),
			RecipeInput(ERessource.CABLE, 15)
		],
		outputs=[RecipeOutput(ERessource.BEACON, 7.5)]
	),
	Recipe(
		'Rifle_Cartridge',
		inputs=[
			RecipeInput(ERessource.BEACON, 3),
			RecipeInput(ERessource.STEEL_PIPE, 30),
			RecipeInput(ERessource.BLACK_POWDER, 30),
			RecipeInput(ERessource.RUBBER, 30)
		],
		outputs=[RecipeOutput(ERessource.RIFLE_CARTRIDGE, 15)]
	),
	Recipe(
		'Supercomputer',
		inputs=[
			RecipeInput(ERessource.COMPUTER, 3.75),
			RecipeInput(ERessource.AI_LIMITER, 3.75),
			RecipeInput(ERessource.HIGHSPEED_CONNECTOR, 5.625),
			RecipeInput(ERessource.PLASTIC, 52.5)
		],
		outputs=[RecipeOutput(ERessource.SUPERCOMPUTER, 1.875)]
	),
	Recipe(
		'Computer',
		inputs=[
			RecipeInput(ERessource.CIRCUIT_BOARD, 25),
			RecipeInput(ERessource.CABLE, 22.5),
			RecipeInput(ERessource.PLASTIC, 45),
			RecipeInput(ERessource.SCREW, 130)
		],
		outputs=[RecipeOutput(ERessource.COMPUTER, 2.5)]
	),
	Recipe(
		'Crystal_Oscillator',
		inputs=[
			RecipeInput(ERessource.QUARTZ_CRYSTAL, 18),
			RecipeInput(ERessource.CABLE, 14),
			RecipeInput(ERessource.REINFORCED_IRON_PLATE, 2.5),
		],
		outputs=[RecipeOutput(ERessource.CRYSTAL_OSCILLATOR, 1)]
	),
	Recipe(
		'Gas_Filter',
		inputs=[
			RecipeInput(ERessource.COAL, 37.5),
			RecipeInput(ERessource.RUBBER, 15),
			RecipeInput(ERessource.FABRIC, 15),
		],
		outputs=[RecipeOutput(ERessource.GAS_FILTER, 7.5)]
	),
	Recipe(
		'Iodine_Infused_Filter',
		inputs=[
			RecipeInput(ERessource.GAS_FILTER, 3.75),
			RecipeInput(ERessource.QUICKWIRE, 30),
			RecipeInput(ERessource.ALUMINUM_CASING, 3.75),
		],
		outputs=[RecipeOutput(ERessource.IODINE_INFUSED_FILTER, 3.75)]
	),
	Recipe(
		'HighSpeed_Connector',
		inputs=[
			RecipeInput(ERessource.QUICKWIRE, 210),
			RecipeInput(ERessource.CABLE, 37.5),
			RecipeInput(ERessource.CIRCUIT_BOARD, 3.75),
		],
		outputs=[RecipeOutput(ERessource.HIGHSPEED_CONNECTOR, 3.75)]
	),
	Recipe(
		'Heavy_Modular_Frame',
		inputs=[
			RecipeInput(ERessource.MODULAR_FRAME, 10),
			RecipeInput(ERessource.STEEL_PIPE, 30),
			RecipeInput(ERessource.ENCASED_INDUSTRIAL_BEAM, 10),
			RecipeInput(ERessource.SCREW, 200)
		],
		outputs=[RecipeOutput(ERessource.HEAVY_MODULAR_FRAME, 2)]
	),
	Recipe(
		'Turbo_Motor',
		inputs=[
			RecipeInput(ERessource.COOLING_SYSTEM, 7.5),
			RecipeInput(ERessource.RADIO_CONTROL_UNIT, 3.75),
			RecipeInput(ERessource.MOTOR, 7.5),
			RecipeInput(ERessource.RUBBER, 45)
		],
		outputs=[RecipeOutput(ERessource.TURBO_MOTOR, 1.875)]
	),
	Recipe(
		'Uranium_Fuel_Rod',
		inputs=[
			RecipeInput(ERessource.ENCASED_URANIUM_CELL, 20),
			RecipeInput(ERessource.ENCASED_INDUSTRIAL_BEAM, 1.2),
			RecipeInput(ERessource.ELECTROMAGNETIC_CONTROL_ROD, 2),
		],
		outputs=[RecipeOutput(ERessource.URANIUM_FUEL_ROD, 0.4)]
	),
	Recipe(
		'Plutonium_Fuel_Rod',
		inputs=[
			RecipeInput(ERessource.ENCASED_PLUTONIUM_CELL, 7.5),
			RecipeInput(ERessource.STEEL_BEAM, 4.5),
			RecipeInput(ERessource.ELECTROMAGNETIC_CONTROL_ROD, 1.5),
			RecipeInput(ERessource.HEAT_SINK, 2.5)
		],
		outputs=[RecipeOutput(ERessource.PLUTONIUM_FUEL_ROD, 0.25)]
	),
	Recipe(
		'Radio_Control_Unit',
		inputs=[
			RecipeInput(ERessource.ALUMINUM_CASING, 40),
			RecipeInput(ERessource.CRYSTAL_OSCILLATOR, 1.25),
			RecipeInput(ERessource.COMPUTER, 1.25),
		],
		outputs=[RecipeOutput(ERessource.RADIO_CONTROL_UNIT, 2.5)]
	),
	Recipe(
		'Modular_Engine',
		inputs=[
			RecipeInput(ERessource.MOTOR, 2),
			RecipeInput(ERessource.RUBBER, 15),
			RecipeInput(ERessource.SMART_PLATING, 2),
		],
		outputs=[RecipeOutput(ERessource.MODULAR_ENGINE, 1)]
	),
	Recipe(
		'Adaptive_Control_Unit',
		inputs=[
			RecipeInput(ERessource.AUTOMATED_WIRING, 7.5),
			RecipeInput(ERessource.CIRCUIT_BOARD, 5),
			RecipeInput(ERessource.HEAVY_MODULAR_FRAME, 1),
			RecipeInput(ERessource.COMPUTER, 1)
		],
		outputs=[RecipeOutput(ERessource.ADAPTIVE_CONTROL_UNIT, 1)]
	),
	Recipe(
		'Magnetic_Field_Generator',
		inputs=[
			RecipeInput(ERessource.VERSATILE_FRAMEWORK, 2.5),
			RecipeInput(ERessource.ELECTROMAGNETIC_CONTROL_ROD, 1),
			RecipeInput(ERessource.BATTERY, 5),
		],
		outputs=[RecipeOutput(ERessource.MAGNETIC_FIELD_GENERATOR, 1)]
	),
	Recipe(
		'Thermal_Propulsion_Rocket',
		inputs=[
			RecipeInput(ERessource.MODULAR_ENGINE, 2.5),
			RecipeInput(ERessource.TURBO_MOTOR, 1),
			RecipeInput(ERessource.COOLING_SYSTEM, 3),
			RecipeInput(ERessource.FUSED_MODULAR_FRAME, 1)
		],
		outputs=[RecipeOutput(ERessource.THERMAL_PROPULSION_ROCKET, 1)]
	)
]