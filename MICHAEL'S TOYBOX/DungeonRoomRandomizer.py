import RoomRandomizer
import random

#4x4 array of rooms

emptyRoom = RoomRandomizer.emptyRoom

def BDRand():
    global emptyRoom
    randomInt = random.randint(0, 10)
    print(randomInt)
    if randomInt > 4:
        RoomRandomizer.buildRoom(4)
        newRoom = RoomRandomizer.room
    else:
        newRoom = emptyRoom
    return newRoom

def drawPath(direction, dunRoom):
    if direction == "up":
        dunRoom[2][2] = 1
        dunRoom[2][1] = 1#EDIT THIS TO MAKE BRIDGES
        dunRoom[2][0] = 1
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
    dungeonRooms = [
        [BDRand(), BDRand(), BDRand(), BDRand()],
        [BDRand(), BDRand(), BDRand(), BDRand()],
        [BDRand(), BDRand(), BDRand(), BDRand()],
        [BDRand(), BDRand(), BDRand(), BDRand()]
    ]
    traversable = False
    while(traversable == False):
        traversable = True
        paths = 4
        for rRow in range(len(dungeonRooms)):
            for rCol in range(len(dungeonRooms[rRow])):
                if rCol == 0:
                    paths -= 1
                else:
                    if rCol -1 == emptyRoom:#UP
                        paths -= 1
                    else:
                        drawPath("up", dungeonRooms[rRow][rCol])
                if rCol == len(dungeonRooms[rCol]):
                    paths -= 1
                else:
                    if rCol +1 == emptyRoom:#DOWN
                        paths -= 1
                    else:
                        drawPath("down", dungeonRooms[rRow][rCol])
                if rRow == 0:
                    paths -= 1
                else:
                    if rRow -1 == emptyRoom:#LEFT
                        paths -= 1
                    else:
                        drawPath("left", dungeonRooms[rRow][rCol])
                if rRow == len(dungeonRooms[rRow]):
                    paths -= 1
                else:
                    if rRow +1 == emptyRoom:#RIGHT
                        paths -= 1
                    else:
                        drawPath("right", dungeonRooms[rRow][rCol])
            if paths <= 0:
                print("Nontraversable map generated")
                traversable = False
            if traversable == False:
                break
        if traversable == False:#reshuffle
            dungeonRooms = [
                [BDRand(), BDRand(), BDRand(), BDRand()],
                [BDRand(), BDRand(), BDRand(), BDRand()],
                [BDRand(), BDRand(), BDRand(), BDRand()],
                [BDRand(), BDRand(), BDRand(), BDRand()]
            ]
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
