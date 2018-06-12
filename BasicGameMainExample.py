import pygame


pygame.init()
screen = pygame.display.set_mode((800,600))
run = True
#def quit(e): #optional event registration method
#    global run
#    run = False
#events.register(pygame.QUIT, quit)

clock = pygame.Clock()

while run:
    clock.tick(30)//30 FPS

    #Events First
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    #Physics Second

    #Rendering Third
    
    #if event.

pygame.quit()

