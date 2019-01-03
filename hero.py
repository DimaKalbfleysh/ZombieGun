import pygame

from shot import Shot
from sprite import SHOOTING, STAND_GG


class Hero:
    def __init__(self, win):
        self.win = win
        self.hp = 100
        self.animation = 0
        self.position = 1
        self.width_hp = 40
        self.y = 210
        self.x = 226
        self.death = False

    def move(self, step, position):
        """ Метод передвигает героя """
        self.position = position
        self.x += step

    def draw_walking(self, sprite):
        """ Метод отображает идущего героя """
        if self.animation + 1 >= 24:
            self.animation = 0
        sprite_index = self.animation // 6
        pygame.display.update(self.win.blit(sprite[sprite_index], (self.x, self.y)))
        self.animation += 1

    def is_death(self):
        """ Метод проверяет герой умер или нет """
        if self.width_hp <= 0 and self.hp <= 0:
            self.death = True

    def shooting(self, shots):
        """ Метод создаёт пули """
        if len(shots) < 10:
            if self.position:
                coordinates_shot = [round(self.x + 45), round(self.y + 22)]
                shot = Shot(coordinates_shot, 1)
            else:
                coordinates_shot = [round(self.x + 10), round(self.y + 22)]
                shot = Shot(coordinates_shot, -1)
            shots.append(shot)
        return shots

    def draw_shooting(self):
        """ Метод отображает стреляющего героя """
        pygame.display.update(self.win.blit(SHOOTING[self.position], (self.x, self.y)))

    def draw_standing(self):
        """ Метод отображает стоящего героя """
        pygame.display.update(self.win.blit(STAND_GG[self.position], (self.x, self.y)))
