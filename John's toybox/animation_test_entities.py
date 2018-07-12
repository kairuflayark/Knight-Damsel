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
        
