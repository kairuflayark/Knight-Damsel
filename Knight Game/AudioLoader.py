import pygame
import time

pygame.mixer.init()

sounds = []
songs = []
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


adventure = pygame.mixer.Sound("Assets/Sounds/adventure.ogg")

adventure.play(-1)

time.sleep(30)

pygame.quit()