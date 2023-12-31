import pygame
import utils
from enums import EScreen, EColor, EOrientation, EConnection, EConnectionLet

class Build:
    def __init__(self, type, size, pos, connections = [], shift = (0, 0)):
        self.orientation = EOrientation.NORTH
        self.type = type
        self.size = size
        self.pos = (pos[0] + size[0] // 2, pos[1] + size[1] // 2)
        self.shift = shift
        self.move((0, 0)) # init grid_pos with shift
        self.connections = connections
        self.selected = False
        self.recipe = None
        self.ratio = 0

    @property
    def start_pos(self):
        return (self.grid_pos[0] - self.size[0] // 2, self.grid_pos[1] - self.size[1] // 2)

    def disconnect(self):
        for connection in self.connections:
            connection.disconnect()

    def copy(self):
        connections = []
        # copy connections
        for connection in self.connections:
            connections.append(connection.copy())
        build = Build(self.type, self.size, self.pos, connections, self.shift)
        build.recipe = self.recipe
        # assign copied connection to their true own build
        for connection in build.connections:
            connection.build = build
        return build

    def align_pos_on_grid(self, pos, shift):
        gap = (pos[0] % EScreen.CELL_SIZE, pos[1] % EScreen.CELL_SIZE)
        return (
            pos[0] + shift[0] + (EScreen.CELL_SIZE - gap[0] if gap[0] > EScreen.CELL_SIZE // 2 else -gap[0]),
            pos[1] + shift[1] + (EScreen.CELL_SIZE - gap[1] if gap[1] > EScreen.CELL_SIZE // 2 else -gap[1]),
        )

    def move(self, rel):
        self.pos = utils.add_pair(self.pos, rel)
        self.grid_pos = self.align_pos_on_grid(self.pos, self.shift)

    def rotate(self):
        self.size = (self.size[1], self.size[0])
        self.shift = (self.shift[1], self.shift[0])
        self.orientation = (self.orientation + 1) % 4
        for connection in self.connections:
            connection.rotate()

    def calc_outputs(self):
        for connection in self.connections:
            # we dont care about input component because we only care about the linked connection output value
            connection.component = None
        if self.recipe != None:
            for output in self.recipe.outputs:
                for connection in self.connections:
                    if connection.component == None and connection.let == output.let: # TODO if con.type == input.type
                        connection.component = output
                        break
    
    def set_recipe(self, recipe):
        self.recipe = recipe
        self.calc_outputs()
        self.find_start()

    def draw_recipe_component(self, GR, components):
        offsets = [
            EScreen.COMPONENT_WIDTH // 2,
            EScreen.PADDING // 2 + EScreen.COMPONENT_WIDTH,
            EScreen.PADDING + EScreen.COMPONENT_WIDTH * 3//2,
            EScreen.PADDING * 3//2 + EScreen.COMPONENT_WIDTH * 2,
        ]
        start_x = self.grid_pos[0] - offsets[len(components) - 1]
        component_gap = EScreen.COMPONENT_WIDTH + EScreen.PADDING
        for (index, component) in enumerate(components):
            x = start_x + index * component_gap
            y = self.grid_pos[1] - EScreen.COMPONENT_WIDTH - EScreen.PADDING // 4 if component.let == EConnectionLet.OUTLET else self.grid_pos[1] + EScreen.PADDING // 4
            # icon
            icon = GR.get_icon(component.ressource)
            GR.screen.blit(icon, (x, y))
            # text
            text = GR.font.render(f'{component.quantity}', True, EColor.OUTLET if component.let == EConnectionLet.OUTLET else EColor.INLET)
            text_y = y - EScreen.FONT_SIZE + EScreen.PADDING // 2 if component.let == EConnectionLet.OUTLET else y + EScreen.COMPONENT_WIDTH
            GR.screen.blit(text, (x + EScreen.PADDING // 4, text_y))

    def draw_ratio(self, GR):
        match self.orientation:
            case EOrientation.NORTH:
                pos = (self.grid_pos[0] + self.size[0] // 2 + EScreen.PADDING, self.grid_pos[1])
            case EOrientation.EAST:
                pos = (self.grid_pos[0], self.grid_pos[1] + self.size[1] // 2 + EScreen.PADDING)
            case EOrientation.SOUTH:
                pos = (self.grid_pos[0] - (self.size[0] // 2 + EScreen.COMPONENT_WIDTH + EScreen.PADDING), self.grid_pos[1])
            case EOrientation.WEST:
                pos = (self.grid_pos[0], self.grid_pos[1] - (self.size[1] // 2 + EScreen.COMPONENT_WIDTH // 2 + EScreen.PADDING))
        text = GR.font.render(f'{round(self.ratio * 100)}%', True, EColor.FLOATING_TEXT)
        GR.screen.blit(text, pos)

    def draw(self, GR):
        # build
        rect = pygame.Rect(self.start_pos[0], self.start_pos[1], self.size[0], self.size[1])
        color = EColor.SELECTED_BUILD if self.selected else EColor.BASE_BUILD
        pygame.draw.rect(GR.screen, color, rect)
        # draw recipe components
        if self.recipe:
            self.draw_recipe_component(GR, self.recipe.outputs)
            self.draw_recipe_component(GR, self.recipe.inputs)
        # connections
        for connection in self.connections:
            connection.draw(GR, self.grid_pos)
        # center
        # pygame.draw.circle(screen, 'red', self.grid_pos, 2)

    def draw_connection_lines(self, screen):
        for connection in self.connections:
            if connection.connected_to and connection.let == EConnectionLet.OUTLET:
                connection_start_pos = utils.add_pair(self.grid_pos, connection.pos)
                connection_to_start_pos = utils.add_pair(connection.connected_to.build.grid_pos, connection.connected_to.pos)
                pygame.draw.line(screen, EColor.CONNECTION_LINE, connection_start_pos, connection_to_start_pos, EConnection.LINE_THICKNESS)

    def collide(self, rel):
        return rel[0] > self.start_pos[0] and rel[0] < self.start_pos[0] + self.size[0] and rel[1] > self.start_pos[1] and rel[1] < self.start_pos[1] + self.size[1]

    def collide_connection(self, rel):
        inside_pos = utils.sub_pair(rel, self.grid_pos)
        for connection in self.connections:
            if connection.collide(inside_pos):
                return connection
        return None
    
    def calc_ratio(self):
        if self.recipe != None:
            ratios = []
            for input in self.recipe.inputs:
                ratio = 0
                for connection in self.connections:
                    if connection.let == EConnectionLet.INLET:
                        if connection.connected_to != None and connection.connected_to.component != None and connection.connected_to.component.ressource == input.ressource:
                            ratio = connection.connected_to.component.quantity * connection.connected_to.build.ratio / input.quantity
                            ratio = 1 if ratio > 1 else ratio
                            break
                ratios.append(ratio)
            min_ratio = ratios[0] if len(ratios) else 1
            for ratio in ratios:
                min_ratio = ratio if ratio < min_ratio else min_ratio
            self.ratio = min_ratio

    def process_r(self, stack = []):
        if not utils.contains(self, stack):
            stack.append(self)
            self.calc_outputs()
            self.calc_ratio()
            # go up the chain
            for connection in self.connections:
                if connection.let == EConnectionLet.OUTLET and connection.connected_to:
                    connection.connected_to.build.process_r(stack)
    
    def process(self):
        self.process_r([])

    def find_start_r(self, stack = []):
        print(stack, self.type)
        if not utils.contains(self, stack):
            stack.append(self)
            connected = False
            for connection in self.connections:
                if connection.let == EConnectionLet.INLET and connection.connected_to != None:
                    connected = True
                    connection.connected_to.build.find_start_r(stack) # we go deeper
            if not connected:
                self.process() # start to go up

    def find_start(self):
        print('\nstart')
        self.find_start_r([])