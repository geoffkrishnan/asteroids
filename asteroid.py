import pygame
import random
from circleshape import CircleShape
from constants import *  # noqa: F403


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:  # noqa: F405
            return
        split_angle = random.uniform(20, 50)
        angle1 = self.velocity.rotate(split_angle)
        angle2 = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS  # noqa: F405
        new_ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast1.velocity = angle1 * 1.2
        new_ast2.velocity = angle2 * 1.2
