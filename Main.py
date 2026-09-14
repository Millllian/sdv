import pygame, sys
from Settings import *
from Level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Pydew Valley')
        self.clock = pygame.time.Clock()
        self.Level = Level()

    def run(self):
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                dt = self.clock.tick() / 1000
                self.Level.run(dt)
                pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()