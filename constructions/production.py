from build import Build
from data import EConstruction
from enums import EOrientation
from connection import BeltOutlet, BeltInlet, PipeOutlet, PipeInlet

class Smelter(Build):
    def __init__(self, pos):
        connections = [
            BeltOutlet(self, (0, -50)),
            BeltInlet(self, (0, 50), EOrientation.SOUTH)
        ]
        Build.__init__(self, EConstruction.SMELTER, (60, 100), pos, connections, (0, 5))

class Foundry(Build):
    def __init__(self, pos):
        connections = [
            BeltOutlet(self, (20, -45)),
            BeltInlet(self, (-20, 45), EOrientation.SOUTH),
            BeltInlet(self, (20, 45), EOrientation.SOUTH)
        ]
        Build.__init__(self, EConstruction.FOUNDRY, (100, 90), pos, connections)

class Constructor(Build):
    def __init__(self, pos):
        connections = [
            BeltOutlet(self, (0, -50)),
            BeltInlet(self, (0, 50), EOrientation.SOUTH),
        ]
        Build.__init__(self, EConstruction.CONSTRUCTOR, (80, 100), pos, connections)

class Assembler(Build):
    def __init__(self, pos):
        connections = [
            BeltOutlet(self, (0, -75)),
            BeltInlet(self, (-20, 75), EOrientation.SOUTH),
            BeltInlet(self, (20, 75), EOrientation.SOUTH),
        ]
        Build.__init__(self, EConstruction.ASSEMBLER, (100, 150), pos, connections)

class Manufacturer(Build):
    def __init__(self, pos):
        connections = [
            BeltOutlet(self, (0, -100)),
            BeltInlet(self, (-60, 100), EOrientation.SOUTH),
            BeltInlet(self, (-20, 100), EOrientation.SOUTH),
            BeltInlet(self, (20, 100), EOrientation.SOUTH),
            BeltInlet(self, (60, 100), EOrientation.SOUTH),
        ]
        Build.__init__(self, EConstruction.MANUFACTURER, (180, 200), pos, connections)


class Refinery(Build):
    def __init__(self, pos):
        connections = [
            PipeOutlet(self, (-20, -100)),
            BeltOutlet(self, (20, -100)),
            PipeInlet(self, (-20, 100), EOrientation.SOUTH),
            BeltInlet(self, (20, 100), EOrientation.SOUTH),
        ]
        Build.__init__(self, EConstruction.REFINERY, (100, 200), pos, connections)

class Packager(Build):
    def __init__(self, pos):
        connections = [
            BeltOutlet(self, (0, -40)),
            PipeOutlet(self, (0, -20)),
            BeltInlet(self, (0, 20), EOrientation.SOUTH),
            PipeInlet(self, (0, 40), EOrientation.SOUTH),
        ]
        Build.__init__(self, EConstruction.PACKAGER, (80, 80), pos, connections)

class Blender(Build):
    def __init__(self, pos):
        connections = [
            BeltOutlet(self, (20, -80)),
            PipeOutlet(self, (60, -80)),
            BeltInlet(self, (-60, 80), EOrientation.SOUTH),
            BeltInlet(self, (-20, 80), EOrientation.SOUTH),
            PipeInlet(self, (20, 80), EOrientation.SOUTH),
            PipeInlet(self, (60, 80), EOrientation.SOUTH),
        ]
        Build.__init__(self, EConstruction.BLENDER, (180, 160), pos, connections)

class ParticuleAccelerator(Build):
    def __init__(self, pos):
        connections = [
            BeltOutlet(self, (-130, -120)),
            BeltInlet(self, (-170, 120), EOrientation.SOUTH),
            BeltInlet(self, (-130, 120), EOrientation.SOUTH),
            PipeInlet(self, (-90, 120), EOrientation.SOUTH),
        ]
        Build.__init__(self, EConstruction.PARTICULE_ACCELERATOR, (380, 240), pos, connections)
