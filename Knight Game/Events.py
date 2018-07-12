import pygame
import text
import Map

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
    

class Plot(object):
    def __init__(self):
        # king 1 = talked to king
        # King 2 = left note
        # king 3 = Headed right off
        self.king = None
        self.vizzi = None
        self.charles = None
        self.dragon = None
        self.wizard = None
        self.villain = None
        self.charlesBoss = False
        self.kingBoss = False
        self.hasVizzi = False
        self.princess = None
        self.isAlive = True

        self.currentEvent = 0
        self.currentState = 0
        self.decision = 0


    def updateDecision(self, event, value):
        if (self.king == 2 and self.vizzi == 2) or (self.king == 1 and (self.charles != 3)):
            self.kingBoss = True
        if self.charles != 1:
            self.charlesBoss = True
        if event == 0:
            self.king = value
        elif event == 1:
            self.vizzi = value
            if value == 2:
                self.hasVizzi = True
        elif event == 2:
            self.charles = value
        elif event == 3:
            if value == 2:
                if self.hasVizzi:
                    self.dragon = 3
                else:
                    self.isAlive = False
                    self.dragon = value
            else:
                self.dragon = value
        elif event == 4:
            self.wizard = value
            if value == 1:
                self.isAlive = False
        elif event == 5:
            if self.charlesBoss and self.kingBoss:
                self.villain = 2
            elif self.charlesBoss:
                self.villain = 0
            elif self.kingBoss:
                self.villain = 1
        elif event == 6:
            self.princess = value
            if self.kingBoss and value == 2:
                self.isAlive = False

    def currentText(self):
        return text.getText(self.currentEvent, self.currentState, self.getDecision())

    def currentRoom(self):
        return self.currentEvent

    def currentState(self):
        return self.currentState

    def getDecision(self):
        if self.currentEvent == 0:
            return self.king
        if self.currentEvent == 1:
            return self.vizzi
        if self.currentEvent == 2:
            return self.charles
        if self.currentEvent == 3:
            return self.dragon
        if self.currentEvent == 4:
            return self.wizard
        if self.currentEvent == 5:
            return self.villain
        if self.currentEvent == 6:
            return self.princess


    def key_handler(self, e):
        print(self.currentState)
        if e.type == pygame.KEYDOWN:
            print("down")
            if e.key == pygame.K_RETURN:
                print('enter')
                if self.currentState == 0:
                    print('state ')
                    self.currentState = 1
                    print(self.currentState)
            if self.currentState == 1:
                if e.key == pygame.K_DOWN and self.decision < len(self.currentText()):
                    self.decision += 1
                elif e.key == pygame.K_UP and self.decision > 0:
                    self.decision -= 1

        print(self.currentText())


