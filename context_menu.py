import pygame
from enums import EContextMenu, EColor

class EContextMenuType:
    BASE = 'BASE',
    SUB = 'SUB'

class ContextMenuItem:
    def __init__(self, text):
        self.text = text
        self.width = EContextMenu.WIDTH

    def collide(self, pos, rel, index):
        height = index * EContextMenu.HEIGHT
        return True if rel[0] > pos[0] and rel[0] < pos[0] + self.width and rel[1] > pos[1] + height and rel[1] < pos[1] + height + EContextMenu.HEIGHT else False

    def draw(self, screen, font, pos, index):
        rect = pygame.Rect(pos[0], pos[1] + index * EContextMenu.HEIGHT, EContextMenu.WIDTH, EContextMenu.HEIGHT)
        pygame.draw.rect(screen, EContextMenu.COLOR, rect)
        text = font.render(self.text, True, EContextMenu.FONT_COLOR)
        screen.blit(text, (pos[0] + EContextMenu.PADDING, pos[1] + index * EContextMenu.HEIGHT + EContextMenu.PADDING))


class ContextMenuBaseItem(ContextMenuItem):
    def __init__(self, text, callback, arg = None):
        ContextMenuItem.__init__(self, text)
        self.type = EContextMenuType.BASE
        self.callback = callback
        self.arg = arg

class SubContextMenuRecipe(ContextMenuBaseItem):
    def __init__(self, callback, args):
        ContextMenuBaseItem.__init__(self, args[1].name, callback, args)
        self.width = EContextMenu.WIDTH * 2

    def draw_recipe_components(self, screen, font, pos, components, index, color):
        for component in components:
            text = font.render(f'{component.quantity}', True, color)
            try:
                icon = pygame.image.load(f'./assets/ressources/{component.ressource}.png') 
            except:
                icon = pygame.image.load('./assets/ressources/Not_Found.png')
            screen.blit(icon, (pos[0] + EContextMenu.RECIPE_COMPONENT_WIDTH * index, pos[1] + EContextMenu.PADDING // 2))
            screen.blit(text, (pos[0] + EContextMenu.RECIPE_COMPONENT_WIDTH * (index + 1) + EContextMenu.PADDING // 2, pos[1] + EContextMenu.PADDING))
            index += 1
        return index

    def draw(self, screen, font, pos, index):
        calc_pos = (pos[0] + EContextMenu.WIDTH, pos[1] + EContextMenu.HEIGHT * index)
        rect = pygame.Rect(pos[0], calc_pos[1], EContextMenu.WIDTH * 2, EContextMenu.HEIGHT)
        pygame.draw.rect(screen, EContextMenu.COLOR, rect)
        text = font.render(self.text, True, EContextMenu.FONT_COLOR)
        screen.blit(text, (pos[0] + EContextMenu.PADDING, calc_pos[1] + EContextMenu.PADDING))
        component_index = self.draw_recipe_components(screen, font, calc_pos, self.arg[1].inputs, 0, EColor.INLET_COLOR)
        calc_pos = (calc_pos[0] + EContextMenu.RECIPE_COMPONENT_WIDTH + EContextMenu.PADDING, calc_pos[1])
        self.draw_recipe_components(screen, font, calc_pos, self.arg[1].outputs, component_index, EColor.OUTLET_COLOR)


class SubContextMenuItem(ContextMenuItem):
    def __init__(self, text, items):
        ContextMenuItem.__init__(self, text)
        self.type = EContextMenuType.SUB
        self.sub_items = items


class ContextMenu:
    def __init__(self, font):
        self.font = font
        self.items = []
        self.sub_menu = None
        self.displayed = False

    def close(self):
        self.displayed = False
        if self.sub_menu:
            self.sub_menu.close()
            self.sub_menu = None

    def open(self, pos, items):
        self.close()
        self.pos = pos
        self.items = items
        self.displayed = True

    def slide_sub_menu(self, dir):
        self.sub_menu.pos = (self.sub_menu.pos[0], self.sub_menu.pos[1] + dir * EContextMenu.SLIDE_HEIGHT)

    def collide(self, rel):
        if self.displayed:
            if self.sub_menu:
                return self.sub_menu.collide(rel)
            for index, item in enumerate(self.items):
                if item.collide(self.pos, rel, index):
                    match item.type:
                        case EContextMenuType.BASE:
                            item.callback(self.pos, item.arg)
                            return False
                        case EContextMenuType.SUB:
                            self.sub_menu = ContextMenu(self.font)
                            self.sub_menu.open(rel, item.sub_items)
                            return True
        return False

    def draw(self, screen):
        if self.displayed:
            for index, item in enumerate(self.items):
                item.draw(screen, self.font, self.pos, index)
            if self.sub_menu:
                self.sub_menu.draw(screen)
