from typing import List


class Text(object):
    def __init__(self):
        self.num_choice = None
        self.intro = None
        self.decision = None
        self.result = None

    def getIntro(self):
        return self.intro[0]


class King_text(Text):

    intro: List[str]

    def __init__(self):
        super().__init__()
        self.num_choice = 3
        self.intro = ["What should I do now?"]
        self.decision = ["Tell the King",
                         "Leave a note",
                         "Leave immediately"]
        self.result = [["He sends you off with his trust"],
                       ["With the note written you leave"],
                       ["Saddling your horse you leave"]]
    def getIntro(self):
        return self.intro[0]

    def getDecision(self):
        return self.decision

    def getResult(self, value):
        return self.result[value]

class Vizzi_text(Text):
    def __init__(self):
        super().__init__()
        self.num_choice = 3
        self.intro = [ ["On the way you encounter Vizzi who was"],
                       ["running late to kidnap Christine"] ]
        self.decision = ["Kill him",
                         "Let him leave",
                         "Leave immediately"]
        self.result = [["He dies a pitiful death"],
                       ["He hurries away to drink away his shame"],
                       ["For the money you paid him, he agrees to come"]]

class Charles_text(Text):
    def __init__(self):
        super().__init__()
        self.num_choice = 3
        self.intro = ["As you are considering whether or not to take the",
                      "left door or the right one of your fellow knights arrives"]
        self.decision = ["Stab him in the back",
                         "Try and convince him to leave",
                         "Make it into a competition"]
        self.result = [["He falls and his body lies resting on the floor"],
                       ["With a mighty clash of swords he collapses bloodied and exhausted"],
                       ["He agrees and tells you to choose which door to go through"]]

class Dragon_text():
    def __init__(self):
        self.num_choice = 2
        self.intro = [ "Standing beyond the door is a Battle scared warrior woman" ]
        self.decision = ["Talk it out",
                         "Fight",
                         "Flirt"]
        self.result = [["Moved by your plea she allows you to pass"],
                       ["The Dragoness roasts you"],
                       ["She ignores your actions and you die a bloody death"],
                       ["Vizzi begins to flirt with her and you escape past her"]]

class Wizard_Text(Text):
    def __init__(self):
        super().__init__()
        self.num_choice = 2
        self.intro = [ "The Room is Gloomy and a powerful mage leans over a cauldron" ]
        self.decision = ["Bluff your way past",
                         "Kick him into the Cauldron",
                         "Fight"]
        self.result = [[""],
                       ["You hurry down the Corridor"]]

class Villian_Text(Text):
    def __init__(self):
        super().__init__()
        self.num_choice = 2
        self.intro = [ "Finally you have reached the dastardly villain",
                       "beyond the door you can see the cell he",
                        "is holding the Princess in." ]
        self.decision = ["Fight",
                         "Fight",
                         "and Fight"]
        self.result = [["The Other knight bursts through the door angry that his plans", " to kidnap the Princess were foiled"],
                       ["The King enters through the door having found out", "that you had arranged to have his daughter kidnapped."]]

class Princess_King_text(Text):
    def __init__(self):
        super().__init__()
        self.num_choice = 2
        self.intro = [ "After a long battle the king falls to his knees exhausted" ]
        self.decision = ["Explain your actions",
                         "Kill him!"]
        self.result = [["Good End"],
                       ["You hurry down the Corridor"]]

class Princess_Charles_text(Text):
    def __init__(self):
        super().__init__()
        self.num_choice = 2
        self.intro = [ "The " ]
        self.decision = ["Bluff your way past",
                         "Kick him into the Cauldron",
                         "Fight"]
        self.result = [[""],
                       ["You hurry down the Corridor"]]

class Princess_King_and_Charles_text(Text):
    def __init__(self):
        super().__init__()
        self.num_choice = 2
        self.intro = [ "The " ]
        self.decision = ["Bluff your way past",
                         "Kick him into the Cauldron",
                         "Fight"]
        self.result = [[""],
                       ["You hurry down the Corridor"]]

def getText(event, part, decision):
    text = None
    if event == 0:
        if part == 0:
            text = King_text.getIntro(King_text())
        elif part == 1:
            text = King_text.getDecision(King_text())
        else:
            text = King_text.getResult(King_text(), decision)

    return text