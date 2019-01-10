import pygame
from shell import Shell
from sprite import SHOOTING, STAND_GG


class Hero:
    """ The class is responsible for the behavior of the hero. """
    def __init__(self, win):
        self.win = win
        self.hp = 100
        self.animation = 0
        self.position = 1
        self.width_hp = 40
        self.y = 210
        self.x = 226
        self.death = False
        self.damage = 25

    def move(self, step, position):
        """ The method moves the hero. """
        self.position = position
        self.x += step

    def draw_walking(self, sprite):
        """ The method displays the walking hero. """
        if self.animation + 1 >= 24:
            self.animation = 0
        sprite_index = self.animation // 6
        pygame.display.update(self.win.blit(sprite[sprite_index], (self.x, self.y)))
        self.animation += 1

    def is_death(self):
        """ Method is checking hero died or not. """
        if self.width_hp <= 0 and self.hp <= 0:
            self.death = True

    def shooting(self, shells):
        """ The method is responsible for the behavior of the projectile. """
        if len(shells) < 10:
            if self.position:
                coordinates_shell = [round(self.x + 45), round(self.y + 22)]
                shell = Shell(coordinates_shell, 1)
            else:
                coordinates_shell = [round(self.x + 10), round(self.y + 22)]
                shell = Shell(coordinates_shell, -1)
            shells.append(shell)
        return shells

    def draw_shooting(self):
        """ The method displays the shooting hero. """
        pygame.display.update(self.win.blit(SHOOTING[self.position], (self.x, self.y)))

    def draw_standing(self):
        """ The method displays the standing hero. """
        pygame.display.update(self.win.blit(STAND_GG[self.position], (self.x, self.y)))
