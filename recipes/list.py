from data import EConstruction
from recipes.miner_mk1 import MINER_MK1_RECIPES
from recipes.miner_mk2 import MINER_MK2_RECIPES
from recipes.miner_mk3 import MINER_MK3_RECIPES
from recipes.oil_extractor import OIL_EXTRACTOR_RECIPES
from recipes.water_extractor import WATER_EXTRACTOR_RECIPES
from recipes.ressource_well_extractor import RESSOURCEWELL_EXTRACTOR_RECIPES
from recipes.smelter import SMELTER_RECIPES
from recipes.foundry import FOUNDRY_RECIPES
from recipes.constructor import CONSTRUCTOR_RECIPES
from recipes.assembler import ASSEMBLER_RECIPES
from recipes.manufacturer import MANUFACTER_RECIPES
from recipes.refinery import REFINERY_RECIPES
from recipes.packager import PACKAGER_RECIPES
from recipes.particule_accelerator import PARTICULE_ACCELERATOR_RECIPES
from recipes.coal_generator import COAL_GENERATOR_RECIPES
from recipes.fuel_generator import FUEL_GENERATOR_RECIPES
from recipes.nuclear_power_plant import NUCLEAR_POWER_PLANT_RECIPES

RECIPE_LIST = [
    (EConstruction.MINER_MK1, MINER_MK1_RECIPES),
    (EConstruction.MINER_MK2, MINER_MK2_RECIPES),
    (EConstruction.MINER_MK3, MINER_MK3_RECIPES),
    (EConstruction.OIL_EXTRACTOR, OIL_EXTRACTOR_RECIPES),
    (EConstruction.WATER_EXTRACTOR, WATER_EXTRACTOR_RECIPES),
    (EConstruction.RESSOURCEWELL_EXTRACTOR, RESSOURCEWELL_EXTRACTOR_RECIPES),
    (EConstruction.SMELTER, SMELTER_RECIPES),
    (EConstruction.FOUNDRY, FOUNDRY_RECIPES),
    (EConstruction.CONSTRUCTOR, CONSTRUCTOR_RECIPES),
    (EConstruction.ASSEMBLER, ASSEMBLER_RECIPES),
    (EConstruction.MANUFACTURER, MANUFACTER_RECIPES),
    (EConstruction.REFINERY, REFINERY_RECIPES),
    (EConstruction.PACKAGER, PACKAGER_RECIPES),
    (EConstruction.PARTICULE_ACCELERATOR, PARTICULE_ACCELERATOR_RECIPES),
    (EConstruction.COAL_GENERATOR, COAL_GENERATOR_RECIPES),
    (EConstruction.FUEL_GENERATOR, FUEL_GENERATOR_RECIPES),
    (EConstruction.NUCLEAR_POWER_PLANT, NUCLEAR_POWER_PLANT_RECIPES),
]