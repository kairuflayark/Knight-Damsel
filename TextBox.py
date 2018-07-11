import pygame
import sys
import knighttext

white = (255,255,255)
black = (0,0,0)


class Pane(object):
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((600,400), 0, 32)
        self.screen.fill(white)
        pygame.display.update()

    def addText(self):
        # dimensions are X,Y, X2,Y2
        self.rect = pygame.draw.rect(self.screen, black, (0, 300, 600, 400))
        pygame.display.update()
        text = ["He sends you off with his trust"]
        # can display 54 characters / line

        # text = 'Testing one two three four five six seven eight nine ten'
        i = 0
        printT = 300
        myfont = pygame.font.SysFont("monospace", 20)
        # render text
        for i in range(0, len(text)):
            label = myfont.render(text[i], 1, (255, 255, 0))
            self.screen.blit(label, (2, printT))
            printT += 15
            i += 1
        pygame.display.update()


if __name__ == '__main__':
    Pan3 = Pane()
    Pan3.addText()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();
