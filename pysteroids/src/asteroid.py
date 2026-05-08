import pygame
import math
import random

asteroid_big = pygame.image.load("./assets/sprites/asteroids/asteroid_big.png")
asteroid_medium = pygame.image.load("./assets/sprites/asteroids/asteroid_medium.png")
asteroid_small = pygame.image.load("./assets/sprites/asteroids/asteroid_small.png")

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, size, x=random.randint(0, 1280), y=random.randint(0, 720)):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = asteroid_big
        self.size = size
        self.x = x
        self.y = y
        self.x_spd = random.uniform(-1, 1)
        self.y_spd = random.uniform(-1, 1)
        self.rect = self.sprite.get_rect()
        self.rect.center = (self.x, self.y)
    
    def move(self):
        self.x += self.x_spd * random.randint(1, 3)
        self.y -= self.y_spd * random.randint(1, 3)
        self.rect = self.sprite.get_rect()
        self.rect.center = (self.x + self.sprite.get_width() / 2, self.y + self.sprite.get_height() / 2)
    
    def draw(self, screen):
        if self.size > 0:
            match self.size:
                case 3:
                    self.sprite = asteroid_big
                case 2:
                    self.sprite = asteroid_medium
                case 1:
                    self.sprite = asteroid_small
                case _:
                    return
            screen.blit(self.sprite, (self.x, self.y))

    def warp(self):
        if self.x < 0:
            self.x = pygame.display.get_window_size()[0]
        elif self.x > pygame.display.get_window_size()[0]:
            self.x = 0
            
        if self.y < 0:
            self.y = pygame.display.get_window_size()[1]
        elif self.y > pygame.display.get_window_size()[1]:
            self.y = 0