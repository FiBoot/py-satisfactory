from enums import EContextMenu

class EContextMenuType:
    BASE = 'BASE',
    SUB = 'SUB'

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
