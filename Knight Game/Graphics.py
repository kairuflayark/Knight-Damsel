import pygame

#import Map
tiles = []#tiles = Map.tiles



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
        
        
def render():
    global screen, background
    screen.fill((0,0,0))#black
    screen.blit(background, (0,0))#load backgroud
    
    for tile in tileMap:#load map first
        screen.blit(tile.sprite, (tile.x, tile.y), tile.frame)
        
    for sprite in sprites:#load entities
        screen.blit(sprite.sprite, (sprite.x, sprite.y), sprite.frame)

    pygame.display.flip()#print to screen
    
def load(path):
    global images
    if path not in images:
        images[path] = pygame.image.load(path)
    return images[path]
        
