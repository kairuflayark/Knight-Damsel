import RoomRandomizer

#4x4 array of rooms

def BDRand():
    randomInt = random.randint(0, 10)
    if randomInt > 4:
        room = RoomRandomizer.buildRoom(4)
    else:
        room = RoomRandomizer.room
    return room


def buildDungen():
    dungenRooms = [
        [BDRand(),BDRand(),BDRand(),BDRand()],
        [BDRand(),BDRand(),BDRand(),BDRand()],
        [BDRand(),BDRand(),BDRand(),BDRand()],
        [BDRand(),BDRand(),BDRand(),BDRand()]
    ]
    return dungenRooms
