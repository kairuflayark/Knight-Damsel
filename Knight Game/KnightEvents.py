import pygame



class Plot(object):
    def __init__(self):
        # king 1 = talked to king
        # King 2 = left note
        # king 3 = Headed right off
        self.king = 0
        self.vizzi = 0
        self.charles = 0
        self.door = 0
        self.dragon = 0
        self.wizard = 0
        self.villain = 0
        self.charlesBoss = False
        self.kingBoss = False
        self.hasVizzi = False
        self.princess = 0

    def update_king(self, value):
        self.king = value

    def update_vizzi(self, value):
        self.vizzi = value
        if value == 3:
            self.hasVizzi = True

    def update_charles(self, value):
        self.charles = value

    def update_door(self, value):
        self.door = value

    def update_dragon(self, value):
        if value == 1 and self.hasVizzi == True:
            self.dragon = 4
        else:
            self.dragon = value

    def update_wizard(self, value):
        self.wizard = value

    def update_villain(self, value):
        self.villain = value


    def update_final_boss(self):
        if (self.king == 2 and self.vizzi == 2) or (self.king == 1 and (self.charles != 3)):
            self.kingBoss = True
        if self.charles != 1:
            self.charlesBoss = True

    def update_final_boss_end(self, value):

