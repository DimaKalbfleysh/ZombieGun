import pygame
import random
from vars import SKELETON_LEFT
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
animation_zombie = 0
animation_skeleton = 0
animation_gg = 0
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
gift = False
coin = False
k = -1
total_killed = 0
zobmie_killed = 0
skeletons_killed = 0
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
    def __init__(self, x, y, hp, width_hp, height):
        self.x = x
        self.y = y
        self.hp = hp
        self.width = width_hp
        self.height = height

    def draw(self, animation, fps, sprites):
        pygame.draw.rect(win, (255, 0, 0), (self.x - 15, self.y, self.width, self.height))
        win.blit(sprites[animation // fps], (self.x, self.y))

        # fontObj = pygame.font.Font('freesansbold.ttf', 15)
        # textSurfaceObj = fontObj.render('lvl' + str(level), True, (128, 128, 128))
        # textRectObj = textSurfaceObj.get_rect()
        # textRectObj.center = (self.x + 23, self.y - 15)
        # win.blit(textSurfaceObj, textRectObj)


def draw_window():
    global animation_gg, animation_zombie, animation_skeleton
    win.blit(BG, (0, 0))
    win.blit(SKULL, (0, 0))
    win.blit(COIN_1, (60, 0))
    if animation_gg + 1 >= 32:
        animation_gg = 0
    if left:
        win.blit(GG_LEFT[animation_gg // 8], (x, y))
        animation_gg += 1

    elif right:
        win.blit(GG_RIGHT[animation_gg // 8], (x, y))
        animation_gg += 1

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

    for zomb in zombies:
        zomb.draw(animation_zombie, 20, ZOMBIE_LVL_1)
        animation_zombie += 1
        if animation_zombie + 1 >= 60:
            animation_zombie = 0

    for sh in shots:
        sh.draw_shot()

    for skelet in skeletons:
        skelet.draw(animation_skeleton, 10, SKELETON_LEFT)
        animation_skeleton += 1
        if animation_skeleton + 1 >= 30:
            animation_skeleton = 0

    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render(str(total_killed), True, (255, 0, 0))
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
gift_y = -100
gift_x = random.randrange(0, 400)


def exit_the_game(run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    return run


def killing_monsters(monsters, shots, damage, *args):
    global total_killed, zobmie_killed
    for monster in monsters:
        for shot in shots:
            if monster.x + args[0] == shot.shot_x or monster.x + args[1] == shot.shot_x:
                monster.hp -= 50
                shots.pop(shots.index(shot))
                if monster.width > 0:
                    monster.width -= damage
        if monster.hp <= 0:
            monsters.pop(monsters.index(monster))
            total_killed += 1
            zobmie_killed += 1


while run:
    clock.tick(120)
    pos = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    if But1.collidepoint(pos):
        button1 = True
    else:
        button1 = False

    pos = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    if But1.collidepoint(pos) and pressed1:
        start_game = True
        width = 40
        GG_xp = 100
        x = 226
        damage = False
        gift = False
        coin = False
        zombies = []
        skeletons = []
        shots = []
        total_killed = 0
        zobmie_killed = 0
        skeletons_killed = 0
        gift_x = random.randrange(0, 400)
        gift_y = 0
        pygame.mixer.init()
        pygame.mixer.music.load("documents/XXXTentacion - Look at Me (minus).mp3")
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
            if zombie.x == 100:
                Zombie = Monster(round(x1), round(200), 100, 40, 3)
                zombies.append(Zombie)
            if zombie.x == x:
                damage = True
                if width > 0:
                    GG_xp -= 25
                    width -= 10
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
                Skeleton = Monster(round(470), round(195), 200, 80, 3)
                skeletons.append(Skeleton)
            if skeleton.x == x + 10:
                damage = True
                GG_xp -= 50
                width -= 20

            if skeleton.x == x or skeleton.x == x - 1 or skeleton.x == x - 2:
                damage = False
            if width <= 0 and GG_xp <= 0:
                pygame.mixer.music.stop()
                start_game = False
        killing_monsters(zombies, shots, 20, 30, 29)
        killing_monsters(skeletons, shots, 25, 0, 1)

        if total_killed % 10 == 9 and not coin:
            if gift_y < -50:
                gift_x = random.randrange(0, 400)
            gift = True

        if gift:
            if gift_y < 230:
                gift_y += 3
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

        if len(zombies) < 1:
                zombies.append(Monster(round(x1), round(200), 100, 40, 3))
        if len(skeletons) < 1:
            skeletons.append(Monster(round(470), round(195), 200, 80, 3))

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
    run = exit_the_game(run)
    draw_game()
pygame.quit()
