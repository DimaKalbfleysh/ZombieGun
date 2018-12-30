import pygame

from shot import Shot
from sprite import GG_LEFT, GG_RIGHT, SHOOTING, STAND_GG


class GG:
    def __init__(self, win):
        self.win = win
        self.x = 226
        self.y = 210
        self.width_hp_gg = 40
        self.gg_hp = 100
        self.animation_gg = 0
        self.position = 1
        self.speed = 2

    def move_left(self):
        self.position = 0
        self.x -= self.speed

    def draw_left(self):
        if self.animation_gg + 1 >= 32:
            self.animation_gg = 0
        pygame.display.update(self.win.blit(GG_LEFT[self.animation_gg // 8], (self.x, self.y)))
        self.animation_gg += 1

    def move_right(self):
        self.position = 1
        self.x += self.speed

    def draw_right(self):
        if self.animation_gg + 1 >= 32:
            self.animation_gg = 0
        pygame.display.update(self.win.blit(GG_RIGHT[self.animation_gg // 8], (self.x, self.y)))
        self.animation_gg += 1

    def death(self, start_game, But1):
        if not (self.width_hp_gg <= 0 and self.gg_hp <= 0):
            return [start_game, But1]
        pygame.mixer.music.stop()
        start_game = False
        But1 = pygame.draw.rect(self.win, (0, 0, 0), (135, 60, 180, 18))
        return [start_game, But1]

    def shooting(self, shots):
        if len(shots) < 10:
            if self.position == 1:
                coordinates_shot = [round(self.x + 45), round(self.y + 22)]
                shot = Shot(coordinates_shot, 1)
            else:
                coordinates_shot = [round(self.x + 10), round(self.y + 22)]
                shot = Shot(coordinates_shot, -1)
            shots.append(shot)
        return shots

    def draw_shooting(self):
        pygame.display.update(self.win.blit(SHOOTING[self.position], (self.x, self.y)))

    def stand(self):
        pygame.display.update(self.win.blit(STAND_GG[self.position], (self.x, self.y)))

