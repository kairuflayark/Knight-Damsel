import pygame
import time

pygame.mixer.init()

adventure = pygame.mixer.Sound("Assets/Sounds/adventure.ogg")
dungeon_boss = pygame.mixer.Sound("Assets/Sounds/dungeon_boss.ogg")
dungeon_entry = pygame.mixer.Sound("Assets/Sounds/dungeon_entry.ogg")
epic = pygame.mixer.Sound("Assets/Sounds/epic.ogg")
road = pygame.mixer.Sound("Assets/Sounds/road.ogg")
soft_battle = pygame.mixer.Sound("Assets/Sounds/soft_battle.ogg")

sounds = []
songs = [adventure, dungeon_boss, dungeon_entry, epic, road, soft_battle]
soundTracks = {}
musicTracks = {}
  
#for music
def addMusic(song):
    global songs
    if song not in songs:
        songs.append(song)

def removeMusic(song):
    global songs
    if song in songs:
        songs.remove(song)


#for sounds
def addSound(sound):
    global sounds
    if sound not in sounds:
        sounds.append(sound)

def removeSound(sound):
    global sounds
    if sound in sounds:
        sounds.remove(sound)
   
def loadSound(path):
    global soundTracks
    if path not in soundTracks:
        soundTracks[path] = pygame.mixer.Sound(path)
    return soundTracks[path]

def loadMusic(path):
    global musicTracks
    if path not in musicTracks:
        musicTracks[path] = pygame.mixer.music.load(path)
    return musicTracks[path]


def playMusic(playSong):
    global songs
    if playSong in songs:
            playSong.play()

playSong = songs[0]
playMusic(playSong)
# adventure = pygame.mixer.Sound("Assets/Sounds/adventure.ogg")
# dungeon_boss = pygame.mixer.Sound("Assets/Sounds/dungeon_boss.ogg")
# dungeon_entry = pygame.mixer.Sound("Assets/Sounds/dungeon_entry.ogg")
# epic = pygame.mixer.Sound("Assets/Sounds/epic.ogg")
# road = pygame.mixer.Sound("Assets/Sounds/road.ogg")
# soft_battle = pygame.mixer.Sound("Assets/Sounds/soft_battle.ogg")

# adventure.play(-1)

time.sleep(30)

pygame.quit()