import pygame
from circleshape import CircleShape
from constants import *  # noqa: F403
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)  # noqa: F405
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)  # type: ignore

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt  # noqa: F405

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt  # noqa: F405

    def update(self, dt):
        keys = pygame.key.get_pressed()
        # Left
        if keys[pygame.K_a]:
            self.rotate(dt)
        # Right
        if keys[pygame.K_e]:
            self.rotate(-dt)
        # Up
        if keys[pygame.K_COMMA]:
            self.move(dt)
        if keys[pygame.K_o]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.timer -= dt

    def shoot(self):
        if self.timer > 0:
            return
        bullet = Shot(self.position.x, self.position.y)
        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED  # noqa: F405
        self.timer = PLAYER_SHOT_COOLDOWN  # noqa: F405
