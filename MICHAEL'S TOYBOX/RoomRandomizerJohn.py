import random

intRoom = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

emptyRoom = [
    ['X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X']
]

def buildRoom(minTiles):
    tilect = 0
    if minTiles > 9: minTiles = 9
    if minTiles < 4: minTiles = 4

    while tilect <= minTiles:
        tilect = 0
        #randomizes only the middle tiles
        for r in range(len(intRoom)):
            for c in range(len(intRoom[r])):
                if (r != 0 and r != len(intRoom) - 1) and (c != 0 and c != len(intRoom[r]) - 1):
                    room[r][c] = random.randint(0, 1)
                else:
                    room[r][c] = 0

        #blanks out disconnected tiles
        for r in range(len(room)):
            for c in range(len(room[r])):
                connections = 0
                if (r != 0 and r != len(room) - 1) and (c != 0 and c != len(room[c]) - 1):
                    if room[r][c] == 1:
                        if room[r - 1][c] == 0 and room[r][c - 1] == 0 and room[r + 1][c] == 0 and room[r][c + 1] == 0:
                            room[r][c] = 0

        #always activates center tile
        room[2][2] = 1

        #counts active tiles
        for r in range(len(room)):
            for c in range(len(room[r])):
                if room[r][c] == 1:
                    tilect += 1
    return room

def ConvertedBuildRoom():
    intRoomTC = buildRoom(4)
    charRoom = emptyRoom

    for r in range(len(intRoomTC)):
        for c in range(len(intRoomTC)):
            if intRoomTC[r][c] == 0:
                charRoom[r][c] = 'X'
            else:
                charRoom[r][c] = 'O'
    return charRoom


    
    
