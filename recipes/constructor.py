from data import ERessource
from recipe import Recipe, RecipeInput, RecipeOutput

CONSTRUCTOR_RECIPES = [
    Recipe('Cable', inputs=[RecipeInput(ERessource.WIRE, 60)], outputs=[RecipeOutput(ERessource.CABLE, 30)]),
    Recipe('Wire', inputs=[RecipeInput(ERessource.COPPER_INGOT, 15)], outputs=[RecipeOutput(ERessource.WIRE, 30)]),
    Recipe('Concrete', inputs=[RecipeInput(ERessource.LIMESTONE, 45)], outputs=[RecipeOutput(ERessource.CONCRETE, 15)]),
    Recipe('Screw', inputs=[RecipeInput(ERessource.IRON_ROD, 10)], outputs=[RecipeOutput(ERessource.SCREW, 40)]),
    Recipe('Biomass', inputs=[RecipeInput(ERessource.LEAVES, 120)], outputs=[RecipeOutput(ERessource.BIOMASS, 60)]),
    Recipe('Biomass', inputs=[RecipeInput(ERessource.WOOD, 60)], outputs=[RecipeOutput(ERessource.BIOMASS, 300)]),
    Recipe('Iron Plate', inputs=[RecipeInput(ERessource.IRON_INGOT, 30)], outputs=[RecipeOutput(ERessource.IRON_PLATE, 20)]),
    Recipe('Iron Rod', inputs=[RecipeInput(ERessource.IRON_INGOT, 15)], outputs=[RecipeOutput(ERessource.IRON_ROD, 15)]),
    Recipe('Copper Sheet', inputs=[RecipeInput(ERessource.COPPER_INGOT, 20)], outputs=[RecipeOutput(ERessource.COPPER_SHEET, 10)]),
    Recipe('Empty Canister', inputs=[RecipeInput(ERessource.PLASTIC, 30)], outputs=[RecipeOutput(ERessource.EMPTY_CANISTER, 60)]),
    Recipe('Aluminum Casing', inputs=[RecipeInput(ERessource.ALUMINUM_INGOT, 90)], outputs=[RecipeOutput(ERessource.ALUMINUM_CASING, 60)]),
    Recipe('Quartz Crystal', inputs=[RecipeInput(ERessource.RAW_QUARTZ, 37.5)], outputs=[RecipeOutput(ERessource.QUARTZ_CRYSTAL, 22.5)]),
    Recipe('Silica', inputs=[RecipeInput(ERessource.RAW_QUARTZ, 22.5)], outputs=[RecipeOutput(ERessource.SILICA, 37.5)]),
    Recipe('Steel Beam', inputs=[RecipeInput(ERessource.STEEL_INGOT, 60)], outputs=[RecipeOutput(ERessource.STEEL_BEAM, 15)]),
    Recipe('Steel Pipe', inputs=[RecipeInput(ERessource.STEEL_INGOT, 30)], outputs=[RecipeOutput(ERessource.STEEL_PIPE, 20)]),
    Recipe('Empty Fluid Tank', inputs=[RecipeInput(ERessource.ALUMINUM_INGOT, 60)], outputs=[RecipeOutput(ERessource.EMPTY_FLUID_TANK, 60)]),
    Recipe('Copper Powder', inputs=[RecipeInput(ERessource.COPPER_INGOT, 300)], outputs=[RecipeOutput(ERessource.COPPER_POWDER, 50)]),
    Recipe('Solid Biofuel', inputs=[RecipeInput(ERessource.BIOMASS, 120)], outputs=[RecipeOutput(ERessource.SOLID_BIOFUEL, 60)]),
    Recipe('Hog Protein', inputs=[RecipeInput(ERessource.HOG_REMAINS, 20)], outputs=[RecipeOutput(ERessource.ALIEN_PROTEIN, 20)]),
    Recipe('Spitter Protein', inputs=[RecipeInput(ERessource.PLASMA_SPITTER_REMAINS, 20)], outputs=[RecipeOutput(ERessource.ALIEN_PROTEIN, 20)]),
    Recipe('Alien DNA Capsule', inputs=[RecipeInput(ERessource.ALIEN_PROTEIN, 10)], outputs=[RecipeOutput(ERessource.ALIEN_DNA_CAPSULE, 10)]),
    Recipe('Biomass', inputs=[RecipeInput(ERessource.ALIEN_PROTEIN, 15)], outputs=[RecipeOutput(ERessource.BIOMASS, 1500)]),
    Recipe('Hatcher Protein', inputs=[RecipeInput(ERessource.HATCHER_REMAINS, 20)], outputs=[RecipeOutput(ERessource.ALIEN_PROTEIN, 20)]),
    Recipe('Stinger Protein', inputs=[RecipeInput(ERessource.STINGER_REMAINS, 20)], outputs=[RecipeOutput(ERessource.ALIEN_PROTEIN, 20)]),
    Recipe('Quickwire', inputs=[RecipeInput(ERessource.CATERIUM_INGOT, 12)], outputs=[RecipeOutput(ERessource.QUICKWIRE, 60)]),
    Recipe('Biomass', inputs=[RecipeInput(ERessource.MYCELIA, 15)], outputs=[RecipeOutput(ERessource.BIOMASS, 150)]),
    # Power Shard (1)
    # Blue Power Slug 7.5
    # Power Shard 7.5 
    # Power Shard (2)
    # Yellow Power Slug 5
    # Power Shard 10
    # Power Shard (5)
    # Purple Power Slug 2.5 
    # Power Shard 12.5 
    Recipe('Color Cartridge', inputs=[RecipeInput(ERessource.FLOWER_PETALS, 50)], outputs=[RecipeOutput(ERessource.COLOR_CARTRIDGE, 100)]),
    Recipe('Iron Rebar', inputs=[RecipeInput(ERessource.IRON_ROD, 15)], outputs=[RecipeOutput(ERessource.IRON_REBAR, 15)]),
    Recipe('Alternate: Steel Canister', inputs=[RecipeInput(ERessource.STEEL_INGOT, 60)], outputs=[RecipeOutput(ERessource.EMPTY_CANISTER, 40)]),
    Recipe('Alternate: Steel Rod', inputs=[RecipeInput(ERessource.STEEL_INGOT, 12)], outputs=[RecipeOutput(ERessource.IRON_ROD, 48)]),
    Recipe('Alternate: Charcoal', inputs=[RecipeInput(ERessource.WOOD, 15)], outputs=[RecipeOutput(ERessource.COAL, 150)]),
    Recipe('Alternate: Biocoal', inputs=[RecipeInput(ERessource.BIOMASS, 37.5)], outputs=[RecipeOutput(ERessource.COAL, 45)]),
    Recipe('Alternate: Cast Screw', inputs=[RecipeInput(ERessource.IRON_INGOT, 12.5)], outputs=[RecipeOutput(ERessource.SCREW, 50)]),
    Recipe('Alternate: Steel Screw', inputs=[RecipeInput(ERessource.STEEL_BEAM , 5)], outputs=[RecipeOutput(ERessource.SCREW, 260)]),
    Recipe('Alternate: Iron Wire', inputs=[RecipeInput(ERessource.IRON_INGOT, 12.5)], outputs=[RecipeOutput(ERessource.WIRE, 22.5)]),
    Recipe('Alternate: Caterium Wire', inputs=[RecipeInput(ERessource.CATERIUM_INGOT, 15)], outputs=[RecipeOutput(ERessource.WIRE, 120)]),
]