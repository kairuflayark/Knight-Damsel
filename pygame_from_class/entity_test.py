import graphics_test
import pygame

class Entitiy(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sprite = None
        self.facing = None
        self.frame_num = 0
        self.frame = None

class George(Entity):
    frames = {
        "up": [(2 * 48,y * 48,48,48)
               for y in xrange(4)],#2
        "down": [(0,y * 48,48,48)
                 for y in xrange(4)],#1
        "left": [(1 * 48,y * 48,48,48)
               for y in xrange(4)],#3
        "right": [(3 * 48,y * 48,48,48)
               for y in xrange(4)],#4
        }

        
    def __init__(self):
        super(George, self).__init__()
        self.sprite = graphics.load(
            os.path.join("george.png")
            )
        self.frame = self.frames["down"][0]
        self.frame_num = 0
        self.facing = "down"

    def update(self):
        self.frame_num = (self.frame_num + 1)%4
        self.frame =  self.frames[self.facing][self.frame_num]

