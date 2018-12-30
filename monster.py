import pygame


class Monster:
    def __init__(self, coordinates, hp, width_hp_monster):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.hp = hp
        self.width_hp_monster = width_hp_monster
        self.height_hp_monster = 4
        self.animation = 0

    def draw(self, win, fps, sprites):
        if self.animation + 1 >= fps * 3:
            self.animation = 0
        pygame.draw.rect(win, (0, 0, 255), (self.x - 15, self.y, self.width_hp_monster, self.height_hp_monster))
        pygame.display.update(win.blit(sprites[self.animation // fps], (self.x, self.y)))
        self.animation += 1
        # fontObj = pygame.font.Font('freesansbold.ttf', 15)
        # textSurfaceObj = fontObj.render('lvl' + str(level), True, (128, 128, 128))
        # textRectObj = textSurfaceObj.get_rect()
        # textRectObj.center = (self.x + 23, self.y - 15)
        # win.blit(textSurfaceObj, textRectObj)

    def monster_movement(self, monsters, plus):
        if plus:
            if self.x < 450:
                self.x += 1
            else:
                monsters.remove(self)
        else:
            if self.x > 1:
                self.x -= 1
            else:
                monsters.remove(self)

    def blow(self, gg, damage):
        if self.x == gg.x:
            gg.gg_hp -= damage
            gg.width_hp_gg -= damage/2.5
