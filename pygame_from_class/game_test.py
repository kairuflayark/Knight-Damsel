import pygame

import entity_test
import graphics_test
import events_test

graphics.init((400,400))
run = true
pygame.init();

graphics.background = graphics.load("background.png")

george = entity.George()
graphics.add(george)


def quit(e):
    global run
    if (e.type == pygame.KEYUP):
        if (e.key == pygame.K_F4 and e.mod & pygame.KMOD_ALT):
            run = False
    elif (e.type == pygame.QUIT):
        run = False

events.register(pygame.QUIT, quit)
events.register(pygame.KEYUP, quit)
events.register(pygame.KEYDOWN, george.key_handler)
events.register(pygame.KEYUP, george.key_handler)

clock = pygame.time.Clock()

while run:
    clock.tick(30)
    
    # event handeling first
    events_test.update():

    # game physics second


    # rendering third
    graphics.render()

pygame.quit()
