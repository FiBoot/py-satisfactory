
import pygame
import utils
from enums import EScreen

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
    def __init__(self, name, size, pos, connections = [], shift = (0, 0)):
        self.name = name
        self.size = size
        self.pos = (pos[0] + size[0] // 2, pos[1] + size[1] // 2)
        self.shift = shift
        self.move((0, 0)) # init grid_pos with shift
        self.connections = connections
        self.selected = False

    def __str__(self):
        return f'{self.name} {self.pos}'
    
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

    def draw(self, screen):
        # build
        rect = pygame.Rect(self.start_pos[0], self.start_pos[1], self.size[0], self.size[1])
        color = EBuildColor.SELECTED if self.selected else EBuildColor.BASE
        pygame.draw.rect(screen, color, rect)
        # connections
        for connection in self.connections:
            connection.draw(screen, self.grid_pos)
        # middle
        # pygame.draw.circle(screen, 'red', self.grid_pos, 2)
    
    def draw_connection_lines(self, screen):
        pass

    def collide(self, rel):
        return rel[0] > self.start_pos[0] and rel[0] < self.start_pos[0] + self.size[0] and rel[1] > self.start_pos[1] and rel[1] < self.start_pos[1] + self.size[1]

    def collide_connection(self, rel):
        inside_pos = utils.sub_pair(rel, self.grid_pos)
        for connection in self.connections:
            if connection.collide(inside_pos):
                return connection
        return None