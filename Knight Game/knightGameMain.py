import pygame
import knighttext
import sys
#import time
#import AudioLoader #enables loading and unloading of music and sound
#import Graphics #system to handle loading unloading and rendering of graphics
#import Entities

#!!!! Priority write assignments !!!!

#import knightStory    #Stores story nodes to be called
#import knightEvents   #Stores game events
#import knightDungeon   #Procedural room/dungeon generation system

pygame.init()
screen = pygame.display.set_mode((800,600))
run = True

clock = pygame.time.Clock()

while run:
    clock.tick(30)  #30 FPS

    #Events First


    #Physics Second


    #Rendering Third
    #//Graphics.render()

    TextBox.Pane()  #//Shows a blank screen. REPLACE WITH MAP RENDERING


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
