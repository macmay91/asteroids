# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *

def main():
    pygame.init()
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)

    player_ship = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        clock.tick(60)
        dt = clock.tick(60)/1000
        
        for object in updatable:
            object.update(dt)

        for object in asteroids:
            if object.collision(player_ship):
                print("Game over!")
                sys.exit()

        #rendering
        screen.fill((0, 0, 0))
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()




if __name__ == "__main__":
    main()