from build import Build
from data import EConstruction
from enums import EOrientation
from connection import BeltOutlet, BeltInlet, PipeOutlet, PipeInlet

class Logistic(Build):
    def __init__(self, type, pos, connections):
        Build.__init__(self, type, (40, 40), pos, connections)

    def process(self, level = 0):
        print(f'calculating ratio {self.type} ({level})')
        self.ratio = 1
        
        

class ConveyorSpliter(Logistic):
    def __init__(self, pos):
        connections = [
            BeltInlet(self, (0, 20), EOrientation.SOUTH),
            BeltOutlet(self, (-20, 0), EOrientation.WEST),
            BeltOutlet(self, (0, -20)),
            BeltOutlet(self, (20, 0), EOrientation.EAST),
        ]
        Logistic.__init__(self, EConstruction.CONVEYOR_SPLITER, pos, connections)

class ConveyorMerger(Logistic):
    def __init__(self, pos):
        connections = [
            BeltOutlet(self, (0, -20), EOrientation.NORTH),
            BeltInlet(self, (20, 0), EOrientation.EAST),
            BeltInlet(self, (0, 20), EOrientation.SOUTH),
            BeltInlet(self, (-20, 0), EOrientation.WEST),
        ]
        Logistic.__init__(self, EConstruction.CONVEYOR_MERGER, pos, connections)

class PipeSpliter(Logistic):
    def __init__(self, pos):
        connections = [
            PipeInlet(self, (0, 20), EOrientation.SOUTH),
            PipeOutlet(self, (-20, 0), EOrientation.WEST),
            PipeOutlet(self, (0, -20)),
            PipeOutlet(self, (20, 0), EOrientation.EAST),
        ]
        Logistic.__init__(self, EConstruction.PIPE_SPLITER, pos, connections)

class PipeMerger(Logistic):
    def __init__(self, pos):
        connections = [
            PipeOutlet(self, (0, -20), EOrientation.NORTH),
            PipeInlet(self, (20, 0), EOrientation.EAST),
            PipeInlet(self, (0, 20), EOrientation.SOUTH),
            PipeInlet(self, (-20, 0), EOrientation.WEST),
        ]
        Logistic.__init__(self, EConstruction.PIPE_MERGER, pos, connections)
