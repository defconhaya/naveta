import pygame
from settings import *
from bullet import Bullet

class Naveta(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load('gfx/naveta.png')
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH /2, SCREEN_HEIGHT / 2))
    
    def update(self) -> None:
        self.rect.center = pygame.mouse.get_pos()

    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])