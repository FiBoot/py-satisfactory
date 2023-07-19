import pygame
from context_menu import ContextMenu, ContextMenuItem
from enums import EScreen, EButtonType, EContextMenu
from constructions.list import CONSTRUCTIONS

# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((EScreen.WIDTH, EScreen.HEIGHT))
font = pygame.font.SysFont(None, EContextMenu.FONT_SIZE)
clock = pygame.time.Clock()
context_menu = ContextMenu(font)


builds = []
active_build = None
active_connection = None


def construction_context_menu_items(constructions):
    menu_items = []
    for (name, construction) in constructions:
        menu_items.append(ContextMenuItem(f'Create {name}', create_building, construction))
    return menu_items

def collide_build(pos):
    collided = None
    for build in builds:
        build.selected = False
        if build.collide(pos):
            collided = build
    if collided:
        collided.selected = True
    return collided

def draw_grid(screen):
    for i in range(0, EScreen.WIDTH // EScreen.CELL_SIZE):
        pygame.draw.line(screen, EScreen.GRID_COLOR, (i * EScreen.CELL_SIZE, 0), (i * EScreen.CELL_SIZE, EScreen.HEIGHT))
        pygame.draw.line(screen, EScreen.GRID_COLOR, (0, i * EScreen.CELL_SIZE), (EScreen.WIDTH, i * EScreen.CELL_SIZE))


# context menu callbacks
def quit(rel, _):
    pygame.quit()

def create_building(rel, construction):
    builds.append(construction(rel))

def delete_building(rel, build):
    builds.remove(build)


running = True
while running:
    
    # events
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False

            case pygame.MOUSEBUTTONDOWN:
                match event.button: 
                    case EButtonType.LEFT:
                        # context menu
                        context_menu.collide(event.pos)
                        context_menu.close()
                        # active build
                        active_build = collide_build(event.pos)
                        if active_build:
                            active_connection = active_build.collide_connection(event.pos)

                    case EButtonType.RIGHT:
                        # open context menu
                        # TODO
                        build = collide_build(event.pos)
                        if build:
                            context_menu.open(event.pos, [
                                ContextMenuItem('Delete build', delete_building, build),
                            ])
                        else:
                            menu_items = construction_context_menu_items(CONSTRUCTIONS)
                            menu_items.append(ContextMenuItem('Quit', quit, running))
                            context_menu.open(event.pos, menu_items)

            case pygame.MOUSEBUTTONUP:
                # connection
                if active_connection:
                    for build in builds:
                        if build != active_build and build.collide(event.pos):
                            connection = build.collide_connection(event.pos)
                            if connection and connection.type != active_connection.type:
                                active_connection.connect(connection)
                    active_connection = None
                active_build = None

            case pygame.MOUSEMOTION:
                # move build
                if active_build and not active_connection:
                    active_build.move(event.rel)


    # render
    screen.fill(EScreen.BACKGROUND_COLOR)

    draw_grid(screen)

    for build in builds:
        build.draw(screen)

    context_menu.draw(screen)


    # display
    pygame.display.flip()
    # limit fps
    clock.tick(EScreen.FPS)

pygame.quit()