import pygame
import random
from vars import SKELETON_LEFT
from vars import ZOMBIE_LVL_2
from vars import ZOMBIE_LVL_1
from vars import MAIN_MENU
from vars import MAIN_MENU_START_GAME
from vars import BG
from vars import SKULL
from vars import COIN_1
from vars import GG_LEFT
from vars import GG_RIGHT
from vars import SHOOTING
from vars import DAMAGE_GG
from vars import STAND_GG
from vars import GIFT
from vars import COIN

pygame.init()
win = pygame.display.set_mode((450, 280))
pygame.display.set_caption("Zombie Gan")
clock = pygame.time.Clock()

x = 226
y = 210
width = 40
GG_xp = 100
anim1 = 0
anim2 = 0
anim = 0
x1 = -20
speed = 2
left = False
right = False
shooting = False
damage = False
death = False
button1 = False
start_game = False
lvl2 = False
death_zombie = False
gift = False
coin = False
k = -1
a = 0
q = 0
w = 0
A = random.randrange(1, 4)
But1 = pygame.draw.rect(win, (0, 0, 0), (135, 60, 180, 18))


class Shot:
    def __init__(self, shot_x, shot_y, radius, color, facing):
        self.shot_x = shot_x
        self.shot_y = shot_y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 1 * facing

    def draw_shot(self):
        pygame.draw.circle(win, self.color, (self.shot_x, self.shot_y), self.radius)


class Monster:
    def __init__(self, x, y, xp, width, height):
        self.x = x
        self.y = y
        self.xp = xp
        self.width = width
        self.height = height


