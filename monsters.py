import pygame
from vars import x, damage, GG_xp, width


class Monster:
    def __init__(self, x, y, hp, width_hp, height):
        self.x = x
        self.y = y
        self.hp = hp
        self.width = width_hp
        self.height = height

    def draw(self, win, animation, fps, sprites):
        pygame.draw.rect(win, (0, 0, 255), (self.x - 15, self.y, self.width, self.height))
        win.blit(sprites[animation // fps], (self.x, self.y))
        # fontObj = pygame.font.Font('freesansbold.ttf', 15)
        # textSurfaceObj = fontObj.render('lvl' + str(level), True, (128, 128, 128))
        # textRectObj = textSurfaceObj.get_rect()
        # textRectObj.center = (self.x + 23, self.y - 15)
        # win.blit(textSurfaceObj, textRectObj)

    def monster_movement(self, monsters):
        if self.x < 450:
            self.x += 1
        else:
            monsters.remove(self)

    def blow(self):
        global damage, GG_xp, width
        if self.x == x:
            damage = True
            GG_xp -= 25
            width -= 10
        if self.x == x + 10 or self.x == x + 9 or self.x == x + 8:
            damage = False
