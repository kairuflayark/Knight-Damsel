import pygame

import michael
import Events
import Map
import Entities

tileMap = []



resolution = None
screen = None
sprites = []
background = None
images = {}

def init(res):
    global resolution, screen
    resolution = res
    screen = pygame.display.set_mode(res)
    


#for spritesheet
def add(sprite):
    global sprites
    if sprite not in sprites:
        sprites.append(sprite)

def remove(sprite):
    global sprites
    if sprite in sprites:
        sprites.remove(sprite)
        
        
def render(Plot):
    global screen, background
    screen.fill((255,255,255))#black
    #screen.blit(background, (0,0))#load backgroud
    
    #for tile in tileMap:#load map first
    #    screen.blit(tile.sprite, (tile.x, tile.y), tile.frame)

    #for row in range(Map.MAPHEIGHT):
    #    for column in range(Map.MAPWIDTH):
    #        screen.blit(Map.tiles[Map.tilemap[row][column]], (column * Map.TILESIZE, row * Map.TILESIZE))
    Map.displayMap(Plot.currentRoom(), screen)
    displaySprite(Plot.currentRoom())

    for entitiy in sprites:#load entities
        screen.blit(entitiy.sprite, ((entitiy.x, entitiy.y)), entitiy.frame)


    #IF textbox load textbox
    michael.drawTextBox(screen)
    michael.drawText(Plot.currentText(), screen)
        #if textbox:
            #print("There is a text box!")
    Entities.displayArrow(screen, Plot.currentState, Plot.decision)

    pygame.display.flip()#print to screen
    
def load(path):
    global images
    if path not in images:
        images[path] = pygame.image.load(path)
    return images[path]

def displaySprite(mapNum):
    player = Entities.Player()
    king = Entities.King()
    vizzi = Entities.Vizzi()
    charles = Entities.Charles()
    dragon = Entities.Dragon()
    wizard = Entities.Wizard()
    villain = Entities.Villain()
    print(sprites)
    if mapNum == 0:
        player.x = (40 * 4)
        player.y = (40 * 2) - 15
        remove(player)
        add(player)  # //player sprite
        king.x = (40 * 9)
        king.y = (40 * 2) - 15
        remove(king)
        add(king)
    elif mapNum == 1:
        #remove(king) #// Can't seem to get this function to work
        king.y += 1000 #// Moving them off-screen instead of removing them
        vizzi.x = (40 * 9)
        vizzi.y = (40 * 2) - 15
        remove(vizzi)
        add(vizzi)
    elif mapNum == 2:
        #remove(vizzi)
        vizzi.y += 1000
        charles.x = (40 * 9)
        charles.y = (40 * 2) - 15
        remove(charles)
        add(charles)
    elif mapNum == 3:
        #remove(charles)
        charles.y += 1000
        dragon.x = (40 * 9)
        dragon.y = (40 * 2) - 15
        remove(dragon)
        add(dragon)
    elif mapNum == 4:
        #remove(dragon)
        dragon.y += 1000
        wizard.x = (40 * 9)
        wizard.y = (40 * 2) - 15
        remove(wizard)
        add(wizard)
    elif mapNum == 5:
        #remove(wizard)
        wizard.y += 1000
        villain.x = (40 * 9)
        villain.y = (40 * 2) - 15
        remove(villain)
        add(villain)
    elif mapNum >= 6:
        #remove(wizard)
        wizard.y += 1000
        villain.x = (40 * 9)
        villain.y = (40 * 2) - 15
        remove(villain)
        add(villain)