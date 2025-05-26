import pygame
from constants import *

def main():
    # display welcome text
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initialize pygame
    pygame.init()

    # get a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill screen with solid black color
        pygame.Surface.fill(screen, color="black")
        # refreshes screen
        pygame.display.flip()

if __name__ == "__main__":
    main()