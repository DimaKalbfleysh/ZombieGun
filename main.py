import pygame
from hero import Hero
from monster import *
from sprite import *
from vars import *
from window import Window

win = pygame.display.set_mode((450, 280))
pygame.init()
pygame.display.set_caption("Zombie Gun")
hero = Hero(win)
button_start_game = pygame.draw.rect(win, (0, 0, 0), (135, 60, 180, 18))


def draw_game():
    win.blit(MAIN_MENU, (0, 0))
    if button:
        win.blit(MAIN_MENU_START_GAME, (0, 0))
    if start_game:
        win.blit(BG, (0, 0))
        win.blit(SKULL, (0, 0))
        win.blit(COIN_1, (60, 0))
        pygame.draw.rect(win, (255, 0, 0), (hero.x, hero.y, hero.width_hp, 3))
        for zomb in zombies:
            zomb.draw()
        for sh in shells:
            sh.draw(win)
        for skelet in skeletons:
            skelet.draw()
        draw_amount_money_or_total_killed(total_killed, 40, 18)
        draw_amount_money_or_total_killed(money, 100, 18)
    pygame.display.flip()


def draw_amount_money_or_total_killed(amount, x, y):
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render(str(amount), True, (255, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (x, y)
    win.blit(textSurfaceObj, textRectObj)


def killing_monsters(monsters, damage, *args):
    global total_killed
    for monster in monsters:
        for sh in shells:
            if monster.x + args[0] == sh.x or monster.x + args[1] == sh.x:
                monster.hp -= 50
                shells.remove(sh)
                if monster.width_hp > 0:
                    monster.width_hp -= damage
        if monster.hp <= 0:
            monsters.remove(monster)
            total_killed += 1


window = Window(win, hero)
while run:
    clock.tick(120)
    pos = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    if button_start_game.collidepoint(pos):
        button = True
    else:
        button = False

    if button_start_game.collidepoint(pos) and pressed1:
        hero = Hero(win)
        window = Window(win, hero)
        button_start_game = pygame.draw.rect(win, (0, 0, 0), (0, 0, 0, 0))
        start_game = True
        zombies = []
        skeletons = []
        shells = []
        total_killed = 0
        window.start_music()
        money = 0

    coordinates_zombie = [round(-20), round(200)]
    zombie_ = Zombie(win, coordinates_zombie, ZOMBIE_LVL_1, 150, 10, 25, hero, 1)

    coordinates_skeleton = [round(470), round(195)]
    skeleton_ = Skeleton(win, coordinates_skeleton, SKELETON_LEFT, 200, 10, 50, hero, -1)

    if start_game:
        if not zombies:
            zombies.append(zombie_)
        if not skeletons:
            skeletons.append(skeleton_)

        for shell in shells:
            shell.move(shells)

        for zombie in zombies:
            zombie.move(zombies)
            if zombie.x == zombie.main_character.x:
                zombie.blow()
            if zombie.x == 100:
                zombies.append(zombie_)

        for skeleton in skeletons:
            skeleton.move(skeletons)
            if skeleton.x == skeleton.main_character.x:
                skeleton.blow()
            if skeleton.x == 300:
                skeletons.append(skeleton_)

        killing_monsters(zombies, 20, 30, 29)
        killing_monsters(skeletons, 25, 0, 1)
        hero.is_death()
        start_game = window.get_start_game()
        button_start_game = window.get_button_start_game()

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] and hero.x > 1) or (keys[pygame.K_a] and hero.x > 1):
            hero.move(-2, 0)
            hero.draw_walking(GG_LEFT)

        elif (keys[pygame.K_RIGHT] and hero.x < 420) or (keys[pygame.K_d] and hero.x < 420):
            hero.move(2, 1)
            hero.draw_walking(GG_RIGHT)

        elif keys[pygame.K_SPACE]:
            shells = hero.shooting(shells)
            hero.draw_shooting()
        else:
            hero.draw_standing()

    window.stop_music()
    draw_game()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
