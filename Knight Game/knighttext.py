class Text(object):
    def __init__(self):
        self.num_choice = None
        self.intro = None
        self.decision = None
        self.result = None


class King_text(Text):
    def __init__(self):
        self.num_choice = 3
        self.intro = [["What should I do now?"]]
        self.decision = [["Tell the King"],
                         ["Leave a note"],
                         ["Leave immediately"]]
        self.result = ["He sends you off with his trust",
                       "With the note written you leave",
                       "Saddling your horse you leave"]

class Vizzi_text(Text):
    def __init__(self):
        self.num_choice = 3
        self.intro = [ ["On the way you encounter Vizzi who was"],
                       ["running late to kidnap Christine"] ]
        self.decision = ["Kill him",
                         "Let him leave",
                         "Leave immediately"]
        self.result = ["He dies a pitiful death",
                       "He hurries away to drink away his shame",
                       "For the money you paid him, he agrees to come"]

class Charles_text(Text):
    def __init__(self):
        self.num_choice = 3
        self.intro = ["As you are considering whether or not to take the",
                      "left door or the right one of your fellow knights arrives"]
        self.decision = ["Stab him in the back",
                         "Try and convince him to leave",
                         "Make it into a competition"]
        self.result = ["He falls and his body lies resting on the floor",
                       "With a mighty clash of swords he collapses bloodied and exhausted",
                       "He agrees and tells you to choose which door to go through"]

class Door_text():
    def __init__(self):
        self.num_choice = 2
        self.intro = [ "Left or straight?" ]
        self.decision = ["Left",
                         "Straight",]
        self.result = [["You go through the left door"],
                       ["You hurry down the Corridor"]]