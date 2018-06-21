import random

room = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

emptyRoom = [#So we always have this to reference
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

def buildRoom(minTiles):
    tilect = 0
    if minTiles > 9: minTiles = 9
    if minTiles < 4: minTiles = 4

    while tilect <= minTiles:
        tilect = 0
        #randomizes only the middle tiles
        for r in range(len(room)):
            for c in range(len(room[r])):
                if (r != 0 and r != len(room) - 1) and (c != 0 and c != len(room[r]) - 1):
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

