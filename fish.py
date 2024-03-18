import vector as v
import pygame

class Fish:
    def __init__(self, position, velocity, screen):
        self.position = position
        self.velocity = velocity
        self.screen = screen
        self.fishy = pygame.image.load('fish_image.png')

        
    def update(self, position, velocity):
        self.position = self.position + self.velocity

    def draw(self):
        self.screen.blit(self.fishy,(self.position.x,self.position.y))
        

     