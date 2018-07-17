import os
import pygame
import Graphics

class Entitiy(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sprite = None
        self.facing = None
        self.frame_num = 0
        self.frame = None



class Player(Entitiy):#the player
    frames = {
        "up": [(3 * 32,y * 48,32,48)
               for y in range(4)],  #row 4
        "down": [(0,y * 48,32,48)
               for y in range(4)],  #row 1
        "left": [(1 * 32,y * 48,32,48)
               for y in range(4)],  #row 2
        "right": [(2 * 32,y * 48,32,48)
               for y in range(4)],  #row 3
        }

    def __init__(self):
        super(Player, self).__init__()
        self.sprite = Graphics.load(
            os.path.join("Assets/nobbynobbs.png")
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

    """def key_handler(self, e):
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
        

class King(Entitiy):#the king
    frames = {
        "up": [(3 * 32,y * 48,32,48)
               for y in range(4)],  #row 4
        "down": [(0,y * 48,32,48)
               for y in range(4)],  #row 1
        "left": [(1 * 32,y * 48,32,48)
               for y in range(4)],  #row 2
        "right": [(2 * 32,y * 48,32,48)
               for y in range(4)],  #row 3
        }

    def __init__(self):
        super(King, self).__init__()
        self.sprite = Graphics.load(
            os.path.join("Assets/king.png")
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

class Vizzi(Entitiy):#the fake villan
    frames = {
        "up": [(3 * 32,y * 48,32,48)
               for y in range(4)],  #row 4
        "down": [(0,y * 48,32,48)
               for y in range(4)],  #row 1
        "left": [(1 * 32,y * 48,32,48)
               for y in range(4)],  #row 2
        "right": [(2 * 32,y * 48,32,48)
               for y in range(4)],  #row 3
        }

    def __init__(self):
        super(Vizzi, self).__init__()
        self.sprite = Graphics.load(
            os.path.join("Assets/Vizzi.png")
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

class Charles(Entitiy):#the other knight
    frames = {
        "up": [(3 * 32,y * 48,32,48)
               for y in range(4)],  #row 4
        "down": [(0,y * 48,32,48)
               for y in range(4)],  #row 1
        "left": [(1 * 32,y * 48,32,48)
               for y in range(4)],  #row 2
        "right": [(2 * 32,y * 48,32,48)
               for y in range(4)],  #row 3
        }

    def __init__(self):
        super(Charles, self).__init__()
        self.sprite = Graphics.load(
            os.path.join("Assets/charles.png")
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

class Princess(Entitiy):#Princess
    frames = {
        "up": [(3 * 32,y * 48,32,48)
               for y in range(4)],  #row 4
        "down": [(0,y * 48,32,48)
               for y in range(4)],  #row 1
        "left": [(1 * 32,y * 48,32,48)
               for y in range(4)],  #row 2
        "right": [(2 * 32,y * 48,32,48)
               for y in range(4)],  #row 3
        }

    def __init__(self):
        super(Princess, self).__init__()
        self.sprite = Graphics.load(
            os.path.join("Assets/princess.png")
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

class Dragon(Entitiy):#female villan
    frames = {
        "up": [(3 * 32,y * 48,32,48)
               for y in range(4)],  #row 4
        "down": [(0,y * 48,32,48)
               for y in range(4)],  #row 1
        "left": [(1 * 32,y * 48,32,48)
               for y in range(4)],  #row 2
        "right": [(2 * 32,y * 48,32,48)
               for y in range(4)],  #row 3
        }


    def __init__(self):
        super(Dragon, self).__init__()
        self.sprite = Graphics.load(
            os.path.join("Assets/dragon.png")
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
    

    
class Wizard(Entitiy):#wizard?
    frames = {
        "up": [(3 * 32,y * 48,32,48)
               for y in range(4)],  #row 4
        "down": [(0,y * 48,32,48)
               for y in range(4)],  #row 1
        "left": [(1 * 32,y * 48,32,48)
               for y in range(4)],  #row 2
        "right": [(2 * 32,y * 48,32,48)
               for y in range(4)],  #row 3
        }

    def __init__(self):
        super(Wizard, self).__init__()
        self.sprite = Graphics.load(
            os.path.join("Assets/wizard.png")
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

class Villain(Entitiy):#Villain
    frames = {
        "up": [(3 * 32, y * 48, 32, 48)
               for y in range(4)],  # row 4
        "down": [(0, y * 48, 32, 48)
                 for y in range(4)],  # row 1
        "left": [(1 * 32, y * 48, 32, 48)
                 for y in range(4)],  # row 2
        "right": [(2 * 32, y * 48, 32, 48)
                  for y in range(4)],  # row 3
    }

    def __init__(self):
        super(Villain, self).__init__()
        self.sprite = Graphics.load(
            os.path.join("Assets/devil.png")
        )
        self.frame = self.frames["down"][0]
        self.frame_num = 0
        self.facing = "down"
        self.speed = 0.5
        self.velocity = [0, 0]

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.frame_num = (self.frame_num + self.speed * .25) % 4
        self.frame = self.frames[self.facing][self.frame_num]



class displayArrow():
    def __init__(self, screen, visible, decision):
        self.sprite = Graphics.load(
            os.path.join("Assets/pointer.png")
        )
        self.frame = None
        self.screen = screen
        if decision == 0:
            frame = [8, 197]
        elif decision == 1:
            frame = [2, 212]
        elif decision == 2:
            frame = [2, 228]
        if visible == 1:
            self.screen.blit(self.sprite, (frame[0], frame[1]))




