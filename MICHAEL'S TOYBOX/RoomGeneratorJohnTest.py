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

defaultRoom1 = [
    [X, X, X, X, X],
    [X, O, O, X, X],
    [X, X, O, X, X],
    [X, O, O, O, X],
    [X, X, X, X, X]
]

defaultRoom2 = [
    [X, X, X, X, X],
    [X, O, X, O, X],
    [X, O, X, O, X],
    [X, O, X, O, X],
    [X, X, X, X, X]
]

defaultRoom3 = [
    [X, X, X, X, X],
    [X, O, O, O, X],
    [X, X, O, O, X],
    [X, O, O, O, X],
    [X, X, X, X, X]
]

defaultRoom4 = [
    [X, X, X, X, X],
    [X, O, X, O, X],
    [X, O, O, O, X],
    [X, X, X, O, X],
    [X, X, X, X, X]
]

defaultMap = [
    [defaultRoom1, defaultRoom2],
    [defaultRoom3, defaultRoom4]
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
        for room in roomRow:
            for tileRow in range(RoomHeight):
                for tileCol in range(RoomWidth):
                    #xOffset = (tileCol * TILESIZE)
                    #yOffset = (tileRow * TILESIZE)
                    xOffset = (tileCol * TILESIZE)
                    yOffset = (tileRow * TILESIZE)
                    pygame.draw.rect(screen, colors[room[tileRow][tileCol]], (xOffset + xRoomOffset, yOffset + yRoomOffset, TILESIZE, TILESIZE))
            xRoomOffset += TILESIZE * 5#len(RoomHeight)
        yRoomOffset += TILESIZE * 5#len(RoomWidth)
        xRoomOffset = 0
    pygame.display.flip()







    
