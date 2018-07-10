"""
ACTION SCREEN

    1) Draw ACTION SCREEN

    2) Display ENEMY

        1) Display NAME

        2) Display HP

        3) Display SPRITE

    3) Display ALLY (Inherits from Enemy perhaps)

        1) CHECK for Ally

        1) Display NAME

        2) Display HP

        3) Display SPRITE

    4) Display ACTIVITY BOX

        a) Display ENEMY TEXT

        b) Display ACTION BOX

            i)      Attack

                        i) Display ATTACK RESULTS

            ii)     Check

                        i) Display ENEMY TEXT

            iii)    Leave

                        a) EXIT Action Screen

"""

import pygame
import sys
import TextBox

pygame.draw.rect(pygame.display.set_mode((600,400), 0, 32), (0,0,0), (0, 300, 600, 400))
TextBox.Pane.addRect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();

