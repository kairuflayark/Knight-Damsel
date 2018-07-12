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
