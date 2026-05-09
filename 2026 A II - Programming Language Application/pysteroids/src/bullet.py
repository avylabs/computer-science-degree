import pygame
import math

bullet_sprite = pygame.image.load("./assets/sprites/spaceship/bullet.png")

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, seno, cosseno, screen):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = bullet_sprite
        self.point = pos
        self.x, self.y = self.point
        self.x_spd = cosseno * 10
        self.y_spd = seno * 10
        self.rect = self.sprite.get_rect()
        self.rect.center = (self.x, self.y)
    
    def move(self):
        self.x += self.x_spd
        self.y -= self.y_spd
        self.rect = self.sprite.get_rect()
        self.rect.center = (self.x, self.y)
    
    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))