import pygame
import sys
from pygame.locals import *


DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
STONE = 4
GOLD = 5
DUNGEON = 6
TORCH_STONE_UP = 7
TORCH_STONE_DOWN = 8
RED_CARPET = 9

colors = {
    DIRT: pygame.image.load('dirt.png'),
    GRASS: pygame.image.load('grass.png'),
    WATER: pygame.image.load('water.png'),
    COAL: pygame.image.load('dirt.png'),
    STONE: pygame.image.load('stone.png'),
    GOLD: pygame.image.load('gold.png'),
    DUNGEON: pygame.image.load('dungeon.png'),
    TORCH_STONE_UP: pygame.image.load('torch_stone_up.png'),
    TORCH_STONE_DOWN: pygame.image.load('torch_stone_down.png'),
    RED_CARPET: pygame.image.load('red_carpet.png')
}


tilemap = [
    [GOLD, TORCH_STONE_DOWN, STONE, TORCH_STONE_DOWN, STONE, TORCH_STONE_DOWN, STONE, TORCH_STONE_DOWN, STONE, TORCH_STONE_DOWN],
    [GOLD, GOLD, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE],
    [GOLD, GOLD, GOLD, GOLD, RED_CARPET, RED_CARPET, RED_CARPET, RED_CARPET, RED_CARPET, RED_CARPET],
    [GOLD, GOLD, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE],
    [GOLD, TORCH_STONE_UP, STONE, TORCH_STONE_UP, STONE, TORCH_STONE_UP, STONE, TORCH_STONE_UP, STONE, TORCH_STONE_UP]
]

TILESIZE = 40
MAPWIDTH = 10
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