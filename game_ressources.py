import pygame
from enums import EScreen, ERessource

class GameRessources():
    def __init__(self):
        self.PATH = './assets/ressources/'
        self.EXT ='.png'

        # pygame setup
        pygame.init()
        pygame.font.init()

        self.icons = []
        self.font = pygame.font.SysFont(None, EScreen.FONT_SIZE)
        self.screen = pygame.display.set_mode((EScreen.WIDTH + 1, EScreen.HEIGHT + 1))

    def get_loaded_icon(self, icon_name):
        for [name, icon] in self.icons:
            if name == icon_name:
                return icon
        try:
            icon = pygame.image.load(f'{self.PATH}{icon_name}{self.EXT}')
        except:
            icon = pygame.image.load(f'{self.PATH}{ERessource.UNKNOW}{self.EXT}')
        print(f'adding new icon {icon_name}')
        self.icons.append((icon_name, icon))
        return icon

    def get_icon(self, icon_name):
        return self.get_loaded_icon(icon_name)
