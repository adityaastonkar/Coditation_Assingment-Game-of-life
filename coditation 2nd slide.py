# importing necessary packages for execution
import numpy as np
import pygame
from coditation import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
# This sets the margin between each cell
MARGIN = 5
# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [580, 580]
screen = pygame.display.set_mode(WINDOW_SIZE)
# Set the screen background
screen.fill(BLACK)

# Set title of screen
pygame.display.set_caption("Coditation")


# to run the loop continuosly
done = False

# Screen update
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one or zero
            grid[row][column] = 1 if grid[row][column]== 0 else 0
        # check if the key is pressed
        elif event.type == pygame.KEYDOWN:
            # setting spacebar key function
            if event.key==pygame.K_SPACE:
                Check_conditions(grid)
            # setting R key for reset
            elif event.key == pygame.K_r:
                grid = np.zeros((23, 23))
                Check_conditions(grid)

    # creating grid on screen
    for row in range(23):
        for column in range(23):
            color = WHITE
            if grid[row][column] == 1:
                color = BLACK
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # 60 frames per second
    clock.tick(60)

    # update screen
    pygame.display.flip()

# on exit.
pygame.quit()