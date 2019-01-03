import pygame


class Window:
    def __init__(self, win, main_character):
        self.win = win
        self.main_character = main_character

    def get_button_start_game(self):
        if self.main_character.death:
            button_start_game = pygame.draw.rect(self.win, (0, 0, 0), (135, 60, 180, 18))
        else:
            button_start_game = pygame.draw.rect(self.win, (0, 0, 0), (0, 0, 0, 0))
        return button_start_game

    def get_start_game(self):
        start_game = not self.main_character.death
        return start_game

    def stop_music(self):
        if self.main_character.death:
            pygame.mixer.music.stop()

    def start_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("documents/XXXTentacion - Look at Me (minus).mp3")
        pygame.mixer.music.play(-1)
