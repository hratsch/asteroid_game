import pygame
from constants import *
from player import *

def main():
    # display welcome text
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initialize pygame
    pygame.init()

    # initalize game clock
    game_clock = pygame.time.Clock()
    dt = 0

    # get a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # implement group class
    Player.containers = (updatable, drawable)
    # implement Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # two groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # create game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill screen with solid black color
        pygame.Surface.fill(screen, color="black")

        # re-render player // being phased out w/ groups
        #player.draw(screen)
        #player.update(dt)

        # using groups
        updatable.update(dt)
        for player in drawable:
            player.draw(screen)
            



        # refreshes screen
        pygame.display.flip()

       

        # set fps to 60
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()