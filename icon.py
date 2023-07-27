import pygame
import utils
from data import ERessource

class EIcon:
    PATH = './assets/ressources/'
    EXT ='.png'

loaded_icons = []

def get_loaded_icon(name):
    for [icon_name, icon] in loaded_icons:
        if icon_name == name:
            return icon
    return

def get_icon(name):
    try:
        icon = pygame.image.load(f'{EIcon.PATH}{name}{EIcon.EXT}')
    except:
        icon = pygame.image.load(f'{EIcon.PATH}{ERessource.UNKNOW}{EIcon.EXT}')
    return icon
