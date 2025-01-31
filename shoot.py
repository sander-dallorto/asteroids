import pygame
from constants import SHOT_RADIUS
from circleshape import CircleShape

class Shoot(CircleShape):

    def __init__(self, x, y, radius = SHOT_RADIUS, colour="white"):
        super().__init__(x, y, radius)  
        self.colour = colour

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.position.x, self.position.y), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
