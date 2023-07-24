
import pygame
import utils
from enums import EScreen, EColor, EContextMenu
from connection import EConnection, EConnectionLet

class EBuildColor:
    BASE = '#AD9D5C'
    SELECTED = '#D0E1D4'

def align_pos_on_grid(pos, shift):
    gap = (pos[0] % EScreen.CELL_SIZE, pos[1] % EScreen.CELL_SIZE)
    return (
        pos[0] + shift[0] + (EScreen.CELL_SIZE - gap[0] if gap[0] > EScreen.CELL_SIZE // 2 else -gap[0]),
        pos[1] + shift[1] + (EScreen.CELL_SIZE - gap[1] if gap[1] > EScreen.CELL_SIZE // 2 else -gap[1]),
    )

class Build:
    def __init__(self, type, size, pos, connections = [], shift = (0, 0)):
        self.type = type
        self.size = size
        self.pos = (pos[0] + size[0] // 2, pos[1] + size[1] // 2)
        self.shift = shift
        self.move((0, 0)) # init grid_pos with shift
        self.connections = connections
        self.selected = False
        self.recipe = None

    def __str__(self):
        return f'{self.type} {self.pos}'
    
    @property
    def start_pos(self):
        return (self.grid_pos[0] - self.size[0] // 2, self.grid_pos[1] - self.size[1] // 2)

    def delete(self):
        for connection in self.connections:
            if connection.connected_to:
                connection.connected_to.connected_to = None
            del connection

    def move(self, rel):
        self.pos = utils.add_pair(self.pos, rel)
        self.grid_pos = align_pos_on_grid(self.pos, self.shift)

    def rotate(self):
        self.size = (self.size[1], self.size[0])
        self.shift = (self.shift[1], self.shift[0])
        for connection in self.connections:
            connection.rotate()
    
    def draw_recipe_component(self, screen, font, components):
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
            try:
                icon = pygame.image.load(f'./assets/ressources/{component.ressource}.png') 
            except:
                icon = pygame.image.load('./assets/ressources/Not_Found.png')
            screen.blit(icon, (x, y))
            # text
            text = font.render(f'{component.quantity}', True, EColor.OUTLET if component.let == EConnectionLet.OUTLET else EColor.INLET)
            text_y = y - EContextMenu.FONT_SIZE + EScreen.PADDING // 2 if component.let == EConnectionLet.OUTLET else y + EScreen.COMPONENT_WIDTH
            screen.blit(text, (x + EScreen.PADDING // 4, text_y))

    def draw(self, screen, font):
        # build
        rect = pygame.Rect(self.start_pos[0], self.start_pos[1], self.size[0], self.size[1])
        color = EBuildColor.SELECTED if self.selected else EBuildColor.BASE
        pygame.draw.rect(screen, color, rect)
        # connections
        for connection in self.connections:
            connection.draw(screen, self.grid_pos)
        # draw recipe components
        if self.recipe:
            self.draw_recipe_component(screen, font, self.recipe.outputs)
            self.draw_recipe_component(screen, font, self.recipe.inputs)
        # middle
        pygame.draw.circle(screen, 'red', self.grid_pos, 2)
    
    def draw_connection_lines(self, screen, font):
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