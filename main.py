import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

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

    # groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # implement group class
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # get a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # implement Player object
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Asteroid Field object
    AsteroidField(Asteroid)

    # create game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill screen with solid black color
        pygame.Surface.fill(screen, color="black")

        # using groups
        updatable.update(dt)
        for objects in drawable:
            objects.draw(screen)

        # refreshes screen
        pygame.display.flip()

        # set fps to 60
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()