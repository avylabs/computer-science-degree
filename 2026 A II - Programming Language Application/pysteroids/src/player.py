import pygame
import math
from bullet import Bullet

idle_sprite = pygame.image.load("./assets/sprites/spaceship/spaceship.png")
thrust_sprite = pygame.image.load("assets/sprites/spaceship/spaceship_thrust.png")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = idle_sprite
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.x = pygame.display.get_window_size()[0] / 2
        self.y = pygame.display.get_window_size()[1] / 2
        self.thrust = False
        self.spd = 0.1
        self.vel_x = 0
        self.vel_y = 0
        self.angle = 0
        self.rotated = pygame.transform.rotate(self.sprite, self.angle)
        self.rect = self.rotated.get_rect()
        self.rect.center = (self.x, self.y)
        self.cosseno = math.cos(math.radians(self.angle + 90))
        self.seno = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosseno + self.width / 2, self.y - self.seno * self.height / 2)
    
    def draw(self, screen):
        if self.thrust == True:
            self.sprite = thrust_sprite
        else:
            self.sprite = idle_sprite
        screen.blit(self.rotated, self.rect)

    def move_left(self):
        self.angle += 5
        self.rotated = pygame.transform.rotate(self.sprite, self.angle)
        self.rect = self.rotated.get_rect()
        self.rect.center = (self.x, self.y)
        self.cosseno = math.cos(math.radians(self.angle + 90))
        self.seno = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosseno * self.width / 2, self.y - self.seno * self.height / 2)

    def move_right(self):
        self.angle -= 5
        self.rotated = pygame.transform.rotate(self.sprite, self.angle)
        self.rect = self.rotated.get_rect()
        self.rect.center = (self.x, self.y)
        self.cosseno = math.cos(math.radians(self.angle + 90))
        self.seno = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosseno + self.width / 2, self.y - self.seno * self.height / 2)

    def move_foward(self, keys):
        if keys[pygame.K_UP]:
            self.thrust = True
            self.vel_x += self.cosseno * self.spd
            self.vel_y -= self.seno * self.spd
        else:
            self.thrust = False

        self.x += max(-4, min(self.vel_x, 4))
        self.y += max(-4, min(self.vel_y, 4))

        self.rotated = pygame.transform.rotate(self.sprite, self.angle)
        self.rect = self.rotated.get_rect()
        self.rect.center = (self.x, self.y)
        self.cosseno = math.cos(math.radians(self.angle + 90))
        self.seno = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosseno * self.width / 2, self.y - self.seno * self.height / 2)
    
    def warp(self):
        if self.x < 0:
            self.x = pygame.display.get_window_size()[0]
        elif self.x > pygame.display.get_window_size()[0]:
            self.x = 0
            
        if self.y < 0:
            self.y = pygame.display.get_window_size()[1]
        elif self.y > pygame.display.get_window_size()[1]:
            self.y = 0