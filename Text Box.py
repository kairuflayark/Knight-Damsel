import pygame
import sys


white = (255,255,255)
black = (0,0,0)


class Pane(object):
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption('Box Test')
        self.screen = pygame.display.set_mode((600,400), 0, 32)
        self.screen.fill(white)
        pygame.display.update()


    def addText(self):
        # dimensions are X,Y, X2,Y2
        self.rect = pygame.draw.rect(self.screen, black, (0, 300, 600, 400))
        pygame.display.update()
        # can display 54 characters / line
        # render ((content, [not sure what True does] (color of font)) (location to start drawing at)
        self.screen.blit(self.font.render('Testing one two three', True, (255,0,0)), (2, 300))
        pygame.display.update()

if __name__ == '__main__':
    Pan3 = Pane()
    Pan3.addText()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();