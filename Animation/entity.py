import os

import pygame

import graphics


class Entity(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sprite = None


# Change Sprites to combat
class Vizzi(Entity):
    frames = {

        # neutral
        "start": [(0, 4, 69, 51)],
        "one": [(77, 4, 69, 51)],
        "two": [(166, 4, 69, 51)],
        "three": [(262, 4, 69, 51)],
        "four": [(357, 4, 69, 51)]

    }

    def __init__(self):
        super(Vizzi, self).__init__()
        self.sprite = graphics.load(
            os.path.join("Animation V.png")
        )
        self.frame = self.frames["start"][0]
        self.attack = False
        self.aFrame = 0
        # self.frame_num = 0
        # self.facing = "down"
        # self.speed = 0.5
        # self.velocity = [0, 0]

    # Change
    def update(self):
        if self.attack:

            if self.aFrame == 0:
                pygame.mixer.init()
                coin = pygame.mixer.Sound("Thwack.wav")
                coin.play()
                self.frame = self.frames["one"][0]
                self.aFrame = 1
            elif self.aFrame == 1:
                self.frame = self.frames["two"][0]
                self.aFrame = 2
            elif self.aFrame == 2:
                self.frame = self.frames["three"][0]
                self.aFrame = 3
            elif self.aFrame == 3:
                self.frame = self.frames["four"][0]
                self.aFrame = 4
            elif self.aFrame == 4:
                self.frame = self.frames["start"][0]
                self.aFrame = 0
                self.attack = False
        # self.x += self.velocity[0]
        # self.y += self.velocity[1]
        # self.frame_num = (self.frame_num + self.speed * 0.25) % 4
        # self.frame = self.frames[self.facing][int(self.frame_num)]

    # change
    def key_handler(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a:
                self.attack = True

        #         self.velocity[1] -= self.speed
        #         self.facing = "up"
        #     elif (e.key == pygame.K_DOWN):
        #         self.velocity[1] += self.speed
        #         self.facing = "down"
        #     elif (e.key == pygame.K_LEFT):
        #         self.velocity[0] -= self.speed
        #         self.facing = "left"
        #     elif (e.key == pygame.K_RIGHT):
        #         self.velocity[0] += self.speed
        #         self.facing = "right"
        # elif (e.type == pygame.KEYUP):
        #     if (e.key == pygame.K_UP):
        #         self.velocity[1] += self.speed
        #     elif (e.key == pygame.K_DOWN):
        #         self.velocity[1] -= self.speed
        #     elif (e.key == pygame.K_LEFT):
        #         self.velocity[0] += self.speed
        #     elif (e.key == pygame.K_RIGHT):
        #         self.velocity[0] -= self.speed
