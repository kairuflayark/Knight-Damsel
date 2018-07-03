import pygame

import animation_test_events
import animation_test_graphics
import animation_test_entities

#initialization
pygame.init()
#screen = pygame.display.set_mode((800,600))
animation_test_graphics.init((800,600))
run = True
animation_test_graphics.background = animation_test_graphics.load("background.jpg")
coin = animation_test_entities.Coin()
animation_test_graphics.add(coin)


def quit(e):
    global run
    if (e.type == pygame.KEYUP):
        if (e.key == pygame.K_F4 and e.mod & pygame.KMOD_ALT):
            run = False
    elif (e.type == pygame.QUIT):
        run = False

animation_test_events.register(pygame.QUIT, quit)
animation_test_events.register(pygame.KEYUP, quit)
#events.register(pygame.KEYDOWN, george.key_handler)
#events.register(pygame.KEYUP, george.key_handler)

clock = pygame.time.Clock()

while run:
    clock.tick(30)#30 FPS

    #Events First
    animation_test_events.update()
    #for event in pygame.event.get():
    #    if event.type == pygame.QUIT:
    #        run = False
            
    #Physics Second
    coin.update()

    #Rendering Third
    animation_test_graphics.render()
    
    

pygame.quit()

