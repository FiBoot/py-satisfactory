import pygame
from context_menu import ContextMenu, ContextMenuItem
from build import Build
from enums import EScreen, EButtonType, EContextMenu

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


def create_building(rel):
    builds.append(Build(150, 80, rel))


def collide_build(pos):
    collided = None
    for build in builds:
        build.selected = False
        if build.collide(pos):
            collided = build
    if collided:
        collided.selected = True
    return collided


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
                        context_menu.open(event.pos, [
                            ContextMenuItem('create build', create_building),
                            ContextMenuItem('truc', create_building)
                        ])

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

    for build in builds:
        build.draw(screen)

    context_menu.draw(screen)


    # display
    pygame.display.flip()
    # limit fps
    clock.tick(EScreen.FPS)

pygame.quit()