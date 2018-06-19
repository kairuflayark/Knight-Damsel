#IMPORTS
import sys
import pygame

import RoomRandomizer
import DungeonRoomRandomizer


#CONSTANTS

#Instructions for draw dimensions
TILESIZE = 40	#pixel size (width x height) of each tile
MAPWIDTH = 5	#number of columns in the tilemap
MAPHEIGHT = 5	#number of rows in the tilemap

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



#VARIABLES
done = False



#SETUP

#Create a randomized room of at least 4 tiles
#note: parameter must be between 4 and 9

	#RoomRandomizer.buildRoom(4)

#buildRoom randomizes the variable "RoomRandomizer.room"
room = DungeonRoomRandomizer.BuildDungeon()

#Map new room value to tile values
for row in range(len(room)):
	for column in range(len(room[row])):
		if room[row][column] == 0: room[row][column] = X
		else: room[row][column] = O
tilemap = room


#INITIALIZATION
pygame.init()
screen = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))



#PROCESS LOOP
while True:
	#EXIT CONDITION
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	#DRAW THE SCREEN
	#pygame.draw.rect([argument], [rgb argument(s)], {shape([x1], [y1], [x2], [y2]))
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			pygame.draw.rect(screen, colors[tilemap[row][column]], (column * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE))

	pygame.display.flip()



#CLEAN EXIT
#note: 	this will never be reached with the current logic.
#		exit logic is in the process loop.
pygame.quit()
sys.exit()