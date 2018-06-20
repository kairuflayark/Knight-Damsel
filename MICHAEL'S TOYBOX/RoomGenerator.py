import sys
import pygame

TILESIZE = 40	#pixel size (width x height) of each tile
MAPWIDTH = 5	#number of columns in the tilemap
MAPHEIGHT = 5	#number of rows in the tilemap
RoomHeight = 5
RoomWidth = 5

#colors
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)

#tile values
X = 0	#impassable (closed) tile
O = 1	#passable (open) tile

#tile associations
colors = {
    X: BLACK,
    O: BROWN,
}

defaultRoom = [
    [X, X, X, X, X],
    [X, O, O, O, X],
    [X, O, O, O, X],
    [X, O, O, O, X],
    [X, X, X, X, X]
]
defaultMap = [
    [defaultRoom, defaultRoom],
    [defaultRoom, defaultRoom]
]

#INITIALIZATION
pygame.init()
screen = pygame.display.set_mode((MAPWIDTH*RoomWidth*TILESIZE, MAPHEIGHT*RoomWidth*TILESIZE))

while True:
    # EXIT CONDITION
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    xRoomOffset = 0
    yRoomOffset = 0
    for roomRow in defaultMap:
        xRoomOffset += 1
        for room in roomRow:
            yRoomOffset += 1
            for tileRow in range(RoomHeight):
                for tileCol in range(RoomWidth):
                    #xOffset = (tileCol * TILESIZE)
                    #yOffset = (tileRow * TILESIZE)
                    xOffset = (xRoomOffset * tileCol * TILESIZE)
                    yOffset = (yRoomOffset * tileRow * TILESIZE)
                    pygame.draw.rect(screen, colors[room[tileRow][tileCol]], (xOffset, yOffset, TILESIZE, TILESIZE))
    pygame.display.flip()