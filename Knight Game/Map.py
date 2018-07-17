import pygame
import sys
from pygame.locals import *
import Events
import AudioLoader



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

king_play = True
road_play = False
dungeon_entry_play = False
dungeon_mid_play = False
tilemap_play = False

def displayMap(mapNum, screen):
    global kings_chamber, road, tilemap, dungeon_entry, dungeon_mid, king_play, road_play, dungeon_entry_play, dungeon_mid_play, tilemap_play
    currentMap = []
    if mapNum == 0:
        currentMap = kings_chamber
    elif mapNum == 1:
        if king_play:
            AudioLoader.stopMusic()
            king_play = False
        currentMap = road
        if not road_play:
            AudioLoader.playSong = AudioLoader.songs[0]
            AudioLoader.playMusic(AudioLoader.playSong)
            road_play = True
    elif mapNum == 2:
        if road_play:
            AudioLoader.stopMusic()
            road_play = False
        currentMap = dungeon_entry
        if not dungeon_entry_play:
            AudioLoader.playSong = AudioLoader.songs[5]
            AudioLoader.playMusic(AudioLoader.playSong)
            dungeon_entry_play = True
    elif mapNum == 3:
        if dungeon_entry_play:
            AudioLoader.stopMusic()
            dungeon_entry_play = False
        currentMap = dungeon_mid
        if not dungeon_mid_play:
            AudioLoader.playSong = AudioLoader.songs[2]
            AudioLoader.playMusic(AudioLoader.playSong)
            dungeon_mid_play = True
    elif mapNum == 4:
        if dungeon_entry_play:
            AudioLoader.stopMusic()
            dungeon_entry_play = False
        currentMap = dungeon_mid
        if not dungeon_mid_play:
            AudioLoader.playSong = AudioLoader.songs[2]
            AudioLoader.playMusic(AudioLoader.playSong)
            dungeon_mid_play = True
    elif mapNum == 5:
        if dungeon_mid_play:
            AudioLoader.stopMusic()
            dungeon_mid_play = False
        currentMap = tilemap
        if not tilemap_play:
            AudioLoader.playSong = AudioLoader.songs[1]
            AudioLoader.playMusic(AudioLoader.playSong)
            tilemap_play = True
    elif mapNum >= 6:
        if dungeon_mid_play:
            AudioLoader.stopMusic()
            dungeon_mid_play = False
        currentMap = tilemap
        if not tilemap_play:
            AudioLoader.playSong = AudioLoader.songs[1]
            AudioLoader.playMusic(AudioLoader.playSong)
            tilemap_play = True
    #so on

    #print room
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            screen.blit(tiles[currentMap[row][column]], (column * TILESIZE, row * TILESIZE))

        


"""
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

"""
