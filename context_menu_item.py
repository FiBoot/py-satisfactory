import pygame
from enums import EScreen, EColor, EContextMenu
from context_menu import EContextMenuType

class ContextMenuItem:
    def __init__(self, text, width = EContextMenu.WIDTH):
        self.text = text
        self.width = width

    def collide(self, pos, rel, index):
        height = index * EContextMenu.HEIGHT
        return True if rel[0] > pos[0] and rel[0] < pos[0] + self.width and rel[1] > pos[1] + height and rel[1] < pos[1] + height + EContextMenu.HEIGHT else False

    def draw(self, screen, font, pos, index):
        rect = pygame.Rect(pos[0], pos[1] + index * EContextMenu.HEIGHT, self.width, EContextMenu.HEIGHT)
        pygame.draw.rect(screen, EColor.CONTEXT_MENU, rect)
        text = font.render(self.text, True, EColor.FONT)
        screen.blit(text, (pos[0] + EScreen.PADDING, pos[1] + index * EContextMenu.HEIGHT + EScreen.PADDING))

class SubContextMenuItem(ContextMenuItem):
    def __init__(self, text, items):
        ContextMenuItem.__init__(self, text)
        self.type = EContextMenuType.SUB
        self.sub_items = items

# with callback
class ContextMenuBaseItem(ContextMenuItem):
    def __init__(self, text, callback, arg = None, width = EContextMenu.WIDTH):
        ContextMenuItem.__init__(self, text, width)
        self.type = EContextMenuType.BASE
        self.callback = callback
        self.arg = arg

class SubContextMenuRecipe(ContextMenuBaseItem):
    def __init__(self, callback, args):
        self.recipe = args[1]
        ContextMenuBaseItem.__init__(self, args[1].name, callback, args, EContextMenu.WIDTH * 6)

    def draw(self, screen, font, pos, index):
        calc_y = pos[1] + EContextMenu.HEIGHT * index
        rect = pygame.Rect(pos[0], calc_y, self.width, EContextMenu.HEIGHT)
        pygame.draw.rect(screen, EColor.CONTEXT_MENU, rect)
        text = font.render(self.text, True, EColor.FONT)
        screen.blit(text, (pos[0] + EScreen.PADDING, calc_y + EScreen.PADDING))
        self.recipe.draw(screen, font, pos, index)

