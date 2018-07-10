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
        text = ["He sends you off with his trust",
                  "With the note written you leave",
                  "Saddling your horse you leave"]
        # can display 54 characters / line
        # text = 'Testing one two three four five six seven eight nine ten'
        printT = 300
        printR = 2
        letterCount = 0
        # render ((content, [not sure what True does] (color of font)) (location to start drawing at)
        i = 0
        while text:
            self.screen.blit(self.font.render(text[i], True, (255,0,0)), (printR, printT))
            printT += 20
            i += 1
        pygame.display.update()

if __name__ == '__main__':
    Pan3 = Pane()
    Pan3.addText()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();