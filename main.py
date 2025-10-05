from asteroid import Asteroid
from asteroidfield import AsteroidField
import pygame
from constants import *  # noqa: F403
from player import *  # noqa: F403
import sys


def main():
    pygame.init()
    x = SCREEN_WIDTH / 2  # noqa: F405
    y = SCREEN_HEIGHT / 2  # noqa: F405
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # noqa: F405
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)  # noqa: F405
    Shot.containers = (shots, updatable, drawable)  # noqa: F405

    player = Player(x, y)  # noqa: F405

    # Screen
    while True:
        #  so the game quits properly when you click close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)
        # detect if player collided with asteroid and exit + game over if so
        for ast in asteroids:
            if ast.collision(player):
                print("Game over!")
                sys.exit()

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        # limit FPS to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
