import os

def mainScreen():
    os.system('cls')
    print('\n\n ----- Welcome to the telephone app -----\n\n\n')

    choice = input("  [V]iew     [A]dd      \n")

    if choice.lower() in ["v", "view", "[v]iew"]:
        viewContactsScreen()
    elif choice.lower() in ["a", "add", "[a]dd"]:
        addContactScreen()
    else:
        mainScreen()

def viewContactsScreen():
    os.system('cls')
    print('\n\n ----- Welcome to the view screen -----\n\n\n')

    choice = input("  [M]enu     [A]dd      \n")

    if choice.lower() in ["m", "menu", "[m]enu"]:
        mainScreen()
    elif choice.lower() in ["a", "add", "[a]dd"]:
        addContactScreen()
    else:
        viewContactsScreen()

def addContactScreen():
    os.system('cls')
    print('\n\n ----- Welcome to the add screen -----\n\n\n')

    choice = input("  [V]iew     [M]enu      \n")

    if choice.lower() in ["v", "view", "[v]iew"]:
        viewContactsScreen()
    elif choice.lower() in ["m", "menu", "[m]enu"]:
        mainScreen()
    else:
        addContactScreen()

mainScreen()