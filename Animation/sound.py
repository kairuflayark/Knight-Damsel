import pygame
import time

pygame.display.init()
pygame.display.set_mode((10, 10))

pygame.mixer.init()

coin = pygame.mixer.Sound("Thwack.wav")
# coin = pygame.mixer.Sound("Rainy.ogg")
# pygame.mixer.Sound("TheLoomingBattle.OGG")
# pygame.music.play()



coin.play()

time.sleep(30)

pygame.quit()