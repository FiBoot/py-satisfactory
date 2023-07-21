import pygame
from constructions.list import CONSTRUCTION_LIST
from context_menu import *
from enums import *

# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((EScreen.WIDTH + 1, EScreen.HEIGHT + 1))
font = pygame.font.SysFont(None, EContextMenu.FONT_SIZE)
clock = pygame.time.Clock()
context_menu = ContextMenu(font)


constructed_builds = []
active_build = None
active_connection = None


# context menu callbacks
def quit(rel, _):
    pygame.quit()

def create_building(rel, construction):
    constructed_builds.append(construction(rel))

def rotate_build(rel, build):
    build.rotate()

def delete_building(rel, build):
    constructed_builds.remove(build)
    build.delete()
    del build


# funcs
def construction_context_menu_items(constructions):
    menu_items = []
    for (list_name, construction_list) in constructions:
        sub_context_menu_items = []
        for (name, construction) in construction_list:
            sub_context_menu_items.append(ContextMenuBaseItem(name, create_building, construction))    
        menu_items.append(SubContextMenuItem(list_name, sub_context_menu_items))                    
    return menu_items

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

def draw_grid(screen):
    for i in range(0, (EScreen.WIDTH // EScreen.CELL_SIZE) + 1):
        color = EScreen.GRID_COLOR if i % 2 else EScreen.GRID_ALT_COLOR
        pygame.draw.line(screen, color, (i * EScreen.CELL_SIZE, 0), (i * EScreen.CELL_SIZE, EScreen.HEIGHT))
        pygame.draw.line(screen, color, (0, i * EScreen.CELL_SIZE), (EScreen.WIDTH, i * EScreen.CELL_SIZE))


# main loop
running = True
while running:
    
    # events
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False

            case pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                selected_build = get_selected_build(constructed_builds)
                if pressed_keys[pygame.K_r] and selected_build:
                    selected_build.rotate()
                if pressed_keys[pygame.K_d] and selected_build:
                    delete_building(None, selected_build)

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
                            context_menu.open(event.pos, [
                                ContextMenuBaseItem('Rotate', rotate_build, build),
                                ContextMenuBaseItem('Delete', delete_building, build),
                            ])
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
                            active_connection.try_connect(connection)
                    active_connection = None
                active_build = None

            case pygame.MOUSEMOTION:
                # move build
                if active_build and not active_connection:
                    active_build.move(event.rel)


    # render
    screen.fill(EScreen.BACKGROUND_COLOR)

    draw_grid(screen)

    for build in constructed_builds:
        build.draw(screen)
    for build in constructed_builds:
        build.draw_connection_lines(screen)

    context_menu.draw(screen)


    # display
    pygame.display.flip()
    # limit fps
    clock.tick(EScreen.FPS)

pygame.quit()