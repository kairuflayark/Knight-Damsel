import pygame

#!!!! Priority write assignments !!!!

#import knightStory    #Stores story nodes to be called
#import knightEvents   #Stores game events
#import knightGraphics #Stores the graphics system, handles sprites
#import knightDungen   #Procedural room/dungen generation system

pygame.init()
screen = pygame.display.set_mode((800,600))
run = True

clock = pygame.Clock()

while run:
    clock.tick(30)//30 FPS

    #Events First
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    #Physics Second

    #Rendering Third
    
    

pygame.quit()
#sys.exit()

