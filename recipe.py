import pygame
import utils
from icon import get_icon
from enums import EScreen, EColor, EContextMenu
from connection import EConnectionLet, EConnectionType

class RecipeComponent:
    def __init__(self, ressource, quantity, let = EConnectionLet.OUTLET, type = EConnectionType.BELT): # TODO typer les recipes definitions BELT/PIPE
        self.ressource = ressource
        self.quantity = round(quantity, 1)
        self.let = let

class RecipeOutput(RecipeComponent):
    def __init__(self, ressource, quantity):
        RecipeComponent.__init__(self, ressource, quantity)

class RecipeInput(RecipeComponent):
    def __init__(self, ressource, quantity):
        RecipeComponent.__init__(self, ressource, quantity, EConnectionLet.INLET)

class Recipe:
    def __init__(self, name, outputs, inputs = []):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs

    def draw_component(self, screen, font, pos, component):
        # icon
        icon = get_icon(component.ressource)
        screen.blit(icon, (pos[0], pos[1] + EScreen.PADDING // 2))
        # text
        text = font.render(f'{component.quantity}', True, EColor.OUTLET if component.let == EConnectionLet.OUTLET else EColor.INLET)
        screen.blit(text, (pos[0] + EScreen.COMPONENT_WIDTH + EScreen.PADDING // 2, pos[1] + EScreen.PADDING))
        # return next pos
        return (pos[0] - (EScreen.COMPONENT_WIDTH * 2 + EScreen.PADDING), pos[1])

    def draw(self, screen, font, pos, width, index):
        pos = utils.add_pair(pos, (width - (EScreen.COMPONENT_WIDTH * 2 + EScreen.PADDING * 2), EContextMenu.HEIGHT * index))
        for (index, component) in enumerate(self.outputs):
            pos = self.draw_component(screen, font, pos, component)
        for (index, component) in enumerate(self.inputs):
            pos = self.draw_component(screen, font, pos, component)