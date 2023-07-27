import pygame
from enums import EScreen, EColor, EContextMenu
from context_menu import EContextMenuType

class ContextMenuItem:
    def __init__(self, text):
        self.text = text

    def collide(self, pos, width, rel, index):
        height = index * EContextMenu.HEIGHT
        return True if rel[0] > pos[0] and rel[0] < pos[0] + width and rel[1] > pos[1] + height and rel[1] < pos[1] + height + EContextMenu.HEIGHT else False

    def draw(self, screen, font, pos, width, index):
        rect = pygame.Rect(pos[0], pos[1] + index * EContextMenu.HEIGHT, width, EContextMenu.HEIGHT)
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
    def __init__(self, text, callback, arg = None):
        ContextMenuItem.__init__(self, text)
        self.type = EContextMenuType.BASE
        self.callback = callback
        self.arg = arg

class SubContextMenuRecipe(ContextMenuBaseItem):
    def __init__(self, callback, build, recipe, recipe_menu_width):
        ContextMenuBaseItem.__init__(self, recipe.name, callback, (build, recipe))
        self.recipe = recipe
        self.recipe_menu_width = recipe_menu_width

    def draw(self, screen, font, pos, width, index):
        calc_y = pos[1] + EContextMenu.HEIGHT * index
        rect = pygame.Rect(pos[0], calc_y, width + self.recipe_menu_width, EContextMenu.HEIGHT)
        pygame.draw.rect(screen, EColor.CONTEXT_MENU, rect)
        text = font.render(self.text, True, EColor.FONT)
        screen.blit(text, (pos[0] + EScreen.PADDING, calc_y + EScreen.PADDING))
        self.recipe.draw(screen, font, pos, width + self.recipe_menu_width, index)

