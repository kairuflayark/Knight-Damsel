import pygame

listeners = {
    pygame.QUIT: [],
    pygame.KEYDOWN: [],
    pygame.KEYUP: [],
    #pygame.MOUSEMOTION
    #pygame.MOUSEBUTTONDOWN/UP
    }

def register(type, handler):
    global listeners
    if handler not in listeners[type]:
        listeners[type].append(handler)

#def unregister( change event type. IE menu vs gameplay

def update():
    for e in pygame.event.get():
        if e.type in listeners:
            for l in listeners[e.type]:
                l(e)
    
    
