import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from circleshape import CircleShape

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius, colour="white"):
        super().__init__(x, y, radius)  
        self.colour = colour

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.position.x, self.position.y), self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt