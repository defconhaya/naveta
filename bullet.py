import pygame
from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.image = pygame.image.load('gfx/bullet1.png')
        self.rect = self.image.get_rect(center= (x, y))

    def update(self) -> None:
        self.rect.x += 5
        if self.rect.x >= SCREEN_WIDTH +20:
            self.kill()
