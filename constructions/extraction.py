from build import Build
from data import EConstruction
from connection import BeltOutlet, PipeOutlet

class MinerMk1(Build):
    def __init__(self, pos):
        connections = [BeltOutlet(self, (0, -70))]
        Build.__init__(self, EConstruction.MINER_MK1, (80, 140), pos, connections)

class MinerMk2(Build):
    def __init__(self, pos):
        connections = [BeltOutlet(self, (0, -70))]
        Build.__init__(self, EConstruction.MINER_MK2, (80, 140), pos, connections)

class MinerMk3(Build):
    def __init__(self, pos):
        connections = [BeltOutlet(self, (0, -70))]
        Build.__init__(self, EConstruction.MINER_MK3, (80, 140), pos, connections)

class OilExtractor(Build):
    def __init__(self, pos):
        connections = [PipeOutlet(self,(0, -70))]
        Build.__init__(self, EConstruction.OIL_EXTRACTOR, (80, 140), pos, connections)

class WaterExtractor(Build):
    def __init__(self, pos):
        connections = [PipeOutlet(self, (0, -100))]
        Build.__init__(self, EConstruction.WATER_EXTRACTOR, (200, 200), pos, connections)

class RessourceWellPressurizer(Build):
    def __init__(self, pos):
        Build.__init__(self, EConstruction.RESSOURCEWELL_PRESSURIZER, (200, 200), pos)

class RessourceWellExtractor(Build):
    def __init__(self, pos):
        connections = [PipeOutlet(self, (0, -25))]
        Build.__init__(self, EConstruction.RESSOURCEWELL_EXTRACTOR, (50, 50), pos, connections, (5, 0))
