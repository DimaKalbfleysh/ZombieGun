import pygame


class Monster:
    """ The class is responsible for the behavior of the monster. """
    monsters = None
    step = None
    height_hp = 4
    animation = 0

    def __init__(self, win, coordinates, sprites, hp, fps, damage, hero, game):
        self.win = win
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.fps = fps
        self.damage = damage
        self.hero = hero
        self.hp = hp
        self.width_hp = (hp / 50) * 20
        self.sprites = sprites
        self.game = game

    def draw(self):
        """ The method displays the walking monster. """
        if self.animation + 1 >= self.fps * 3:
            self.animation = 0
        pygame.draw.rect(self.win, (0, 0, 255), (self.x - 15, self.y, self.width_hp, self.height_hp))
        self.win.blit(self.sprites[self.animation // self.fps], (self.x, self.y))
        self.animation += 1
        # fontObj = pygame.font.Font('freesansbold.ttf', 15)
        # textSurfaceObj = fontObj.render('lvl' + str(level), True, (128, 128, 128))
        # textRectObj = textSurfaceObj.get_rect()
        # textRectObj.center = (self.x + 23, self.y - 15)
        # win.blit(textSurfaceObj, textRectObj)

    def move(self):
        """
        The method is responsible for the movement of the monster,
        all the logic of the movement you have to redefine.
        """
        pass

    def blow(self):
        """ The method responsible for dealing damage to the hero. """
        self.hero.hp -= self.damage
        self.hero.width_hp -= self.damage / 2.5

    def death(self):
        """ The method is responsible for the death of the monster. """
        for sh in self.game.shells:
            if self.x == sh.x:
                self.hp -= 50
                self.game.shells.remove(sh)
                if self.width_hp > 0:
                    self.width_hp -= self.hero.damage
        if self.hp <= 0:
            self.monsters.remove(self)
            self.game.total_killed += 1


class Zombie(Monster):
    def move(self):
        """ The method moves the zombie to the right. """
        self.step = 1
        self.monsters = self.game.zombies
        if self.x < 450:
            self.x += self.step
        else:
            self.monsters.remove(self)


class Skeleton(Monster):
    def move(self):
        """ The method moves the skeleton to the left. """
        self.step = -1
        self.monsters = self.game.skeletons
        if 1 < self.x:
            self.x += self.step
        else:
            self.monsters.remove(self)
