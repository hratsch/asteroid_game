import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random.uniform(20, 50)
        v1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
        v2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, new_radius)
        Asteroid(self.position.x, self.position.y, new_radius)
        v1 *= 1.2
        v2 *= 1.2
