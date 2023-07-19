import uuid
import pygame

class EConnection:
    SIZE = 20

class EConnectionLet:
    OUTLET = 'OUTLET'
    INLET = 'INLET'

class EConnectionType:
    BELT = 'BELT'
    PIPE = 'PIPE'

class EConnectionColor:
    OUTLET = '#00A6A6'
    INLET = '#F49F0A'

class Connection:
    def __init__(self, build, pos, let = EConnectionLet.OUTLET, type = EConnectionType.BELT):
        self.uuid = uuid.uuid4().hex
        self.build = build
        self.pos = pos
        self.let = let
        self.type = type
        self.connected_to = None
    
    def __str__(self):
        return f'{self.uuid} [{self.let}] ({self.build})'

    def draw(self, screen, build_pos):
        color = EConnectionColor.OUTLET if self.let == EConnectionLet.OUTLET else EConnectionColor.INLET
        match self.type:
            case EConnectionType.BELT:
                rect = pygame.Rect(build_pos[0] + self.pos[0], build_pos[1] + self.pos[1], EConnection.SIZE, EConnection.SIZE)
                pygame.draw.rect(screen, color, rect)
            case EConnectionType.PIPE:
                pos = (build_pos[0] + self.pos[0] + EConnection.SIZE // 2, build_pos[1] + self.pos[1] + EConnection.SIZE // 2)
                pygame.draw.circle(screen, color, pos, EConnection.SIZE // 2)
            
        # connection line
        if self.connected_to and self.let == EConnectionLet.OUTLET:
            start_pos = [self.build.pos[0] + self.pos[0] + EConnection.SIZE // 2, self.build.pos[1] + self.pos[1] + EConnection.SIZE // 2]
            end_pos = [self.connected_to.build.pos[0] + self.connected_to.pos[0] + EConnection.SIZE // 2, self.connected_to.build.pos[1] + self.connected_to.pos[1] + EConnection.SIZE // 2]
            pygame.draw.line(screen, 'white', start_pos, end_pos, 3)


    def collide(self, let):        
        return let[0] > self.pos[0] and let[0] < self.pos[0] + EConnection.SIZE and let[1] > self.pos[1] and let[1] < self.pos[1] + EConnection.SIZE

    def connect(self, connection):
        self.connected_to = connection
        connection.connected_to = self
        print(f'{self} CONNECTED TO {connection}')