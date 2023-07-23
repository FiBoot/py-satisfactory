from data import EConstruction
from recipes.minermk1 import MINERMK1_RECIPES
from recipes.minermk2 import MINERMK2_RECIPES
from recipes.minermk3 import MINERMK3_RECIPES
from recipes.oilextractor import OILEXTRACTOR_RECIPES
from recipes.waterextractor import WATEREXTRACTOR_RECIPES
from recipes.ressourcewellextractor import RESSOURCEWELLEXTRACTOR_RECIPES
from recipes.smelter import SMELTER_RECIPES
from recipes.foundry import FOUNDRY_RECIPES
from recipes.constructor import CONSTRUCTOR_RECIPES
from recipes.assembler import ASSEMBLER_RECIPES
from recipes.manufacturer import MANUFACTER_RECIPES

RECIPE_LIST = [
    (EConstruction.MINERMK1, MINERMK1_RECIPES),
    (EConstruction.MINERMK2, MINERMK2_RECIPES),
    (EConstruction.MINERMK3, MINERMK3_RECIPES),
    (EConstruction.OILEXTRACTOR, OILEXTRACTOR_RECIPES),
    (EConstruction.WATEREXTRACTOR, WATEREXTRACTOR_RECIPES),
    (EConstruction.RESSOURCEWELLEXTRACTOR, RESSOURCEWELLEXTRACTOR_RECIPES),
    (EConstruction.SMELTER, SMELTER_RECIPES),
    (EConstruction.FOUNDRY, FOUNDRY_RECIPES),
    (EConstruction.CONSTRUCTOR, CONSTRUCTOR_RECIPES),
    (EConstruction.ASSEMBLER, ASSEMBLER_RECIPES),
    (EConstruction.MANUFACTURER, MANUFACTER_RECIPES),
]