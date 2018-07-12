import sys

import pygame

import michael
import text

import time
import AudioLoader #enables loading and unloading of music and sound
import Graphics #system to handle loading unloading and rendering of graphics
import Entities
import Events

#!!!! Priority write assignments !!!!
#Connect map to render
#add entities

#####INITIALIZATION#####
pygame.init()
screenRez = ((400,300))
#//screen = pygame.display.set_mode((800,600))
#background = load image here
Graphics.init(screenRez)
run = True

#Graphics.add("Assets/nobbynobs.png") #//player sprite
#player = Entities.Player()


def quit(e):
    global run
    if (e.type == pygame.KEYUP):
        if (e.key == pygame.K_F4 and e.mod & pygame.KMOD_ALT):
            run = False
    elif (e.type == pygame.QUIT):
        run = False
Events.register(pygame.QUIT, quit)
Events.register(pygame.KEYUP, quit)
#Events.register(pygame.KEYDOWN, player.key_handler)
#Events.register(pygame.KEYUP, player.key_handler)

clock = pygame.time.Clock()






#####GAME LOOP#####
while run:
    clock.tick(30)  #30 FPS

    ####Events First
    Events.update()
   
    ####Physics Second

    ####Graphics Third
    Graphics.render()

    #//michael.drawScreen(screen) #// ONLY A PLACEHOLDER FOR TESTING. REPLACE WITH MAP RENDERING.
    #//michael.drawTextBox(screen)
    #//michael.drawText(king, screen)
    #//pygame.display.flip()

    
pygame.quit()
sys.exit()
