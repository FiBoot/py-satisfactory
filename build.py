
import uuid
import pygame
from connection import Connection, EConnectionType, CONNECTION_SIZE

class Build:
    def __init__(self, width, height, pos = [0, 0]):
        self.uuid = uuid.uuid4().hex
        self.width = width
        self.height = height
        self.pos = pos
        self.connections = [Connection(self), Connection(self, EConnectionType.INLET, [self.width - CONNECTION_SIZE, 0])]
        self.selected = False

    def __str__(self):
        return f'{self.uuid} [{self.pos[0]}, {self.pos[1]}]'

    def move(self, rel):
        self.pos = (self.pos[0] + rel[0], self.pos[1] + rel[1])

    def draw(self, screen):
        rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
        color = 'orange' if self.selected else 'purple'
        pygame.draw.rect(screen, color, rect)
        for connection in self.connections:
            connection.draw(screen, self.pos)

    def collide(self, rel):
        return rel[0] > self.pos[0] and rel[0] < self.pos[0] + self.width and rel[1] > self.pos[1] and rel[1] < self.pos[1] + self.height

    def collide_connection(self, rel):
        inside_pos = [rel[0] - self.pos[0], rel[1] - self.pos[1]]
        for connection in self.connections:
            if connection.collide(inside_pos):
                return connection
        return None