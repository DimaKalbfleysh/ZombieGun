from random import randrange

import pygame
from sprite import GIFT


class Bonus:
    """ The class is responsible for behavior of the bonus. """
    def __init__(self, win, sprite, hero, game):
        self.win = win
        self.gift_x = randrange(20, 400)
        self.gift_y = -100
        self.bonus_y = 260
        self.bonus_x = self.gift_x + 20
        self.hero = hero
        self.game = game
        self.sprite = sprite

    def draw_gift(self):
        """ The method displays gift. """
        pygame.display.update(self.win.blit(GIFT, (self.gift_x, self.gift_y)))

    def draw_bonus(self):
        """ The method displays bonus. """
        pygame.display.update(self.win.blit(self.sprite, (self.bonus_x, self.bonus_y)))

    def gift_movement(self):
        """ The method is responsible for movement gift. """
        if self.gift_y < 230:
            self.gift_y += 3
        else:
            self.gift_y = 500
            self.draw_bonus()

    def take_bonus(self):
        """
        The method is responsible for what happens after receiving the bonus,
        the logic of this you must override.
        """
        pass


class Coin(Bonus):
    def take_bonus(self):
        """ After taking the bonus, a coin is added. """
        if self.bonus_x == self.hero.x or self.bonus_x == self.hero.x + 1:
            self.game.money += 1
            self.game.coins.remove(self)
