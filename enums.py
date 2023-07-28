from data import *

class EScreen:
    FPS = 60
    WIDTH = 800
    HEIGHT = 800
    CELL_SIZE = 10
    PADDING = 10
    COMPONENT_WIDTH = 20

class EColor:
    BACKGROUND = '#303030'
    GRID = '#505050'
    GRID_ALT = '#505070'
    BASE_BUILD = '#AD9D5C'
    SELECTED_BUILD = '#D0E1D4'
    CONTEXT_MENU = '#AAAAAA'
    FONT = '#101010'
    OUTLET = '#00A6A6'
    INLET = '#FE5A1D'
    FLOATING = '#C0C0C0'

class EBuildType:
    PRODUCTION = 'Production'
    LOGISTIC = 'Logistic'
    EXTRACTOR = 'Extractor'
    GENERATOR = 'Generator'

class EButtonType:
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3

class EOrientation:
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


# context menu
class EContextMenu:
    FONT_SIZE = 20
    MIN_WIDTH = 40
    HEIGHT = 30
    CHAR_WIDTH = 6
    SLIDE_HEIGHT = 40


# connection
class EConnection:
    SIZE = 20
    LINE_THICKNESS = 5

class EConnectionLet:
    OUTLET = 'OUTLET'
    INLET = 'INLET'

class EConnectionType:
    BELT = 'BELT'
    PIPE = 'PIPE'

LOGISTIC_LIST = [EConstruction.CONVEYOR_SPLITER, EConstruction.PIPE_SPLITER, EConstruction.CONVEYOR_MERGER, EConstruction.PIPE_MERGER]