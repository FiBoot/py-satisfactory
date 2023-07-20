import pygame
from enums import EContextMenu


class EContextMenuType:
    BASE = 'BASE',
    SUB = 'SUB'


class ContextMenuItem:
    def __init__(self, text):
        self.text = text

    def collide(self, pos, rel, index):
        height = index * EContextMenu.HEIGHT
        return True if rel[0] > pos[0] and rel[0] < pos[0] + EContextMenu.WIDTH and rel[1] > pos[1] + height and rel[1] < pos[1] + height + EContextMenu.HEIGHT else False

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
