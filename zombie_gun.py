import pygame
from random import randrange

from monsters import Monster
from sprite import SKELETON_LEFT
from sprite import ZOMBIE_LVL_1
from sprite import MAIN_MENU
from sprite import MAIN_MENU_START_GAME
from sprite import BG
from sprite import SKULL
from sprite import COIN_1
from sprite import GG_LEFT
from sprite import GG_RIGHT
from sprite import SHOOTING
from sprite import DAMAGE_GG
from sprite import STAND_GG
from sprite import GIFT
from sprite import COIN
from vars import y, clock
from vars import x1
from vars import x
from vars import start_game
from vars import width
from vars import GG_xp
from vars import coin
from vars import gift
from vars import position
from vars import speed, run, skeletons, zombies, shots, gift_y, gift_x, money
from vars import animation_gg
from vars import animation_zombie
from vars import animation_skeleton

win = pygame.display.set_mode((450, 280))
pygame.init()
pygame.display.set_caption("Zombie Gun")


class Shot:
    def __init__(self, shot_x, shot_y, radius, color, facing):
        self.shot_x = shot_x
        self.shot_y = shot_y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 1 * facing

    def draw(self):
        pygame.draw.circle(win, self.color, (self.shot_x, self.shot_y), self.radius)


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
        win.blit(SHOOTING[position], (x, y))
    elif damage:
        win.blit(DAMAGE_GG[position], (x, y))
    else:
        win.blit(STAND_GG[position], (x, y))
    if gift:
        win.blit(GIFT, (gift_x, gift_y))
    if coin:
        win.blit(COIN, (coin_x, coin_y))

    pygame.draw.rect(win, (255, 0, 0), (x, y, width, 3))

    for zomb in zombies:
        zomb.draw(win,animation_zombie, 20, ZOMBIE_LVL_1)
        animation_zombie += 1
        if animation_zombie + 1 >= 60:
            animation_zombie = 0

    for sh in shots:
        sh.draw()

    for skelet in skeletons:
        skelet.draw(win, animation_skeleton, 10, SKELETON_LEFT)
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


def exit_the_game(run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    return run


def killing_monsters(monsters, damage, *args):
    global total_killed, zobmie_killed
    for monster in monsters:
        for shot in shots:
            if monster.x + args[0] == shot.shot_x or monster.x + args[1] == shot.shot_x:
                monster.hp -= 50
                shots.remove(shot)
                if monster.width > 0:
                    monster.width -= damage
        if monster.hp <= 0:
            monsters.remove(monster)
            total_killed += 1
            zobmie_killed += 1


def start_music():
    pygame.mixer.init()
    pygame.mixer.music.load("documents/XXXTentacion - Look at Me (minus).mp3")
    pygame.mixer.music.play(-1)


But1 = pygame.draw.rect(win, (0, 0, 0), (135, 60, 180, 18))
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
        But1 = pygame.draw.rect(win, (0, 0, 0), (0, 0, 0, 0))
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
        gift_x = randrange(20, 400)
        gift_y = 0
        start_music()
        coin_x = gift_x + 25
        coin_y = gift_y + 30
        money = 0

    if start_game:
        if not zombies:
            Zombie = Monster(round(x1), round(200), 150, 60, 4)
            zombies.append(Zombie)
        if not skeletons:
            Skeleton = Monster(round(470), round(195), 200, 80, 4)
            skeletons.append(Skeleton)

        for shot in shots:
            if 450 > shot.shot_x > 1:
                shot.shot_x += shot.vel
            else:
                shots.remove(shot)

        for zombie in zombies:
            zombie.monster_movement(zombies)
            zombie.blow()
            if zombie.x == 100:
                Zombie = Monster(round(x1), round(200), 150, 60, 4)
                zombies.append(Zombie)

        for skeleton in skeletons:
            if skeleton.x > 1:
                skeleton.x -= 1
            else:
                skeletons.remove(skeleton)
            if skeleton.x == 250:
                Skeleton = Monster(round(470), round(195), 200, 80, 4)
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
            But1 = pygame.draw.rect(win, (0, 0, 0), (135, 60, 180, 18))

        killing_monsters(zombies, 20, 30, 29)
        killing_monsters(skeletons, 25, 0, 1)

        if total_killed % 10 == 0 and total_killed // 10 != 0 and not coin:
            gift = True
            if gift_y < -50:
                gift_x = randrange(20, 400)

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

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 1:
            position = 0
            x -= speed
            left = True
            right = False

        elif keys[pygame.K_RIGHT] and x < 420:
            position = 1
            x += speed
            left = False
            right = True

        elif keys[pygame.K_SPACE]:
            shooting = True
            if len(shots) < 10:
                if position == 1:
                    shot = Shot(round(x + 45), round(y + 22), 4, (255, 0, 155), 1)
                else:
                    shot = Shot(round(x + 10), round(y + 22), 4, (255, 0, 155), -1)
                shots.append(shot)
        else:
            left = False
            right = False
            shooting = False
    run = exit_the_game(run)
    draw_game()
pygame.quit()
