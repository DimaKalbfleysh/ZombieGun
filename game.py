import pygame


class Game:
    win = pygame.display.set_mode((450, 280))

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Zombie Gun")
        self.run = True
        self.button = False
        self.start_game = False
        self.main_character = None
        self.clock = pygame.time.Clock()
        self.button_start_game = pygame.draw.rect(self.win, (0, 0, 0), (135, 60, 180, 18))
        self.shells = []
        self.zombies = []
        self.skeletons = []
        self.money = 0
        self.total_killed = 0

    def get_button_start_game(self):
        if self.main_character.death:
            self.button_start_game = pygame.draw.rect(self.win, (0, 0, 0), (135, 60, 180, 18))
        else:
            self.button_start_game = pygame.draw.rect(self.win, (0, 0, 0), (0, 0, 0, 0))

    def get_start_game(self):
        self.start_game = not self.main_character.death

    def stop_music(self):
        if self.main_character.death:
            pygame.mixer.music.stop()

    def start_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("documents/XXXTentacion - Look at Me (minus).mp3")
        pygame.mixer.music.play(-1)

    def stop_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
