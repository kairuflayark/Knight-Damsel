import pygame

import graphics
import entity
import events

pygame.init()

graphics.init((400, 400))
vizzi = entity.Vizzi()
graphics.add(vizzi)

graphics.background = graphics.load("vortex.png")


def quit(e):
    global run
    if e.type == pygame.KEYUP:
        if (e.key == pygame.K_F4 and
                e.mod & pygame.KMOD_ALT):
            run = False
    elif e.type == pygame.QUIT:
        run = False


events.register(pygame.QUIT, quit)
events.register(pygame.KEYUP, quit)
events.register(pygame.KEYDOWN, vizzi.key_handler)
events.register(pygame.KEYUP, vizzi.key_handler)

clock = pygame.time.Clock()
# vizzi.update()

run = True
while run:
    clock.tick(10)
    events.register(pygame.KEYDOWN, vizzi.key_handler)
    events.register(pygame.KEYUP, vizzi.key_handler)

    # event handling
    events.update()
    # game physics
    vizzi.update()
    # rendering
    graphics.render()

pygame.quit()