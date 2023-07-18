import pygame
from build import Build

# pygame setup
pygame.init()
surface = pygame.display.set_mode((1600, 900))
clock = pygame.time.Clock()

builds = []
active_build = None
active_connection = None
selected_build = None
builds.append(Build(100, 60, [0, 100]))
builds.append(Build(30, 30, [100, 100]))
builds.append(Build(150, 80, [200, 300]))


def select_build(pos):
    selected_build = None
    for build in builds:
        build.selected = False
        if build.collide(pos):
            selected_build = build
    if selected_build:
        selected_build.selected = True
    return selected_build


running = True
while running:
    
    # events
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False
            case pygame.MOUSEBUTTONDOWN:
                selected_build = select_build(event.pos)
                active_build = selected_build
                if selected_build:
                    active_connection = selected_build.collide_connection(event.pos)
            case pygame.MOUSEBUTTONUP:
                if active_connection:
                    for build in builds:
                        if build != active_build and build.collide(event.pos):
                            connection = build.collide_connection(event.pos)
                            if connection and connection.type != active_connection.type:
                                active_connection.connect(connection)
                    active_connection = None
                active_build = None
            case pygame.MOUSEMOTION:
                if active_build and not active_connection:
                    active_build.move(event.rel)
            

    # render
    surface.fill('#333333')

    for build in builds:
        build.draw(surface)

    # display
    pygame.display.flip()

    # limit to 30 fps
    clock.tick(30)

pygame.quit()