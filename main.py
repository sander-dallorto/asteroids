import pygame
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    running = True
    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        
        updatables.update(dt)
        
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                raise SystemExit("Game Over!")
            
        for drawable in drawables:
            drawable.draw(screen)
    
        pygame.display.flip()
        ms = clock.tick(60)
        dt = ms/1000

if __name__ == "__main__":
    main()