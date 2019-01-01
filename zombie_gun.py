import pygame
from GG import GG
from monster import Monster
from sprite import SKELETON_LEFT, MAIN_MENU_START_GAME, MAIN_MENU
from sprite import ZOMBIE_LVL_1
from sprite import BG
from sprite import SKULL
from sprite import COIN_1
from vars import clock
from vars import start_game
from vars import run, skeletons, zombies, shots, money
from window import Window

win = pygame.display.set_mode((450, 280))
pygame.init()
pygame.display.set_caption("Zombie Gun")
gg = GG(win)


def draw_game():
    win.blit(MAIN_MENU, (0, 0))
    if button:
        win.blit(MAIN_MENU_START_GAME, (0, 0))
    if start_game:
        win.blit(BG, (0, 0))
        win.blit(SKULL, (0, 0))
        win.blit(COIN_1, (60, 0))
        pygame.draw.rect(win, (255, 0, 0), (gg.x, gg.y, gg.width_hp_gg, 3))
        for zomb in zombies:
            zomb.draw()
        for sh in shots:
            sh.draw(win)
        for skelet in skeletons:
            skelet.draw()
        amount_money_or_total_killed(total_killed, 40, 15)
        amount_money_or_total_killed(money, 100, 15)
    pygame.display.update()


def amount_money_or_total_killed(amount, x, y):
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render(str(amount), True, (255, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (x, y)
    win.blit(textSurfaceObj, textRectObj)


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
                if monster.width_hp_monster > 0:
                    monster.width_hp_monster -= damage
        if monster.hp <= 0:
            monsters.remove(monster)
            total_killed += 1
            zobmie_killed += 1


def start_music():
    pygame.mixer.init()
    pygame.mixer.music.load("documents/XXXTentacion - Look at Me (minus).mp3")
    pygame.mixer.music.play(-1)


window = Window(win)
button_start_game = pygame.draw.rect(win, (0, 0, 0), (135, 60, 180, 18))
while run:
    clock.tick(120)
    pos = pygame.mouse.get_pos()
    if button_start_game.collidepoint(pos):
        button = True
    else:
        button = False

    pos = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    if button_start_game.collidepoint(pos) and pressed1:
        button_start_game = pygame.draw.rect(win, (0, 0, 0), (0, 0, 0, 0))
        start_game = True
        gg = GG(win)
        zombies = []
        skeletons = []
        shots = []
        total_killed = 0
        zobmie_killed = 0
        skeletons_killed = 0
        start_music()
        money = 0

    coordinates_zombie = [round(-20), round(200)]
    Zombie = Monster(win, coordinates_zombie, 150, 60, 20, ZOMBIE_LVL_1, 25, gg)

    coordinates_skeleton = [round(470), round(195)]
    Skeleton = Monster(win, coordinates_skeleton, 200, 80, 10, SKELETON_LEFT, 50, gg)

    if start_game:
        if not zombies:
            zombies.append(Zombie)
        if not skeletons:
            skeletons.append(Skeleton)

        for shot in shots:
            shot.movement(shots)

        for zombie in zombies:
            zombie.monster_movement(zombies, True)
            if zombie.x == zombie.gg.x:
                zombie.blow()
            if zombie.x == 100:
                zombies.append(Zombie)

        for skeleton in skeletons:
            skeleton.monster_movement(skeletons, False)
            if skeleton.x == skeleton.gg.x:
                skeleton.blow()
            if skeleton.x == 250:
                skeletons.append(Skeleton)

        killing_monsters(zombies, 20, 30, 29)
        killing_monsters(skeletons, 25, 0, 1)

        # if total_killed % 10 == 0 and total_killed // 10 != 0:
        #     if bonus_y < -50:
        #         bonus_x = randrange(20, 400)
        #         gift = Bonus(win, GIFT, bonus_x, bonus_y)
        # try:
        #     gift.gift_movement()
        #     gift.draw_bonus()
        #     coin = Coin(win, COIN, gift.bonus_x + 25, 260)
        #     money = coin.take_bonus(x, money)
        #     coin.draw_bonus()
        # except:
        #     pass
        start_game, button_start_game = gg.death(start_game, button_start_game)
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] and gg.x > 1) or (keys[pygame.K_a] and gg.x > 1):
            gg.move_left()
            gg.draw_left()

        elif (keys[pygame.K_RIGHT] and gg.x < 420) or (keys[pygame.K_d] and gg.x < 420):
            gg.move_right()
            gg.draw_right()

        elif keys[pygame.K_SPACE]:
            shots = gg.shooting(shots)
            gg.draw_shooting()
        else:
            gg.stand()

    run = exit_the_game(run)
    draw_game()
pygame.quit()
