import uuid
import pygame
import utils
from enums import EOrientation

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

def rect_by_orientation(pos, orientation, size):
   match orientation:
       case EOrientation.NORTH:
           pos = (pos[0], pos[1] + size // 2)
           size = (size, size // 2)
       case EOrientation.EAST:
           size = (size // 2, size)
       case EOrientation.SOUTH:
           size = (size, size // 2)
       case EOrientation.WEST:
           pos = (pos[0] + size // 2, pos[1])
           size = (size // 2, size)
   return pygame.Rect(pos, size)


class Connection:
    def __init__(self, build, pos, orientation = EOrientation.NORTH, let = EConnectionLet.OUTLET, type = EConnectionType.BELT):
        self.uuid = uuid.uuid4().hex
        self.build = build
        self.pos = pos
        self.orientation = orientation
        self.let = let
        self.type = type
        self.connected_to = None
    
    def __str__(self):
        return f'{self.uuid} [{self.let}] ({self.build})'

    @property
    def start_pos(self):
        return utils.sub_pair(self.pos, (EConnection.SIZE // 2, EConnection.SIZE // 2))

    def rotate(self):
        self.pos = (-self.pos[1], self.pos[0])
        self.orientation = (self.orientation + 1) % 4

    def draw(self, screen, build_pos):
        color = EConnectionColor.OUTLET if self.let == EConnectionLet.OUTLET else EConnectionColor.INLET
        start_pos = utils.add_pair(build_pos, self.start_pos)
        rect = rect_by_orientation(start_pos, self.orientation, EConnection.SIZE)
        match self.type:
            case EConnectionType.BELT:
                pygame.draw.rect(screen, color, rect)
            case EConnectionType.PIPE:
                match self.orientation:
                    case EOrientation.NORTH:
                        pygame.draw.rect(screen, color, rect, border_bottom_left_radius=EConnection.SIZE, border_bottom_right_radius=EConnection.SIZE)
                    case EOrientation.EAST:
                        pygame.draw.rect(screen, color, rect, border_top_left_radius=EConnection.SIZE, border_bottom_left_radius=EConnection.SIZE)
                    case EOrientation.SOUTH:
                        pygame.draw.rect(screen, color, rect, border_top_left_radius=EConnection.SIZE, border_top_right_radius=EConnection.SIZE)
                    case EOrientation.WEST:
                        pygame.draw.rect(screen, color, rect, border_bottom_right_radius=EConnection.SIZE, border_top_right_radius=EConnection.SIZE)
        pygame.draw.circle(screen, 'purple', utils.add_pair(self.pos, build_pos), 2)

    def collide(self, rel):
        return rel[0] > self.start_pos[0] and rel[0] < self.start_pos[0] + EConnection.SIZE and rel[1] > self.start_pos[1] and rel[1] < self.start_pos[1] + EConnection.SIZE


class BeltOutlet(Connection):
    def __init__(self, build, pos, orientation = EOrientation.NORTH):
        Connection.__init__(self, build, pos, orientation)

class BeltInlet(Connection):
    def __init__(self, build, pos, orientation = EOrientation.NORTH):
        Connection.__init__(self, build, pos, orientation, EConnectionLet.INLET)

class PipeOutlet(Connection):
    def __init__(self, build, pos, orientation = EOrientation.NORTH):
        Connection.__init__(self, build, pos, orientation, EConnectionLet.OUTLET, EConnectionType.PIPE)

class PipeInlet(Connection):
    def __init__(self, build, pos, orientation = EOrientation.NORTH):
        Connection.__init__(self, build, pos, orientation, EConnectionLet.INLET, EConnectionType.PIPE)
