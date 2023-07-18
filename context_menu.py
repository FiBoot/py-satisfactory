import pygame
from enums import EContextMenu

class ContextMenuItem:
    def __init__(self, text, callback, arg = None):
        self.text = text
        self.callback = callback
        self.arg = arg

    def collide(self, pos, rel, index):
        height = index * EContextMenu.HEIGHT
        return True if rel[0] > pos[0] and rel[0] < pos[0] + EContextMenu.WIDTH and rel[1] > pos[1] + height and rel[1] < pos[1] + height + EContextMenu.HEIGHT else False

    def draw(self, screen, font, pos, index):
        rect = pygame.Rect(pos[0], pos[1] + index * EContextMenu.HEIGHT, EContextMenu.WIDTH, EContextMenu.HEIGHT)
        pygame.draw.rect(screen, EContextMenu.COLOR, rect)
        text = font.render(self.text, True, EContextMenu.FONT_COLOR)
        screen.blit(text, (pos[0] + EContextMenu.PADDING, pos[1] + index * EContextMenu.HEIGHT + EContextMenu.PADDING))

class ContextMenu:
    def __init__(self, font):
        self.font = font
        self.items = []
        self.displayed = False

    def close(self):
        self.displayed = False

    def open(self, pos, items):
        self.pos = pos
        self.items = items
        self.displayed = True

    def collide(self, rel):
        if self.displayed:
            for index, item in enumerate(self.items):
                if item.collide(self.pos, rel, index):
                    item.callback(self.pos, item.arg)

    def draw(self, screen):
        if self.displayed:
            for index, item in enumerate(self.items):
                item.draw(screen, self.font, self.pos, index)
