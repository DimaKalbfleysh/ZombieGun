import pygame  # окно проигрыша
import time
import random

pygame.init()

win = pygame.display.set_mode((450, 280))
pygame.display.set_caption("Zombie Gan")
clock = pygame.time.Clock()
damageGG = [pygame.image.load('damageGG_left.png'),
            pygame.image.load('damageGG_right.png')]
Bg = pygame.image.load('bg.png')
Main_menu = pygame.image.load('main menu.png')
Main_menu1 = pygame.image.load('main menu1.png')
Main_menu2 = pygame.image.load('main menu2.png')
Main_menu3 = pygame.image.load('main menu3.png')
Gift = pygame.image.load('gift.png')
stand = [pygame.image.load('gg_lift1.png'),
         pygame.image.load('gg_right1.png')]
Shooting = [pygame.image.load('shooting_left.png'),
            pygame.image.load('shooting_right.png')]
Death_left = [pygame.image.load('death_left1.png'),
              pygame.image.load('death_left2.png'),
              pygame.image.load('death_left3.png'),
              pygame.image.load('death_left4.png')]
ggRight = [pygame.image.load('gg_right1.png'),
           pygame.image.load('gg_right2.png'),
           pygame.image.load('gg_right3.png'),
           pygame.image.load('gg_right4.png')]

ggLift = [pygame.image.load('gg_lift1.png'),
          pygame.image.load('gg_lift2.png'),
          pygame.image.load('gg_lift3.png'),
          pygame.image.load('gg_lift4.png')]

Zombie_lvl1 = [pygame.image.load('zombie1.png'),
               pygame.image.load('zombie2.png'),
               pygame.image.load('zombie3.png')]
Zombie_lvl2 = [pygame.image.load('zombie1_lvl2.png'),
               pygame.image.load('zombie2_lvl2.png'),
               pygame.image.load('zombie3_lvl2.png'),
               pygame.image.load('zombie4_lvl2.png'),
               pygame.image.load('zombie5_lvl2.png')]

Skeleton_left = [pygame.image.load('skeleton1.png'),
                 pygame.image.load('skeleton2.png'),
                 pygame.image.load('skeleton3.png')]
Coin = pygame.image.load('money.png')
Coin1 = pygame.image.load('money1.png')
Skull = pygame.image.load('skull.png')
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


class Shot():
    def __init__(self, shot_x, shot_y, radius, color, facing):
        self.shot_x = shot_x
        self.shot_y = shot_y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 1 * facing

    def draw_shot(self, win):
        pygame.draw.circle(win, self.color, (self.shot_x, self.shot_y), self.radius)


