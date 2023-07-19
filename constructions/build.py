
import uuid
import pygame
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
    def __init__(self, size, pos, connections = [], shift = (0, 0)):
        self.uuid = uuid.uuid4().hex
        self.size = size
        self.pos = pos
        self.shift = shift
        self.move((0, 0)) # init grid_pos
        self.connections = connections
        self.selected = False

    def __str__(self):
        return f'{self.uuid} [{self.grid_pos[0]}, {self.grid_pos[1]}]'

    def move(self, rel):
        self.pos = self.pos[0] + rel[0], self.pos[1] + rel[1]
        self.grid_pos = align_pos_on_grid(self.pos, self.shift)

    def draw(self, screen):
        rect = pygame.Rect(self.grid_pos[0], self.grid_pos[1], self.size[0], self.size[1])
        color = EBuildColor.SELECTED if self.selected else EBuildColor.BASE
        pygame.draw.rect(screen, color, rect)
        for connection in self.connections:
            connection.draw(screen, self.grid_pos)

    def collide(self, rel):
        return rel[0] > self.grid_pos[0] and rel[0] < self.grid_pos[0] + self.size[0] and rel[1] > self.grid_pos[1] and rel[1] < self.grid_pos[1] + self.size[1]

    def collide_connection(self, rel):
        inside_pos = [rel[0] - self.grid_pos[0], rel[1] - self.grid_pos[1]]
        for connection in self.connections:
            if connection.collide(inside_pos):
                return connection
        return None