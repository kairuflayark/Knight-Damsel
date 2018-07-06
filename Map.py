import pygame
import sys
from pygame.locals import *


DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
STONE = 4

colors = {
    DIRT: pygame.image.load('dirt.png'),
    GRASS: pygame.image.load('dirt.png'),
    WATER: pygame.image.load('water.png'),
    COAL: pygame.image.load('dirt.png'),
    STONE: pygame.image.load('stone.png')
}


tilemap = [
    [STONE, STONE, STONE, WATER, STONE],
    [DIRT, STONE, STONE, WATER, STONE],
    [COAL, STONE, WATER, WATER, STONE],
    [DIRT, STONE, STONE, STONE, STONE],
    [DIRT, DIRT, DIRT, COAL, COAL]
]

TILESIZE = 40
MAPWIDTH = 5
MAPHEIGHT = 5


pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(colors[tilemap[row][column]], (column*TILESIZE, row*TILESIZE))

        pygame.display.update()
