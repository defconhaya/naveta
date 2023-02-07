import pygame, sys
from settings import *
from naveta import Naveta

class Game:
    def __init__(self) -> None:
        pygame.init()        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.mouse.set_visible(False)
        pygame.display.set_caption("Naveta")
        self.clock = pygame.time.Clock()
        self.naveta_group = pygame.sprite.Group()
        self.bullets_group = pygame.sprite.Group()
        self.naveta = Naveta()
        self.naveta_group.add(self.naveta)

    def run(self):
        while True:            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.bullets_group.add(self.naveta.create_bullet())
            dt = self.clock.tick() / 1000            
            self.screen.fill((30,30,30))
            self.naveta_group.draw(self.screen)
            self.bullets_group.draw(self.screen)
            self.naveta_group.update()
            self.bullets_group.update()
            pygame.display.flip()
            self.clock.tick(120)

if __name__ == '__main__':
    
    game = Game()
    game.run()