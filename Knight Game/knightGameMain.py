import sys

import pygame

import michael
import text


import time
import AudioLoader #enables loading and unloading of music and sound
import Graphics #system to handle loading unloading and rendering of graphics
import Entities

#!!!! Priority write assignments !!!!

#import knightStory    #Stores story nodes to be called
#import knightDungeon   #Procedural room/dungeon generation system

pygame.init()
screenRez = ((800,600))
#//screen = pygame.display.set_mode((800,600))
#background = load image here
Graphics.init(screenRez)
run = True

clock = pygame.time.Clock()

while run:
    clock.tick(30)  #30 FPS

    ####Events First
    #for i in range(0, 6):
    #    for j in range(0,2):
    ####Physics Second


    Graphics.render()

    #//michael.drawScreen(screen) #// ONLY A PLACEHOLDER FOR TESTING. REPLACE WITH MAP RENDERING.
    #//michael.drawTextBox(screen)
    #//michael.drawText(king, screen)
    #//pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