class Skeleton(Monster):
    def draw(self, anim, fps, fps_1):
        if anim + 1 >= fps:
            anim = 0
        pygame.draw.rect(win, (255, 0, 0), (self.x - 15, self.y, self.width, self.height))
        win.blit(SKELETON_LEFT[anim // fps_1], (self.x, self.y))


class Zombie(Monster):
    def draw(self, anim, fps, fps_1):
        if anim + 1 >= fps:
            anim = 0
        pygame.draw.rect(win, (255, 0, 0), (self.x + 5, self.y, self.width, self.height))
        win.blit(ZOMBIE_LVL_1[anim // fps_1], (self.x, self.y))
        # fontObj = pygame.font.Font('freesansbold.ttf', 15)
        # textSurfaceObj = fontObj.render('lvl' + str(level), True, (128, 128, 128))
        # textRectObj = textSurfaceObj.get_rect()
        # textRectObj.center = (self.x + 23, self.y - 15)
        # win.blit(textSurfaceObj, textRectObj)


def draw_window():
    global anim, anim1, k, anim2, death_zombie, coin_x, coin_y
    win.blit(BG, (0, 0))
    win.blit(SKULL, (0, 0))
    win.blit(COIN_1, (60, 0))
    if anim + 1 >= 32:
        anim = 0
    if left:
        win.blit(GG_LEFT[anim // 8], (x, y))
        anim += 1

    elif right:
        win.blit(GG_RIGHT[anim // 8], (x, y))
        anim += 1

    elif shooting:
        if k == -1:
            win.blit(SHOOTING[0], (x, y))
        else:
            win.blit(SHOOTING[1], (x, y))
    elif damage:
        if k == -1:
            win.blit(DAMAGE_GG[0], (x, y))
        else:
            win.blit(DAMAGE_GG[1], (x, y))

    else:
        if k == -1:
            win.blit(STAND_GG[0], (x, y))
        else:
            win.blit(STAND_GG[1], (x, y))
    if gift:
        win.blit(GIFT, (gift_x, gift_y))
    if coin:
        win.blit(COIN, (coin_x, coin_y))

    pygame.draw.rect(win, (255, 0, 0), (x, y, width, 3))
    for zombie in zombies:
        zombie.draw(anim1, 30, 20)
        anim1 += 1
    for shot in shots:
        shot.draw_shot()
    for skeleton in skeletons:
        skeleton.draw(anim2, 60, 20)
        anim2 += 1

    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render(str(a), True, (255, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (40, 15)
    win.blit(textSurfaceObj, textRectObj)

    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render(str(money), True, (255, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (100, 15)
    win.blit(textSurfaceObj, textRectObj)


def draw_game():
    win.blit(MAIN_MENU, (0, 0))
    if button1:
        win.blit(MAIN_MENU_START_GAME, (0, 0))
    if start_game:
        draw_window()
    pygame.display.update()


money = 0
shots = []
zombies = []
skeletons = []
run = True
t = 1
N = 1
gift_y = -100
gift_x = random.randrange(0, 400)
while run:
    clock.tick(60)
    pos = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    if But1.collidepoint(pos):
        button1 = True
    else:
        button1 = False

    pos = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    if But1.collidepoint(pos) and pressed1:
        print(button1)
        start_game = True
        width = 40
        GG_xp = 100
        x = 226
        damage = False
        lvl2 = False
        gift = False
        coin = False
        zombies = []
        skeletons = []
        shots = []
        a = 0
        q = 0
        w = 0
        gift_x = random.randrange(0, 400)
        gift_y = 0
        N = 1
        pygame.mixer.init()
        pygame.mixer.music.load("MuseUprising.mp3")
        pygame.mixer.music.play(-1)
        coin_x = gift_x + 25
        coin_y = gift_y + 30
        money = 0

    if start_game:
        for shot in shots:
            if 450 > shot.shot_x > 1:
                shot.shot_x += shot.vel
            else:
                shots.pop(shots.index(shot))
        for zombie in zombies:
            if zombie.x < 450:
                zombie.x += 1
            else:
                zombies.pop(zombies.index(zombie))
            if lvl2:
                if zombie.x == 80:
                    zombies.append(Zombie(round(x1), round(187), 250, 60, 3))
            else:
                if zombie.x == 100:
                    zombies.append(Zombie(round(x1), round(200), 100, 40, 3))
            if lvl2:
                if zombie.x == x:
                    damage = True
                    if width > 0:
                        GG_xp -= 50
                        width -= 20
                        print(GG_xp)
            else:
                if zombie.x == x:
                    damage = True
                    if width > 0:
                        GG_xp -= 25
                        width -= 10
                        print(GG_xp)
            if zombie.x == x + 10 or zombie.x == x + 9 or zombie.x == x + 8:
                damage = False
            if width == 0 and GG_xp <= 0:
                pygame.mixer.music.stop()
                start_game = False

        for skeleton in skeletons:
            if skeleton.x > 1:
                skeleton.x -= 1
            else:
                skeletons.pop(skeletons.index(skeleton))
            if skeleton.x == 250:
                skeletons.append(Skeleton(round(470), round(195), 200, 80, 3))
            if skeleton.x == x + 10:
                damage = True
                if width > 0:
                    GG_xp -= 50
                    width -= 20
                    print(GG_xp)

            if skeleton.x == x or skeleton.x == x - 1 or skeleton.x == x - 2:
                damage = False
            if width <= 0 and GG_xp <= 0:
                pygame.mixer.music.stop()
                start_game = False

        for zombie in zombies:
            for shot in shots:
                if zombie.x + 30 == shot.shot_x or zombie.x + 29 == shot.shot_x:
                    zombie.xp -= 50
                    shots.pop(shots.index(shot))
                    if zombie.width > 0:
                        if lvl2:
                            zombie.width -= 12
                        else:
                            zombie.width -= 20

            if zombie.xp == 0:
                death_zombie = True
                zombies.pop(zombies.index(zombie))
                a += 1
                q += 1

        for skeleton in skeletons:
            for shot in shots:
                if skeleton.x == shot.shot_x or skeleton.x + 1 == shot.shot_x:
                    skeleton.xp -= 50
                    shots.pop(shots.index(shot))
                    if skeleton.width > 0:
                        skeleton.width -= 25
            if skeleton.xp == 0:
                skeletons.pop(skeletons.index(skeleton))
                a += 1
                w += 1

        Z = a % 10
        if Z == 9 and coin is False:
            if gift_y < -50:
                gift_x = random.randrange(0, 400)
            gift = True
        if gift:
            if gift_y < 230:
                gift_y += 1
            else:
                gift = False
                coin = True
                gift_y = -100
        if coin:
            coin_x = gift_x + 25
            coin_y = 260
            if coin_x == x or coin_x == x + 1:
                coin = False
                money += 1

        if q >= 20:
            lvl2 = True
            if len(zombies) < 1:
                zombies.append(Zombie(round(x1), round(187), 250, 60, 3))
        else:
            if len(zombies) < 1:
                zombies.append(Zombie(round(x1), round(200), 100, 40, 3))
        if len(skeletons) < 1:
            skeletons.append(Skeleton(round(470), round(195), 200, 80, 3))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 1:
            k = -1
            x -= speed
            left = True
            right = False

        elif keys[pygame.K_RIGHT] and x < 420:
            k = 1
            x += speed
            left = False
            right = True
        elif keys[pygame.K_SPACE]:
            shooting = True
            if k == 1:
                facing = 1
            else:
                facing = -1
            if len(shots) < 10:
                if k == 1:
                    shots.append(Shot(round(x + 45), round(y + 22), 3, (255, 0, 0), facing))
                else:
                    shots.append(Shot(round(x + 10), round(y + 22), 3, (255, 0, 0), facing))
        else:
            left = False
            right = False
            shooting = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_game()
pygame.quit()
