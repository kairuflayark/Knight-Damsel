#IMPORTS
import sys
import pygame

#CONSTANTS

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

#map to be drawn (letter 'O' not the number '0')
tilemap = [
    [X, X, X, X, X],
    [X, X, O, X, X],
    [X, O, O, X, X],
    [X, O, O, O, X],
    [X, X, X, X, X]
]

#Instructions for draw dimensions
TILESIZE = 40	#pixel size (width x height) of each tile
MAPWIDTH = 5	#number of columns in the tilemap
MAPHEIGHT = 5	#number of rows in the tilemap

#VARIABLES
done = False

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