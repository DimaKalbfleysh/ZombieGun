import pygame
from sprite import MAIN_MENU_START_GAME, MAIN_MENU


class Window:
    def __init__(self, win):
        self.win = win

    def draw_start_button(self):
        pygame.display.update(self.win.blit(MAIN_MENU_START_GAME, (0, 0)))

    def draw_main_menu(self):
        pygame.display.update(self.win.blit(MAIN_MENU, (0, 0)))
