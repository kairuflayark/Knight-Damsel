import RoomRandomizer
import random,time

#4x4 array of rooms

emptyRoom = RoomRandomizer.emptyRoom

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

def BDRand():
    global emptyRoom
    newRoom = []
    randomInt = random.randint(0, 10)
    print(randomInt)
    if randomInt > 4:
        newRoom = RoomRandomizer.buildRoom(4)
        return RoomRandomizer.room
    else:
        return emptyRoom
    #return RoomRandomizer.room

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
    global dungeonRooms
    dungeonRooms = [[],[],[],[],[]]
    #minTiles = 4
    for i in range(5):
        for j in range(5):
            randomInt = random.randint(0, 10)
            if j == 2 and i == 4:
                dungeonRooms[i].append(pathRoom)   #startRoom
            else:
                if randomInt > 4:
                    dungeonRooms[i].append(pathRoom)    #standard room
                else:
                    dungeonRooms[i].append(emptyRoom)   #empty room

    #CODE FOR DRAWING PATHS
    for i in dungeonRooms:#j=lr i=ud
        for j in dungeonRooms[i]:
            #if dungeonRooms[i][j][2][2] == 0: #if there is NO room here
                #CODE HERE
            if dungeonRooms[i][j][2][2] == 1: #if there IS a room here
                #CODE HERE





                #draw connection paths
                if j != 0:
                    if dungenRooms[i][j-1][2][2] == 1:#left
                        dungeonRooms[i][j][2][0] = 1
                        dungeonRooms[i][j][2][1] = 1
                if j != 4:
                    if dungenRooms[i][j+1][2][2] == 1:#right
                        dungeonRooms[i][j][2][3] = 1
                        dungeonRooms[i][j][2][4] = 1
                if i != 0:
                    if dungenRooms[i-1][j][2][2] == 1:#up
                        dungeonRooms[i][j][0][2] = 1
                        dungeonRooms[i][j][1][2] = 1
                if i != 4:
                    if dungenRooms[i+1][j][2][2] == 1:#down
                        dungeonRooms[i][j][3][2] = 1
                        dungeonRooms[i][j][4][2] = 1
                
                

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
