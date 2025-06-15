import circleshape
import pygame

class Asteroid(circleshape.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.pos_x = x
        self.pos_y = y
        self.radius = radius

    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.pos_x, self.pos_y), 
                           self.radius, 2)

    def update(self, dt):
        self.velocity += self.velocity * dt
