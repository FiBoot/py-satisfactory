from enums import EContextMenu
import utils

class EContextMenuType:
    BASE = 'BASE'
    SUB = 'SUB'

class ContextMenu:
    def __init__(self):
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
        self.width = utils.calc_menu_width(items, EContextMenu.MIN_WIDTH, EContextMenu.CHAR_WIDTH)
        self.displayed = True

    def slide_sub_menu(self, dir):
        self.sub_menu.pos = (self.sub_menu.pos[0], self.sub_menu.pos[1] + dir * EContextMenu.SLIDE_HEIGHT)

    def collide(self, rel):
        if self.displayed:
            if self.sub_menu:
                return self.sub_menu.collide(rel)
            for index, item in enumerate(self.items):
                if item.collide(self.pos, self.width, rel, index):
                    match item.type:
                        case EContextMenuType.BASE:
                            item.callback(rel, item.args) if item.args else item.callback(rel)
                            return False
                        case EContextMenuType.SUB:
                            self.sub_menu = ContextMenu()
                            self.sub_menu.open(rel, item.sub_items)
                            return True
        return False

    def draw(self, GR):
        if self.displayed:
            for index, item in enumerate(self.items):
                item.draw(GR, self.pos, self.width, index)
            if self.sub_menu:
                self.sub_menu.draw(GR)
