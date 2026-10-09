import pygame
from Settings import *

class Menu:
    def __init__(self, player, toggle_menu):

        #general setup
        self.player = player
        self.toggle_menu = toggle_menu
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('./s4 - Animations/graphics/font/lycheeSoda.ttf',30)

    def update(self):
        self.display_surface.blit(Surface(1000,1000), (0,0)) 