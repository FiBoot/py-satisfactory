from build import Build
from data import EConstruction
from enums import EOrientation
from connection import BeltOutlet, BeltInlet

class ConveyorSpliter(Build):
    def __init__(self, pos):
        connections = [
            BeltOutlet(self, (0, -20)),
            BeltOutlet(self, (20, 0), EOrientation.EAST),
            BeltInlet(self, (0, 20), EOrientation.SOUTH),
            BeltOutlet(self, (-20, 0), EOrientation.WEST),
        ]
        Build.__init__(self, EConstruction.CONVEYORSPLITER, (40, 40), pos, connections)

class ConveyorMerger(Build):
    def __init__(self, pos):
        connections = [
            BeltInlet(self, (0, -20)),
            BeltInlet(self, (20, 0), EOrientation.EAST),
            BeltOutlet(self, (0, 20), EOrientation.SOUTH),
            BeltInlet(self, (-20, 0), EOrientation.WEST),
        ]
        Build.__init__(self, EConstruction.CONVEYORMERGER, (40, 40), pos, connections)
