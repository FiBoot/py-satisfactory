from constructions.build import Build
from constructions.connection import Connection, EConnectionLet, EConnectionType

class Smelter(Build):
    def __init__(self, pos):
        connections = [
            Connection(self, (20, 0)),
            Connection(self, (20, 80), EConnectionLet.INLET)
        ]
        Build.__init__(self, (60, 100), pos, connections, (0, 5))

class Foundry(Build):
    def __init__(self, pos):
        connections = [
            Connection(self, (60, 0)),
            Connection(self, (20, 70), EConnectionLet.INLET),
            Connection(self, (60, 70), EConnectionLet.INLET)
        ]
        Build.__init__(self, (100, 90), pos, connections)

class Constructor(Build):
    def __init__(self, pos):
        connections = [
            Connection(self, (30, 0)),
            Connection(self, (30, 80), EConnectionLet.INLET),
        ]
        Build.__init__(self, (80, 100), pos, connections)

class Assembler(Build):
    def __init__(self, pos):
        connections = [
            Connection(self, (40, 0)),
            Connection(self, (20, 130), EConnectionLet.INLET),
            Connection(self, (60, 130), EConnectionLet.INLET),
        ]
        Build.__init__(self, (100, 150), pos, connections)

class Manufacturer(Build):
    def __init__(self, pos):
        connections = [
            Connection(self, (80, 0)),
            Connection(self, (20, 180), EConnectionLet.INLET),
            Connection(self, (60, 180), EConnectionLet.INLET),
            Connection(self, (100, 180), EConnectionLet.INLET),
            Connection(self, (140, 180), EConnectionLet.INLET),
        ]
        Build.__init__(self, (180, 200), pos, connections)


class Refinery(Build):
    def __init__(self, pos):
        connections = [
            Connection(self, (20, 0), EConnectionLet.OUTLET, EConnectionType.PIPE),
            Connection(self, (60, 0), EConnectionLet.OUTLET, EConnectionType.BELT),
            Connection(self, (20, 180), EConnectionLet.INLET, EConnectionType.PIPE),
            Connection(self, (60, 180), EConnectionLet.INLET, EConnectionType.BELT),
        ]
        Build.__init__(self, (100, 200), pos, connections)

class Packager(Build):
    def __init__(self, pos):
        connections = [
            Connection(self, (30, 0), EConnectionLet.OUTLET, EConnectionType.BELT),
            Connection(self, (30, 20), EConnectionLet.OUTLET, EConnectionType.PIPE),
            Connection(self, (30, 60), EConnectionLet.INLET, EConnectionType.BELT),
            Connection(self, (30, 40), EConnectionLet.INLET, EConnectionType.PIPE),
        ]
        Build.__init__(self, (80, 80), pos, connections)

class Blender(Build):
    def __init__(self, pos):
        connections = [
            Connection(self, (100, 0), EConnectionLet.OUTLET, EConnectionType.BELT),
            Connection(self, (140, 0), EConnectionLet.OUTLET, EConnectionType.PIPE),
            Connection(self, (20, 140), EConnectionLet.INLET),
            Connection(self, (60, 140), EConnectionLet.INLET),
            Connection(self, (100, 140), EConnectionLet.INLET, EConnectionType.PIPE),
            Connection(self, (140, 140), EConnectionLet.INLET, EConnectionType.PIPE),
        ]
        Build.__init__(self, (180, 160), pos, connections)

PRODUCTION_CONSTRUCTIONS = [
    ['Smelter', Smelter],
    ['Foundry', Foundry],
    ['Constructor', Constructor],
    ['Assembler', Assembler],
    ['Manufacturer', Manufacturer],
    ['Refinery', Refinery],
    ['Packager', Packager],
    ['Blender', Blender],
]