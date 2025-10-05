import pygame
from typing import ClassVar


# Base class for game objecs
class CircleShape(pygame.sprite.Sprite):
    containers: ClassVar[tuple] = ()

    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: float = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, asteroid: "CircleShape") -> bool:
        dx = self.position.x - asteroid.position.x
        dy = self.position.y - asteroid.position.y
        # distance between the two circles centers
        distance_between_2asteroids = (dx**2 + dy**2) ** 0.5  # pythagorean theorem
        # minimum distance when the two circles edges touch
        min_dist_for_collision = self.radius + asteroid.radius

        return distance_between_2asteroids <= min_dist_for_collision
