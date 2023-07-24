from enums import EBuildType
from data import EConstruction
from constructions.production import *
from constructions.logistic import *
from constructions.extraction import *

CONSTRUCTION_LIST = [
    (EBuildType.PRODUCTION, [
        (EConstruction.SMELTER, Smelter),
        (EConstruction.FOUNDRY, Foundry),
        (EConstruction.CONSTRUCTOR, Constructor),
        (EConstruction.ASSEMBLER, Assembler),
        (EConstruction.MANUFACTURER, Manufacturer),
        (EConstruction.REFINERY, Refinery),
        (EConstruction.PACKAGER, Packager),
        (EConstruction.BLENDER, Blender),
        (EConstruction.PARTICULE_ACCELERATOR, ParticuleAccelerator),
    ]),
    (EBuildType.LOGISTIC, [
        (EConstruction.CONVEYORSPLITER, ConveyorSpliter),
        (EConstruction.CONVEYORMERGER, ConveyorMerger),
    ]),
    (EBuildType.EXTRACTOR, [
        (EConstruction.MINERMK1, MinerMk1),
        (EConstruction.MINERMK2, MinerMk2),
        (EConstruction.MINERMK3, MinerMk3),
        (EConstruction.OILEXTRACTOR, OilExtractor),
        (EConstruction.WATEREXTRACTOR, WaterExtractor),
        (EConstruction.RESSOURCEWELLPRESSURIZER, RessourceWellPressurizer),
        (EConstruction.RESSOURCEWELLEXTRACTOR, RessourceWellExtractor),
    ])
]