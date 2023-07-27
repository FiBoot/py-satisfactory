
class EScreen:
    FPS = 60
    WIDTH = 1200
    HEIGHT = 760
    CELL_SIZE = 10
    PADDING = 10
    COMPONENT_WIDTH = 20

class EColor:
    BACKGROUND = '#303030'
    FONT = '#101010'
    GRID = '#505050'
    GRID_ALT = '#505070'
    OUTLET = '#00A6A6'
    INLET = '#FE5A1D'
    CONNECTION_LINE = '#C0C0C0'
    CONTEXT_MENU = '#AAAAAA'

class EBuildType:
    PRODUCTION = 'Production'
    LOGISTIC = 'Logistic'
    EXTRACTOR = 'Extractor'

class EContextMenu:
    FONT_SIZE = 20
    MIN_WIDTH = 40
    HEIGHT = 30
    CHAR_WIDTH = 6
    SLIDE_HEIGHT = 40

class EButtonType:
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3

class EOrientation:
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3