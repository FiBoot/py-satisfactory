import gc
import pygame
import utils
from enums import *
from constructions.list import CONSTRUCTION_LIST
from recipes.list import RECIPE_LIST
from context_menu import ContextMenu
from context_menu_item import ContextMenuBaseItem, SubContextMenuItem, SubContextMenuRecipe

# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((EScreen.WIDTH + 1, EScreen.HEIGHT + 1))
font = pygame.font.SysFont(None, EScreen.FONT_SIZE)
clock = pygame.time.Clock()
context_menu = ContextMenu(font)

constructed_builds = []
active_build = None
active_connection = None
clipboard = None

# context menu callbacks
def quit(rel, _):
    pygame.quit()

def create_building(rel, construction):
    constructed_builds.append(construction(rel))

def rotate_build(rel, build):
    build.rotate()

def delete_building(rel, build):
    constructed_builds.remove(build)
    build.disconnect()
    del build

def select_recip(rel, args):
    [build, recipe] = args
    build.set_recipe(recipe)


# funcs
def collide_build(pos, builds):
    collided = None
    for build in builds:
        build.selected = False
        if build.collide(pos):
            collided = build
    if collided:
        collided.selected = True
    return collided

def get_selected_build(builds):
    for build in builds:
        if build.selected:
            return build
    return None

def construction_context_menu_items(constructions):
    menu_items = []
    for (list_name, construction_list) in constructions:
        sub_context_menu_items = []
        for (name, construction) in construction_list:
            sub_context_menu_items.append(ContextMenuBaseItem(name, create_building, construction))    
        menu_items.append(SubContextMenuItem(list_name, sub_context_menu_items))                    
    return menu_items

def get_recipe_list(build):
    for [name, recipes] in RECIPE_LIST:
        if name == build.type:
            return recipes
    return None

def build_recipe_list_menu_items(build):
    menu_item = []
    recipe_list = get_recipe_list(build)
    if recipe_list:
        recipe_menu_width = utils.calc_recipe_menu_width(recipe_list, EScreen.COMPONENT_WIDTH + EScreen.PADDING)
        for recipe in recipe_list:
            menu_item.append(SubContextMenuRecipe(select_recip, build, recipe, recipe_menu_width))
        return SubContextMenuItem('Recipes', menu_item)
    return None

def draw_grid(screen):
    for i in range(0, (EScreen.WIDTH // EScreen.CELL_SIZE) + 1):
        color = EColor.GRID if i % 2 else EColor.GRID_ALT
        pygame.draw.line(screen, color, (i * EScreen.CELL_SIZE, 0), (i * EScreen.CELL_SIZE, EScreen.HEIGHT))
        pygame.draw.line(screen, color, (0, i * EScreen.CELL_SIZE), (EScreen.WIDTH, i * EScreen.CELL_SIZE))


print('gc threshold')
print(gc.get_threshold())
# main loop
frame = 0
running = True
while running:
    
    # events
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False

            case pygame.MOUSEWHEEL:
                if context_menu.displayed and context_menu.sub_menu:
                    context_menu.slide_sub_menu(event.y)

            case pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                selected_build = get_selected_build(constructed_builds)
                if pressed_keys[pygame.K_r] and selected_build:
                    selected_build.rotate()
                if pressed_keys[pygame.K_d] and selected_build:
                    delete_building(None, selected_build)
                if pressed_keys[pygame.K_c]:
                    build = collide_build(pygame.mouse.get_pos(), constructed_builds)
                    if build:
                        clipboard = build.copy()
                if pressed_keys[pygame.K_v] and clipboard:
                    new_build = clipboard.copy()
                    new_build.pos = pygame.mouse.get_pos()
                    new_build.move((0, 0))
                    constructed_builds.append(new_build)

            case pygame.MOUSEBUTTONDOWN:
                match event.button: 
                    case EButtonType.LEFT:
                        # context menu
                        if context_menu.displayed:
                            menu_collide = context_menu.collide(event.pos)
                            if not menu_collide:
                                context_menu.close()
                        # active build
                        active_build = collide_build(event.pos, constructed_builds)
                        if active_build:
                            active_connection = active_build.collide_connection(event.pos)

                    case EButtonType.RIGHT:
                        # open context menu
                        build = collide_build(event.pos, constructed_builds)
                        if build:
                            menu_items = [
                                ContextMenuBaseItem('Rotate', rotate_build, build),
                                ContextMenuBaseItem('Delete', delete_building, build),
                            ]
                            recipe_menu_items = build_recipe_list_menu_items(build)
                            if recipe_menu_items:
                                menu_items.insert(0, recipe_menu_items)
                            context_menu.open(event.pos, menu_items)
                        else:
                            menu_items = construction_context_menu_items(CONSTRUCTION_LIST)
                            menu_items.append(ContextMenuBaseItem('Quit', quit, running))
                            context_menu.open(event.pos, menu_items)

            case pygame.MOUSEBUTTONUP:
                # connection
                if active_connection:
                    for build in constructed_builds:
                        if build != active_build and build.collide(event.pos):
                            connection = build.collide_connection(event.pos)
                            if connection:
                                active_connection.try_connect(connection)
                    active_connection = None
                active_build = None

            case pygame.MOUSEMOTION:
                # move build
                if active_build and not active_connection:
                    active_build.move(event.rel)


    # render
    screen.fill(EColor.BACKGROUND)

    draw_grid(screen)

    for build in constructed_builds:
        build.draw(screen, font)
    for build in constructed_builds:
        build.draw_connection_lines(screen)
    for build in constructed_builds:
        build.draw_ratio(screen, font)

    context_menu.draw(screen)

    # display
    pygame.display.flip()
    # limit fps
    clock.tick(EConfig.FPS)

    if frame % EConfig.GC_TIMEOUT == 0:
        gc.collect()

    frame += 1

pygame.quit()