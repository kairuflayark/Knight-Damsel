from typing import List


class Text(object):
    def __init__(self):
        self.num_choice = None
        self.intro = None
        self.decision = None
        self.result = None

    def getIntro(self):
        return self.intro


class King_text(Text):

    intro: List[str]

    def __init__(self):
        super().__init__()
        self.num_choice = 3
        self.intro = [["What should I do now?"]]
        self.decision = [["Tell the King"],
                         ["Leave a note"],
                         ["Leave immediately"]]
        self.result = [[["He sends you off with his trust"]],
                       [["With the note written you leave"]],
                       [["Saddling your horse you leave"]]]
    def getIntro(self):
        return self.intro

    def getDecision(self):
        return self.decision

    def getResult(self, value):
        return self.result[value]

class Vizzi_text(Text):
    def __init__(self):
        super().__init__()
        self.num_choice = 3
        self.intro = [ ["On the way you encounter Vizzi who was"],
                       ["running late to kidnap the princess for you"] ]
        self.decision = [["Kill him"],
                         ["Let him leave"],
                         ["Leave immediately"]]
        self.result = [[["He dies a pitiful death"]],
                       [["He hurries away to drink away his shame"]],
                       [["For the money you paid him, he agrees to come"]]]

    def getIntro(self):
        return self.intro

    def getDecision(self):
        return self.decision

    def getResult(self, value):
        return self.result[value]

class Charles_text(Text):
    def __init__(self):
        super().__init__()
        self.num_choice = 3
        self.intro = [["As you are considering whether or not to take the"],
                      ["left door or the right one of your fellow knights arrives"]]
        self.decision = [["Stab him in the back"],
                         ["Try and convince him to leave"],
                         ["Make it into a competition"]]
        self.result = [[["He falls and his body lies resting on the floor"]],
                       [["With a mighty clash of swords he collapses bloodied and exhausted"]],
                       [["He agrees and tells you to choose which door to go through"]]]

    def getIntro(self):
        return self.intro

    def getDecision(self):
        return self.decision

    def getResult(self, value):
        return self.result[value]


class Dragon_text():
    def __init__(self):
        self.num_choice = 2
        self.intro = [ ["Standing beyond the door is a Battle scared warrior woman"] ]
        self.decision = [["Talk it out"],
                         ["Fight"],
                         ["Flirt"]]
        self.result = [[["Moved by your plea she allows you to pass"]],
                       [["The Dragoness roasts you"]],
                       [["She ignores your actions and you die a bloody death"]],
                       [["Vizzi begins to flirt with her and you escape past her"]]]

    def getIntro(self):
        return self.intro

    def getDecision(self):
        return self.decision

    def getResult(self, value):
        return self.result[value]

class Wizard_Text(Text):
    def __init__(self):
        super().__init__()
        self.num_choice = 2
        self.intro = [ ["The Room is Gloomy and a powerful mage leans over a cauldron"] ]
        self.decision = [["Bluff your way past"],
                         ["Kick him into the Cauldron"],
                         ["Fight"]]
        self.result = [[["You fail the check and get fried by lightning"]],
                       [["Caught by surprise he topples into the cauldron"]],
                       [["After a short battle you continue onwards"]]]

    def getIntro(self):
        return self.intro

    def getDecision(self):
        return self.decision

    def getResult(self, value):
        return self.result[value]

class Villian_Text(Text):
    def __init__(self):
        super().__init__()
        self.num_choice = 2
        self.intro = [ ["Finally you have reached the dastardly villain"],
                       ["beyond the door you can see the cell he"],
                        ["is holding the Princess in."]]
        self.decision = [["Fight"],
                         ["Fight"],
                         ["and Fight"]]
        self.result = [[["The Other knight bursts through the door angry that his plans", " to kidnap the Princess were foiled"]],
                       [["The King enters through the door having found out", "that you had arranged to have his daughter kidnapped."]],
                       [["The King and Charles Burst through the door in agreement that you need to die"]]]

    def getIntro(self):
        return self.intro

    def getDecision(self):
        return self.decision

    def getResult(self, value):
        return self.result[value]


class Princess_text(Text):
    def __init__(self):
        super().__init__()
        self.num_choice = 2
        self.intro = [[["After a long battle Charles' sword clatters to the ground."]],
                      [["After a long battle the king falls to his knees exhausted"]],
                      [["after a long battle they both fall"]]]
        self.decision = [[["Finish him"], ["Spare his life."]],
                            [["Explain your actions"],["Kill him!"]

                          ]]
        self.result = [[[" "]],
                       [["victor"]]]

    def getIntro(self):
        return self.intro[0]

    def getDecision(self):
        return self.decision[0]

    def getResult(self, value):
        return self.result[value]


def getText(event, part, decision):
    text = None
    if event == 0:
        if part == 0:
            text = King_text.getIntro(King_text())
        elif part == 1:
            text = King_text.getDecision(King_text())
        else:
            text = King_text.getResult(King_text(), decision)
    if event == 1:
        if part == 0:
            text = Vizzi_text.getIntro(Vizzi_text())
        elif part == 1:
            text = Vizzi_text.getDecision(Vizzi_text())
        else:
            text = Vizzi_text.getResult(Vizzi_text(), decision)
    if event == 2:
        if part == 0:
            text = Charles_text.getIntro(Charles_text())
        elif part == 1:
            text = Charles_text.getDecision(Charles_text())
        else:
            text = Charles_text.getResult(Charles_text(), decision)
    if event == 3:
        if part == 0:
            text = Dragon_text.getIntro(Dragon_text())
        elif part == 1:
            text = Dragon_text.getDecision(Dragon_text())
        else:
            text = Dragon_text.getResult(Dragon_text(), decision)
    if event == 4:
        if part == 0:
            text = Wizard_Text.getIntro(Wizard_Text())
        elif part == 1:
            text = Wizard_Text.getDecision(Wizard_Text())
        else:
            text = Wizard_Text.getResult(Wizard_Text(), decision)
    if event == 5:
        if part == 0:
            text = Villian_Text.getIntro(Villian_Text())
        elif part == 1:
            text = Villian_Text.getDecision(Villian_Text())
        else:
            text = Villian_Text.getResult(Villian_Text(), decision)
    if event == 6:
        if part == 0:
            text = Princess_text.getIntro(Princess_text())
        elif part == 1:
            text = Princess_text.getDecision(Princess_text())
        else:
            text = Princess_text.getResult(Princess_text(), decision)
    return text