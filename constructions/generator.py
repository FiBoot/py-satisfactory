from build import Build
from data import EConstruction
from enums import EOrientation
from connection import BeltOutlet, BeltInlet, PipeInlet

class Generator(Build):
    def __init__(self, type, size, pos, connections):
        Build.__init__(self, type, size, pos, connections)


class CoalGenerator(Generator):
    def __init__(self, pos):
        connections = [
            PipeInlet(self, (-20, 130), EOrientation.SOUTH),
            BeltInlet(self, (20, 130), EOrientation.SOUTH),
        ]
        Generator.__init__(self, EConstruction.COAL_GENERATOR, (100, 260), pos, connections)

class FuelGenerator(Generator):
    def __init__(self, pos):
        connections = [PipeInlet(self, (-0, 100), EOrientation.SOUTH)]
        Generator.__init__(self, EConstruction.FUEL_GENERATOR, (200, 200), pos, connections)

class NuclearPowerPlant(Generator):
    def __init__(self, pos):
        connections = [
            BeltInlet(self, (-20, 215), EOrientation.SOUTH),
            PipeInlet(self, (0, 215), EOrientation.SOUTH),
            BeltOutlet(self, (20, 215), EOrientation.SOUTH),
        ]
        Generator.__init__(self, EConstruction.NUCLEAR_POWER_PLANT, (380, 430), pos, connections)
