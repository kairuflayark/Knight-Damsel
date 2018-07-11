# import pygame




class Plot(object):
    def __init__(self):
        self.Event = 0
        # king 1 = talked to king
        # King 2 = left note
        # king 3 = Headed right off
        self.king = None
        self.vizzi = None
        self.charles = None
        self.door = None
        self.dragon = None
        self.wizard = None
        self.villain = None
        self.charlesBoss = False
        self.kingBoss = False
        self.hasVizzi = False
        self.princess = None
        self.isAlive = True

    def updateplot(self, event, value):
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
            self.door = value
        elif event == 4 and self.door == 0:
            if value == 2:
                if self.hasVizzi:
                    self.dragon = 3
                else:
                    self.isAlive = False
                    self.dragon = value
            else:
                self.dragon = value
        elif event == 4 and self.door == 1:
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



        # def key_handler(self, e):
        #     if e.type == pygame.KEYDOWN:
        #         if e.key == pygame.K_KP_ENTER:






