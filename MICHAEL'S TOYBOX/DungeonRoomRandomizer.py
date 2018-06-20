import RoomRandomizer
import random

#4x4 array of rooms

emptyRoom = RoomRandomizer.room

def BDRand():
    randomInt = random.randint(0, 10)
    print(randomInt)
    if randomInt > 4:
        RoomRandomizer.buildRoom(4)
        room = RoomRandomizer.room
    else:
        room = emptyRoom
    return room

def MixDungeon():
    dungeonRooms = [
        [BDRand(), BDRand(), BDRand(), BDRand()],
        [BDRand(), BDRand(), BDRand(), BDRand()],
        [BDRand(), BDRand(), BDRand(), BDRand()],
        [BDRand(), BDRand(), BDRand(), BDRand()]
    ]
#    traversable = False
#    while(traversable == False):
#        traversable = True
#        paths = 4
#        for rRow in range(len(dungeonRooms)):
#            for rCol in range(len(dungeonRooms[rRow])):
#                if rCol == 0:
#                    paths -= 1
#                else:
#                    if rCol -1 == emptyRoom:#UP
#                        paths -= 1
#                if rCol == len(dungeonRooms[rCol]):
#                    paths -= 1
#                else:
#                    if rCol +1 == emptyRoom:#DOWN
#                        paths -= 1
#                if rRow == 0:
#                    paths -= 1
#                else:
#                    if rRow -1 == emptyRoom:#LEFT
#                        paths -= 1
#                if rRow == len(dungeonRooms[rRow]):
#                    paths -= 1
#                else:
#                    if rRow +1 == emptyRoom:#RIGHT
#                        paths -= 1
#            if paths <= 0:
#                traversable = False
#            if traversable == False:
#                break
#        if traversable == False:#reshuffle
#            dungeonRooms = [
#                [BDRand(), BDRand(), BDRand(), BDRand()],
#                [BDRand(), BDRand(), BDRand(), BDRand()],
#                [BDRand(), BDRand(), BDRand(), BDRand()],
#                [BDRand(), BDRand(), BDRand(), BDRand()]
#            ]
    return dungeonRooms

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
