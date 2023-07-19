from constructions.build import Build
from constructions.connection import Connection, EConnectionLet, EConnectionType


class ConveyorSpliter(Build):
    def __init__(self, pos):
        connections = [
            Connection(self, (10, 20), EConnectionLet.INLET),
            Connection(self, (0, 10)),
            Connection(self, (10, 0)),
            Connection(self, (20, 10)),
        ]
        Build.__init__(self, (40, 40), pos, connections)

class ConveyorMerger(Build):
    def __init__(self, pos):
        connections = [
            Connection(self, (10, 20)),
            Connection(self, (0, 10), EConnectionLet.INLET),
            Connection(self, (10, 0), EConnectionLet.INLET),
            Connection(self, (20, 10), EConnectionLet.INLET)
        ]
        Build.__init__(self, (40, 40), pos, connections)

LOGISTIC_CONSTRUCTIONS = [
    ['ConveyorSpliter', ConveyorSpliter],
    ['ConveyorMerger', ConveyorMerger],
]