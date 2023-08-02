import pygame
import utils
from enums import EScreen, EColor, EOrientation, EConnection, EConnectionLet, EConnectionType


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

def reset_connection(connection):
    if connection:
        if connection.connected_to:
            connection.connected_to.component = None
        connection.connected_to = None
        connection.build.process()


class Connection:
    def __init__(self, build, pos, orientation = EOrientation.NORTH, let = EConnectionLet.OUTLET, type = EConnectionType.BELT):
        self.build = build
        self.pos = pos
        self.orientation = orientation
        self.let = let
        self.type = type
        self.connected_to = None
        self.component = None

    @property
    def start_pos(self):
        return utils.sub_pair(self.pos, (EConnection.SIZE // 2, EConnection.SIZE // 2))

    def rotate(self):
        self.pos = (-self.pos[1], self.pos[0])
        self.orientation = (self.orientation + 1) % 4

    def reset_connection(self):
        reset_connection(self.connected_to)
        reset_connection(self)

    def try_connect(self, connection):
        if connection.let != self.let and connection.type == self.type:
            connection.reset_connection()
            if self.connected_to != None:
                self.connected_to.reset_connection()
            self.connected_to = connection
            connection.connected_to = self
            # start diggin
            self.build.find_start()

    def draw(self, screen, font, build_pos):
        color = EColor.OUTLET if self.let == EConnectionLet.OUTLET else EColor.INLET
        start_pos = utils.add_pair(self.start_pos, build_pos)
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
        # center
        center_pos = utils.add_pair(self.pos, build_pos)
        pygame.draw.circle(screen, 'purple', center_pos, 2)
        # output text
        if self.component and self.let == EConnectionLet.OUTLET:
            text = font.render(f'{round(self.component.quantity * self.build.ratio, 2)}', True, EColor.FLOATING_TEXT)
            match self.orientation:
                case EOrientation.NORTH:
                    text_pos = (center_pos[0] - EScreen.PADDING // 2, center_pos[1] - EScreen.FONT_SIZE)
                case EOrientation.EAST:
                    text_pos = (center_pos[0] + EScreen.FONT_SIZE // 2, center_pos[1] - EScreen.PADDING // 2)
                case EOrientation.SOUTH:
                    text_pos = (center_pos[0] - EScreen.PADDING // 2, center_pos[1] + EScreen.FONT_SIZE // 2)
                case EOrientation.WEST:
                    text_pos = (center_pos[0] - EScreen.FONT_SIZE, center_pos[1] - EScreen.PADDING // 2)
            screen.blit(text, text_pos)

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
        Connection.__init__(self, build, pos, orientation, type=EConnectionType.PIPE)

class PipeInlet(Connection):
    def __init__(self, build, pos, orientation = EOrientation.NORTH):
        Connection.__init__(self, build, pos, orientation, EConnectionLet.INLET, EConnectionType.PIPE)