class Skeleton():
    def __init__(self, skeleton_x, skeleton_y, xp, width, height):
        self.skeleton_x = skeleton_x
        self.skeleton_y = skeleton_y
        self.xp = xp
        self.width = width
        self.height = height

    def draw(self, win):
        global anim2
        if anim2 + 1 >= 30:
            anim2 = 0
        pygame.draw.rect(win, (255, 0, 0), (self.skeleton_x - 15, self.skeleton_y, self.width, self.height))
        win.blit(Skeleton_left[anim2 // 10], (self.skeleton_x, self.skeleton_y))


class Zombie():
    def __init__(self, zombie_x, zombie_y, xp, width, height, level):
        self.zombie_x = zombie_x
        self.zombie_y = zombie_y
        self.xp = xp
        self.width = width
        self.height = height
        self.level = level

    def draw(self, win):
        global anim1
        if anim1 + 1 >= 60:
            anim1 = 0

        if lvl2:
            pygame.draw.rect(win, (255, 0, 0), (self.zombie_x + 5, self.zombie_y, self.width, self.height))
            win.blit(Zombie_lvl2[anim1 // 12], (self.zombie_x, self.zombie_y))
            fontObj = pygame.font.Font('freesansbold.ttf', 15)
            textSurfaceObj = fontObj.render('lvl' + str(self.level), True, (128, 128, 128))
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (self.zombie_x + 23, self.zombie_y - 15)
            win.blit(textSurfaceObj, textRectObj)
        else:
            pygame.draw.rect(win, (255, 0, 0), (self.zombie_x, self.zombie_y, self.width, self.height))
            win.blit(Zombie_lvl1[anim1 // 20], (self.zombie_x, self.zombie_y))
            fontObj = pygame.font.Font('freesansbold.ttf', 15)
            textSurfaceObj = fontObj.render('lvl' + str(self.level), True, (128, 128, 128))
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (self.zombie_x + 23, self.zombie_y - 15)
            win.blit(textSurfaceObj, textRectObj)


def draw_window():
    global anim
    global anim1
    global k
    global anim2
    global death_zombie
    global coin_x
    global coin_y
    win.blit(Main_menu, (0, 0))
    if button1:
        win.blit(Main_menu1, (0, 0))
    if start_game:
        win.blit(Bg, (0, 0))
        win.blit(Skull, (0, 0))
        win.blit(Coin1, (60, 0))
        if anim + 1 >= 32:
            anim = 0
        if left:
            win.blit(ggLift[anim // 8], (x, y))
            anim += 1

        elif right:
            win.blit(ggRight[anim // 8], (x, y))
            anim += 1

        elif shooting:
            if k == -1:
                win.blit(Shooting[0], (x, y))
            else:
                win.blit(Shooting[1], (x, y))
        elif damage:
            if k == -1:
                win.blit(damageGG[0], (x, y))
            else:
                win.blit(damageGG[1], (x, y))

        else:
            if k == -1:
                win.blit(stand[0], (x, y))
            else:
                win.blit(stand[1], (x, y))
        if gift:
            win.blit(Gift, (gift_x, gift_y))
        if coin:
            win.blit(Coin, (coin_x, coin_y))

        pygame.draw.rect(win, (255, 0, 0), (x, y, width, 3))
        for zombie in zombies:
            zombie.draw(win)
            anim1 += 1
        for shot in shots:
            shot.draw_shot(win)
        for skeleton in skeletons:
            skeleton.draw(win)
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
            if zombie.zombie_x < 450:
                zombie.zombie_x += 1
            else:
                zombies.pop(zombies.index(zombie))
            if lvl2:
                if zombie.zombie_x == 80:
                    zombies.append(Zombie(round(x1), round(187), 250, 60, 3, 2))
            else:
                if zombie.zombie_x == 100:
                    zombies.append(Zombie(round(x1), round(200), 100, 40, 3, 1))
            if lvl2:
                if zombie.zombie_x == x:
                    damage = True
                    if width > 0:
                        GG_xp -= 50
                        width -= 20
                        print(GG_xp)
            else:
                if zombie.zombie_x == x:
                    damage = True
                    if width > 0:
                        GG_xp -= 25
                        width -= 10
                        print(GG_xp)
            if zombie.zombie_x == x + 10 or zombie.zombie_x == x + 9 or zombie.zombie_x == x + 8:
                damage = False
            if width == 0 and GG_xp <= 0:
                pygame.mixer.music.stop()
                start_game = False

        for skeleton in skeletons:
            if skeleton.skeleton_x > 1:
                skeleton.skeleton_x -= 1
            else:
                skeletons.pop(skeletons.index(skeleton))
            if skeleton.skeleton_x == 250:
                skeletons.append(Skeleton(round(470), round(195), 200, 80, 3))
            if skeleton.skeleton_x == x + 10:
                damage = True
                if width > 0:
                    GG_xp -= 50
                    width -= 20
                    print(GG_xp)

            if skeleton.skeleton_x == x or skeleton.skeleton_x == x - 1 or skeleton.skeleton_x == x - 2:
                damage = False
            if width <= 0 and GG_xp <= 0:
                pygame.mixer.music.stop()
                start_game = False

        for zombie in zombies:
            for shot in shots:
                if zombie.zombie_x + 30 == shot.shot_x or zombie.zombie_x + 29 == shot.shot_x:
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
                if skeleton.skeleton_x == shot.shot_x or skeleton.skeleton_x + 1 == shot.shot_x:
                    skeleton.xp -= 50
                    shots.pop(shots.index(shot))
                    if skeleton.width > 0:
                        skeleton.width -= 25
            if skeleton.xp == 0:
                skeletons.pop(skeletons.index(skeleton))
                a += 1
                w += 1

        Z = a % 10
        if Z == 9 and coin == False:
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
                zombies.append(Zombie(round(x1), round(187), 250, 60, 3, 2))
        else:
            if len(zombies) < 1:
                zombies.append(Zombie(round(x1), round(200), 100, 40, 3, 1))
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

    draw_window()
pygame.quit()