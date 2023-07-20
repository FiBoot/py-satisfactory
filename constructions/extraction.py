from build import Build
from connection import BeltOutlet, PipeOutlet


class MinerMk1(Build):
    def __init__(self, pos):
        connections = [BeltOutlet(self, (0, -70))]
        Build.__init__(self, (80, 140), pos, connections)

class MinerMk2(Build):
    def __init__(self, pos):
        connections = [BeltOutlet(self, (0, -70))]
        Build.__init__(self, (80, 140), pos, connections)

class MinerMk3(Build):
    def __init__(self, pos):
        connections = [BeltOutlet(self, (0, -70))]
        Build.__init__(self, (80, 140), pos, connections)

class OilExtractor(Build):
    def __init__(self, pos):
        connections = [PipeOutlet(self,(0, -70))]
        Build.__init__(self, (80, 140), pos, connections)

class WaterExtractor(Build):
    def __init__(self, pos):
        connections = [PipeOutlet(self, (0, -100))]
        Build.__init__(self, (200, 200), pos, connections)

class RessourceWellPressurizer(Build):
    def __init__(self, pos):
        Build.__init__(self, (200, 200), pos)

class RessourceWellExtractor(Build):
    def __init__(self, pos):
        connections = [PipeOutlet(self, (0, -25))]
        Build.__init__(self, (50, 50), pos, connections, (5, 0))


EXTRACTION_CONSTRUCTIONS = [
    ['MinerMk1', MinerMk1],
    ['MinerMk2', MinerMk2],
    ['MinerMk3', MinerMk3],
    ['OilExtractor', OilExtractor],
    ['WaterExtractor', WaterExtractor],
    ['RessourceWellPressurizer', RessourceWellPressurizer],
    ['RessourceWellExtractor', RessourceWellExtractor],
]