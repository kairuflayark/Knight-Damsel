import sys
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

done = False
onePress = True

isBlue = True

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			pygame.quit()
			sys.exit()
	if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
		onePress = True
	if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and onePress:
		onePress = False
		if isBlue: isBlue = not isBlue
		else: isBlue = True
	if isBlue: color = (0, 128, 255)
	else: color = (255, 100, 0)
	#draws a rectangle
	#pygame.draw.rect([argument], [rgb argument], {shape([x1], [y1], [x2], [y2]))
	pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))

	pygame.display.flip()