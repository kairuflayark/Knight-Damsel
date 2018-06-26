#import RoomRandomizer
import random,time

#4x4 array of rooms

emptyRoom = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

stdRoom = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

startRoom = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0]
]

pathRoom = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0]
]

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
    dungeonRooms = [[],[],[],[],[]]
    #minTiles = 4
    for i in range(5):
        for j in range(5):
            randomInt = random.randint(0, 10)
            if j == 2 and i == 4:
                dungeonRooms[i].append(stdRoom)   #startRoom
            else:
                if randomInt > 4:
                    dungeonRooms[i].append(stdRoom)    #standard room
                else:
                    dungeonRooms[i].append(emptyRoom)   #empty room

#    return dungeonRooms


    #CODE FOR DRAWING PATHS
    for i in range(len(dungeonRooms)):#j=lr i=ud
        for j in range(len(dungeonRooms[i])):
            pyRoom = stdRoom
            if dungeonRooms[i][j][2][2] == 1: #if there IS a room here
                connections = 0
                if (i - 1) >= 0: #up
                    if dungeonRooms[i-1][j][2][2] == 1:
                        pyRoom[0][2] = 1
                        pyRoom[1][2] = 1
                        connections += 1
                if (i + 1) <= 4: #down
                    if dungeonRooms[i+1][j][2][2] == 1:
                        pyRoom[3][2] = 1
                        pyRoom[4][2] = 1
                        connections += 1
                if (j - 1) >= 0: #left
                    if dungeonRooms[i][j-1][2][2] == 1:
                        pyRoom[2][0] = 1
                        pyRoom[2][1] = 1
                        connections += 1
                if (j + 1) <= 4: #right
                    if dungeonRooms[i][j+1][2][2] == 1:
                        pyRoom[2][3] = 1
                        pyRoom[2][4] = 1
                        connections += 1
                if connections < 1:
                    dungeonRooms[i][j] = emptyRoom
                if connections > 1:
                    dungeonRooms[i][j] = pyRoom

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
