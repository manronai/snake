# Simple pygame program

# Import and initialize the pygame library
import time

import pygame
from snakeclass import snake
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
snkobj = snake()
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    snkobj.createBody(pygame, screen)
    if pygame.key.get_pressed()[pygame.K_LEFT] == True:
        snkobj.leftOn()

    if pygame.key.get_pressed()[pygame.K_RIGHT] == True:
        snkobj.rightOn()

    if pygame.key.get_pressed()[pygame.K_UP] == True:
        snkobj.upOn()

    if pygame.key.get_pressed()[pygame.K_DOWN] == True:
        snkobj.downOn()

    snkobj.move()


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()