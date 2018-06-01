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
    run = False

events.register(pygame.Quit, quit)

while run:
    # event handeling first
    events_test.update():

    # game physics second


    # rendering third
    graphics.render()

pygame.quit()
