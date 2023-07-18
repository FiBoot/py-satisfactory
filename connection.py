import uuid
import pygame

CONNECTION_SIZE = 10
CONNECTION_LINE_SIZE = 3
CONNECTION_LINE_COLOR = '#999999'

class EConnectionType:
    OUTLET = 'OUTLET'
    INLET = 'INLET'

class EConnectionColor:
    OUTLET = 'red'
    INLET = 'green'

class Connection:
    def __init__(self, build, type = EConnectionType.OUTLET, pos = [0, 0]):
        self.uuid = uuid.uuid4().hex
        self.build = build
        self.type = type
        self.pos = pos
        self.connected_to = None
    
    def __str__(self):
        return f'{self.uuid} [{self.type}] ({self.build})'

    def draw(self, surface, build_pos):
        rect = pygame.Rect(build_pos[0] + self.pos[0], build_pos[1] + self.pos[1], CONNECTION_SIZE, CONNECTION_SIZE)
        color = EConnectionColor.OUTLET if self.type == EConnectionType.OUTLET else EConnectionColor.INLET
        pygame.draw.rect(surface, color, rect)
        # connection line
        if self.connected_to and self.type == EConnectionType.OUTLET:
            start_pos = [self.build.pos[0] + self.pos[0] + int(CONNECTION_SIZE / 2), self.build.pos[1] + self.pos[1] + int(CONNECTION_SIZE / 2)]
            end_pos = [self.connected_to.build.pos[0] + self.connected_to.pos[0] + int(CONNECTION_SIZE / 2), self.connected_to.build.pos[1] + self.connected_to.pos[1] + int(CONNECTION_SIZE / 2)]
            pygame.draw.line(surface, CONNECTION_LINE_COLOR, start_pos, end_pos, CONNECTION_LINE_SIZE)


    def collide(self, pos):        
        return pos[0] > self.pos[0] and pos[0] < self.pos[0] + CONNECTION_SIZE and pos[1] > self.pos[1] and pos[1] < self.pos[1] + CONNECTION_SIZE

    def connect(self, connection):
        self.connected_to = connection
        connection.connected_to = self
        print(f'{self} CONNECTED TO {connection}')