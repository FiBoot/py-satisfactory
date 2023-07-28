from enums import EBuildType
from data import EConstruction
from constructions.production import *
from constructions.logistic import *
from constructions.extraction import *
from constructions.generator import *

CONSTRUCTION_LIST = [
    (EBuildType.PRODUCTION, [
        (EConstruction.SMELTER, Smelter),
        (EConstruction.CONSTRUCTOR, Constructor),
        (EConstruction.ASSEMBLER, Assembler),
        (EConstruction.MANUFACTURER, Manufacturer),
        (EConstruction.REFINERY, Refinery),
        (EConstruction.PACKAGER, Packager),
        (EConstruction.FOUNDRY, Foundry),
        (EConstruction.BLENDER, Blender),
        (EConstruction.PARTICULE_ACCELERATOR, ParticuleAccelerator),
    ]),
    (EBuildType.LOGISTIC, [
        (EConstruction.CONVEYOR_SPLITER, ConveyorSpliter),
        (EConstruction.CONVEYOR_MERGER, ConveyorMerger),
        (EConstruction.PIPE_SPLITER, PipeSpliter),
        (EConstruction.PIPE_MERGER, PipeMerger),
    ]),
    (EBuildType.EXTRACTOR, [
        (EConstruction.MINER_MK1, MinerMk1),
        (EConstruction.MINER_MK2, MinerMk2),
        (EConstruction.MINER_MK3, MinerMk3),
        (EConstruction.OIL_EXTRACTOR, OilExtractor),
        (EConstruction.WATER_EXTRACTOR, WaterExtractor),
        (EConstruction.RESSOURCEWELL_PRESSURIZER, RessourceWellPressurizer),
        (EConstruction.RESSOURCEWELL_EXTRACTOR, RessourceWellExtractor),
    ]),
    (EBuildType.GENERATOR, [
        (EConstruction.COAL_GENERATOR, CoalGenerator),
        (EConstruction.FUEL_GENERATOR, FuelGenerator),
        (EConstruction.NUCLEAR_POWER_PLANT, NuclearPowerPlant),
    ])
]
