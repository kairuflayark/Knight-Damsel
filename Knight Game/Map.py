import pygame
import sys
from pygame.locals import *
import Events




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
BUSH = 10
LAVA = 11


tiles = {
    DIRT: pygame.image.load('Tiles/dirt.png'),
    GRASS: pygame.image.load('Tiles/grass.png'),
    WATER: pygame.image.load('Tiles/water.png'),
    COAL: pygame.image.load('Tiles/dirt.png'),
    STONE: pygame.image.load('Tiles/stone.png'),
    GOLD: pygame.image.load('Tiles/gold.png'),
    DUNGEON: pygame.image.load('Tiles/dungeon.png'),
    TORCH_STONE_UP: pygame.image.load('Tiles/torch_stone_up.png'),
    TORCH_STONE_DOWN: pygame.image.load('Tiles/torch_stone_down.png'),
    RED_CARPET: pygame.image.load('Tiles/red_carpet.png'),
    BUSH: pygame.image.load('Tiles/bush.png'),
    LAVA: pygame.image.load('Tiles/lava.png')
}


tilemap = [
    [LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA],
    [LAVA, LAVA, LAVA, LAVA, LAVA, STONE, STONE, STONE, STONE, LAVA],
    [STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE],
    [LAVA, LAVA, LAVA, LAVA, LAVA, STONE, STONE, STONE, STONE, LAVA],
    [LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, LAVA, STONE, LAVA]
]

dungeon_mid = [
    [DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON],
    [DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, STONE, STONE, STONE, DUNGEON, DUNGEON],
    [STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE],
    [DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, STONE, STONE, STONE, DUNGEON, DUNGEON],
    [DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON]
]

dungeon_entry = [
    [DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, STONE, DUNGEON, DUNGEON, DUNGEON],
    [DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, STONE, DUNGEON, DUNGEON, DUNGEON],
    [STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE],
    [DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON],
    [DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON, DUNGEON]
]

road = [
    [GRASS, BUSH, GRASS, BUSH, GRASS, BUSH, GRASS, BUSH, GRASS, BUSH],
    [DIRT, DIRT, DIRT, DIRT, STONE, STONE, DIRT, DIRT, DIRT, DIRT],
    [STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE],
    [DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
    [GRASS, BUSH, GRASS, BUSH, GRASS, BUSH, GRASS, BUSH, GRASS, BUSH]
]

kings_chamber = [
    [GOLD, TORCH_STONE_DOWN, STONE, TORCH_STONE_DOWN, STONE, TORCH_STONE_DOWN, STONE, TORCH_STONE_DOWN, STONE, TORCH_STONE_DOWN],
    [GOLD, GOLD, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE],
    [GOLD, GOLD, GOLD, GOLD, RED_CARPET, RED_CARPET, RED_CARPET, RED_CARPET, RED_CARPET, RED_CARPET],
    [GOLD, GOLD, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE],
    [GOLD, TORCH_STONE_UP, STONE, TORCH_STONE_UP, STONE, TORCH_STONE_UP, STONE, TORCH_STONE_UP, STONE, TORCH_STONE_UP]
]

TILESIZE = 40
MAPWIDTH = 10
MAPHEIGHT = 5


def currentRoom():
    room = Events.Plot().currentRoom()
    if room == 0:
        return kings_chamber
    elif room == 1:
        return road
    elif room == 2:
        return dungeon_entry
    elif room == 3:
        return dungeon_mid
    elif room == 4:
        return dungeon_mid


pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(tiles[tilemap[row][column]], (column * TILESIZE, row * TILESIZE))

        pygame.display.update()

