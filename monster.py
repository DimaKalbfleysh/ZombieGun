import pygame


class Monster:
    def __init__(self, win, coordinates, sprites, hp, fps, damage, main_character, step):
        self.win = win
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.fps = fps
        self.damage = damage
        self.main_character = main_character
        self.step = step
        self.animation = 0
        self.height_hp = 4
        self.hp = hp
        self.width_hp = (hp / 50) * 20
        self.sprites = sprites

    def draw(self):
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

    def move(self, monsters):
        pass

    def blow(self):
        self.main_character.hp -= self.damage
        self.main_character.width_hp -= self.damage / 2.5


class Zombie(Monster):
    def move(self, monsters):
        if self.x < 450:
            self.x += self.step
        else:
            monsters.remove(self)


class Skeleton(Monster):
    def move(self, monsters):
        if 1 < self.x:
            self.x += self.step
        else:
            monsters.remove(self)
