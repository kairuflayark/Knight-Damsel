import RoomRandomizer
import random

#4x4 array of rooms

emptyRoom = RoomRandomizer.emptyRoom

startRoom = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

def BDRand():
    global emptyRoom
    newRoom = []
    randomInt = random.randint(0, 10)
    print(randomInt)
    if randomInt > 4:
        newRoom = RoomRandomizer.buildRoom(4)
        #newRoom = RoomRandomizer.room
    else:
        return emptyRoom
    return newRoom

def drawPath(direction, dunRoom):
    if direction == "up":
        dunRoom[2][2] = 1
        dunRoom[2][2] = 1#EDIT THIS TO MAKE BRIDGES
        dunRoom[2][2] = 1
    if direction == "down":
        dunRoom[2][2] = 1
        dunRoom[2][2] = 1
        dunRoom[2][2] = 1
    if direction == "left":
        dunRoom[2][2] = 1
        dunRoom[2][2] = 1
        dunRoom[2][2] = 1
    if direction == "right":
        dunRoom[2][2] = 1
        dunRoom[2][2] = 1
        dunRoom[2][2] = 1


def MixDungeon():
    global startRoom
    dungeonRooms = [
        [startRoom, BDRand(), BDRand(), BDRand()],
        [BDRand(), BDRand(), BDRand(), BDRand()],
        [BDRand(), BDRand(), BDRand(), BDRand()],
        [BDRand(), BDRand(), BDRand(), BDRand()]
    ]
    return dungeonRooms
"""    traversable = False
    while(traversable == False):
        traversable = True
        paths = 4
        for rRow in range(len(dungeonRooms)):
            for rCol in range(len(dungeonRooms[rRow])):#UP
                if rCol == 0:
                    paths -= 1
                    print("bad up")
                else:
                    if rCol -1 == emptyRoom:
                        paths -= 1
                        print("bad up")
                    else:
                        drawPath("up", dungeonRooms[rRow][rCol])
                if rCol == len(dungeonRooms[rCol]):#DOWN
                    paths -= 1
                    print("bad down")
                else:
                    if rCol +1 == emptyRoom:
                        paths -= 1
                        print("bad down")
                    else:
                        drawPath("down", dungeonRooms[rRow][rCol])
                if rRow == 0:#LEFT
                    paths -= 1
                    print("bad left")
                else:
                    if rRow -1 == emptyRoom:
                        paths -= 1
                        print("bad left")
                    else:
                        drawPath("left", dungeonRooms[rRow][rCol])
                if rRow == len(dungeonRooms[rRow]):#RIGHT
                    paths -= 1
                    print("bad right")
                else:
                    if rRow +1 == emptyRoom:
                        paths -= 1
                        print("bad right")
                    else:
                        drawPath("right", dungeonRooms[rRow][rCol])
            if paths <= 0:
                print("Nontraversable map generated")
                #traversable = False
            if traversable == False:
                break
        if traversable == False:#reshuffle
            dungeonRooms = [
                [startRoom, BDRand(), BDRand(), BDRand()],
                [BDRand(), BDRand(), BDRand(), BDRand()],
                [BDRand(), BDRand(), BDRand(), BDRand()],
                [BDRand(), BDRand(), BDRand(), BDRand()]
            ]"""
    #return dungeonRooms

def BuildDungeon():
    dungeonRooms = MixDungeon()
    rooms = []

    rooms = dungeonRooms[0][0]
    tile = rooms[0][0]

    for rRow in range(len(dungeonRooms)):
        for rCol in range(len(dungeonRooms[rRow])):
            room = dungeonRooms[rRow][rCol]
            for tRow in range(len(room)):
                for tCol in range(len(room[tRow])):
                    rooms.append(room[tRow][tCol])
    return rooms

#BuildDungeon()
