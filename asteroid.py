import pygame
import random

from circleshape import CircleShape
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
        
        new_angle = random.uniform(20, 50)

        angle_a = self.velocity.rotate(new_angle)
        angle_b = self.velocity.rotate(-new_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        ast_1.velocity = angle_a * 1.2
        ast_2.velocity = angle_b * 1.2