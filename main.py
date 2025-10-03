import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (drawables, updatables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for drawable in drawables:
            drawable.draw(screen)

        for updatable in updatables:
            updatable.update(dt)

        for asteroid in asteroids:
            asteroid.draw(screen)
            asteroid.update(dt)

        pygame.display.flip()

        clock.tick(60)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
