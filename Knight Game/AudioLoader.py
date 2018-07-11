import pygame

pygame.mixer.init()

sounds = []
songs = []
soundTracks = {}
musicTracks = {}
  
#for music
def addMusic(sound):
    global songs
    if song not in songs:
        songs.append(song)

def removeMusic(sound):
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
