import pygame

white = (255,255,255)
black = (0,0,0)
txtColor = (255, 0, 45)
brdr = 2 #The border size of the textbox. Currently using a black border.

sWidth = 800 #Width of the entire screen
sHeight = 600 #Height of the entire screen

class drawScreen:
    def __init__(self, screen):
        self.screen = screen
        self.screen.fill(white)
        #pygame.display.update()    #//when used in Main, it renders better with display.flip()

class drawTextBox():
    def __init__(self, screen):
        self.screen = screen
        self.borderbox = pygame.draw.rect(self.screen, black, (0, sHeight * 3/4, sWidth, sHeight))
        self.txtbox = pygame.draw.rect(self.screen, white, (brdr, (sHeight * 3/4) + brdr, sWidth - (brdr*2), sHeight - (brdr*2)))
        #pygame.display.update()    #//when used in Main, it renders better with display.flip()

class drawText():
    def __init__(self, text, screen):
        self.text = text
        self.screen = screen
        i = 0
        printT = sHeight * 3/4
        myfont = pygame.font.SysFont("monospace", 20)

        for i in range(0, len(text)):
            #myfont.render([text], [anti-alias], text color(r, g, b))
            label = myfont.render(text[i][0], 1, txtColor)
            self.screen.blit(label, (2, printT))
            printT += 15
            i += 1
        #pygame.display.update()    #//when used in Main, it renders better with display.flip()
