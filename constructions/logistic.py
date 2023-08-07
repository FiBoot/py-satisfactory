from build import Build
from data import EConstruction
from enums import EOrientation, EConnectionLet
from connection import BeltOutlet, BeltInlet, PipeOutlet, PipeInlet
from recipe import RecipeOutput

class Logistic(Build):
    def __init__(self, type, pos, connections):
        Build.__init__(self, type, (40, 40), pos, connections)

    def draw_ratio(self, GR):
        pass

    def calc_ratio(self):
        self.ratio = 1

    def parent_copy(self, logistic_class):
        connections = []
        # copy connections
        for connection in self.connections:
            connections.append(connection.copy())
        new_logistic = logistic_class(self.type, self.pos, connections)
        # assign copied connection to their true own build
        for connection in new_logistic.connections:
            connection.build = new_logistic
        return new_logistic



class Splitter(Logistic):
    def __init__(self, type, pos, connections):
        Logistic.__init__(self, type, pos, connections)

    def calc_outputs(self):
        for connection in self.connections:
            # we dont care about input component because we only care about the linked connection output value
            connection.component = None
        splitter_input = None
        connected_outputs = []
        for connection in self.connections:
            if connection.let == EConnectionLet.INLET:
                if connection.connected_to:
                    # only 1 input in splitter
                    splitter_input = connection.connected_to
            if connection.let == EConnectionLet.OUTLET and connection.connected_to != None:
                connected_outputs.append(connection)
        if len(connected_outputs):
            if splitter_input and splitter_input.component :
                outputed_quantity = splitter_input.component.quantity * splitter_input.build.ratio / len(connected_outputs)
                for outputs in connected_outputs:
                    outputs.component = RecipeOutput(splitter_input.component.ressource, outputed_quantity)
            else:
                for outputs in connected_outputs:
                    outputs.component = None
    
    def copy(self):
        return self.parent_copy(Splitter)

class Merger(Logistic):
    def __init__(self, type, pos, connections):
        Logistic.__init__(self, type, pos, connections)

    def calc_outputs(self):
        output_component = None
        outlet = None
        for connection in self.connections:
            if connection.let == EConnectionLet.INLET and connection.connected_to and connection.connected_to.component:
                if output_component != None:
                    if output_component.ressource == connection.connected_to.component.ressource:
                       output_component.quantity += connection.connected_to.component.quantity * connection.connected_to.build.ratio
                else: output_component = RecipeOutput(connection.connected_to.component.ressource, connection.connected_to.component.quantity * connection.connected_to.build.ratio)
            elif connection.let == EConnectionLet.OUTLET:
                outlet = connection
        outlet.component = output_component

    def copy(self):
        return self.parent_copy(Merger)


class ConveyorSpliter(Splitter):
    def __init__(self, pos):
        connections = [
            BeltInlet(self, (0, 20), EOrientation.SOUTH),
            BeltOutlet(self, (-20, 0), EOrientation.WEST),
            BeltOutlet(self, (0, -20)),
            BeltOutlet(self, (20, 0), EOrientation.EAST),
        ]
        Splitter.__init__(self, EConstruction.CONVEYOR_SPLITER, pos, connections)

class ConveyorMerger(Merger):
    def __init__(self, pos):
        connections = [
            BeltOutlet(self, (0, -20), EOrientation.NORTH),
            BeltInlet(self, (20, 0), EOrientation.EAST),
            BeltInlet(self, (0, 20), EOrientation.SOUTH),
            BeltInlet(self, (-20, 0), EOrientation.WEST),
        ]
        Merger.__init__(self, EConstruction.CONVEYOR_MERGER, pos, connections)

class PipeSpliter(Splitter):
    def __init__(self, pos):
        connections = [
            PipeInlet(self, (0, 20), EOrientation.SOUTH),
            PipeOutlet(self, (-20, 0), EOrientation.WEST),
            PipeOutlet(self, (0, -20)),
            PipeOutlet(self, (20, 0), EOrientation.EAST),
        ]
        Splitter.__init__(self, EConstruction.PIPE_SPLITER, pos, connections)

class PipeMerger(Merger):
    def __init__(self, pos):
        connections = [
            PipeOutlet(self, (0, -20), EOrientation.NORTH),
            PipeInlet(self, (20, 0), EOrientation.EAST),
            PipeInlet(self, (0, 20), EOrientation.SOUTH),
            PipeInlet(self, (-20, 0), EOrientation.WEST),
        ]
        Merger.__init__(self, EConstruction.PIPE_MERGER, pos, connections)
