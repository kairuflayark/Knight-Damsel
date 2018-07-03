#animation_test_entities
import pygame
import os
import animation_test_graphics
#import animation_test_audio

class Entity(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sprite = None
        self.facing = None
        self.frame_num = 0
        self.frame = None
"""
class Character(Entity):
    frames = {
        #"up": [(2 * 48,y * 48,48,48)
        #       for y in xrange(4)],#2
        #"down": [(0,y * 48,48,48)
        #         for y in xrange(4)],#1
        #"left": [(1 * 48,y * 48,48,48)
        #       for y in xrange(4)],#3
        #"right": [(3 * 48,y * 48,48,48)
        #       for y in xrange(4)],#4
        }

        
    def __init__(self):
        super(George, self).__init__()
        self.sprite = graphics.load(
            os.path.join("george.png")
            )
        self.frame = self.frames["down"][0]
        self.frame_num = 0
        self.facing = "down"
        self.speed = 0.5
        self.velocity = [0,0]

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.frame_num = (self.frame_num + self.speed * .25)%4
        self.frame =  self.frames[self.facing][self.frame_num]

    def key_handler(self, e):
        if (e.type == pygame.KEYDOWN):
            if (e.key == pygame.K_UP):
                self.velocity[1] -= self.speed
                self.facing = "up"
            elif (e.key == pygame.K_DOWN):
                self.velocity[1] += self.speed
                self.facing = "down"
            elif (e.key == pygame.K_LEFT):
                self.velocity[0] -= self.speed
                self.facing = "left"
            elif (e.key == pygame.K_RIGHT):
                self.velocity[0] += self.speed
                self.facing = "right"
            
        elif (e.type == pygame.KEYUP):
            if (e.key == pygame.K_UP):
                self.velocity[1] += self.speed               
            elif (e.key == pygame.K_DOWN):
                self.velocity[1] -= self.speed     
            elif (e.key == pygame.K_LEFT):
                self.velocity[0] += self.speed 
            elif (e.key == pygame.K_RIGHT):
                self.velocity[0] -= self.speed

"""
class Coin(Entity):
    frames = [
        (0,0,50,50),
        (50,0,50,50),
        (100,0,50,50),
        (150,0,50,50)
        ]
    count = 0

        
    def __init__(self):
        super(Coin, self).__init__()
        self.sprite = animation_test_graphics.load(
            os.path.join("22-color.png")
            )
        self.frame = self.frames[0]
        self.frame_num = 0
        self.speed = 0.5
        self.facing = None
        self.x = 0
        self.y = 0
        self.frameUp = True

    def update(self):
        self.count += 1
        if (self.count % 7 == 0):
            if (self.frameUp):
                if (self.frame_num == 0):
                    self.frame_num = 1
                elif (self.frame_num == 1):
                    self.frame_num = 2
                elif (self.frame_num == 2):
                    self.frame_num = 3
                    self.frameUp = False
            else:
                if (self.frame_num == 3):
                    self.frame_num = 2
                elif (self.frame_num == 2):
                    self.frame_num = 1
                elif (self.frame_num == 1):
                    self.frame_num = 0
                    self.frameUp = True

        self.frame = self.frames[self.frame_num]
        
