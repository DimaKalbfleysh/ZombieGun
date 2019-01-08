import pygame
from bonus import Coin
from hero import Hero
from monster import *
from sprite import *
from game import Game

win = pygame.display.set_mode((450, 280))
hero = Hero(win)
game = Game(win, hero)


def draw_game():
    win.blit(MAIN_MENU, (0, 0))
    if game.button:
        win.blit(MAIN_MENU_START_GAME, (0, 0))
    if game.start_game:
        win.blit(BG, (0, 0))
        win.blit(SKULL, (0, 0))
        win.blit(COIN_1, (60, 0))
        pygame.draw.rect(win, (255, 0, 0), (hero.x, hero.y, hero.width_hp, 3))
        for zomb in game.zombies:
            zomb.draw()
        for sh in game.shells:
            sh.draw(win)
        for skelet in game.skeletons:
            skelet.draw()
        draw_amount_money_or_total_killed(game.total_killed, 40, 18)
        draw_amount_money_or_total_killed(game.money, 100, 18)
    pygame.display.flip()


def draw_amount_money_or_total_killed(amount, x, y):
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render(str(amount), True, (255, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (x, y)
    win.blit(textSurfaceObj, textRectObj)


def killing_monsters(monsters, damage, *args):
    for monster in monsters:
        for sh in game.shells:
            if monster.x + args[0] == sh.x or monster.x + args[1] == sh.x:
                monster.hp -= 50
                game.shells.remove(sh)
                if monster.width_hp > 0:
                    monster.width_hp -= damage
        if monster.hp <= 0:
            monsters.remove(monster)
            game.total_killed += 1


coordinates_skeleton = [round(470), round(195)]
coordinates_zombie = [round(-20), round(200)]
while game.run:
    game.clock.tick(120)
    pos = pygame.mouse.get_pos()
    pressed1, _, _ = pygame.mouse.get_pressed()
    if game.button_start_game.collidepoint(pos):
        game.button = True
    else:
        game.button = False

    if game.button_start_game.collidepoint(pos) and pressed1:
        hero = Hero(win)
        game = Game(win, hero)
        game.start_game = True
        game.start_music()

    zombie_ = Zombie(win, coordinates_zombie, ZOMBIE_LVL_1, 150, 10, 25, hero, game)
    skeleton_ = Skeleton(win, coordinates_skeleton, SKELETON_LEFT, 200, 10, 50, hero, game)

    if game.start_game:
        if not game.zombies:
            game.zombies.append(zombie_)
        if not game.skeletons:
            game.skeletons.append(skeleton_)

        for shell in game.shells:
            shell.move(game.shells)

        for zombie in game.zombies:
            zombie.move()
            zombie.death()
            if zombie.x == zombie.hero.x:
                zombie.blow()
            if zombie.x == 100:
                game.zombies.append(zombie_)

        for skeleton in game.skeletons:
            skeleton.move()
            skeleton.death()
            if skeleton.x == skeleton.hero.x:
                skeleton.blow()
            if skeleton.x == 300:
                game.skeletons.append(skeleton_)

        if game.total_killed % 10 == 0 and game.total_killed // 10 != 0 and len(game.coins) < 1:
            bonus_ = Coin(win, COIN, hero, game)
            game.coins.append(bonus_)

        for coin in game.coins:
            coin.draw_gift()
            coin.gift_movement()
            coin.take_bonus()

        killing_monsters(game.zombies, 25, 30, 29)
        killing_monsters(game.skeletons, 25, 0, 1)
        hero.is_death()
        game.get_start_game()
        game.get_button_start_game()

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] and hero.x > 1) or (keys[pygame.K_a] and hero.x > 1):
            hero.move(-2, 0)
            hero.draw_walking(GG_LEFT)

        elif (keys[pygame.K_RIGHT] and hero.x < 420) or (keys[pygame.K_d] and hero.x < 420):
            hero.move(2, 1)
            hero.draw_walking(GG_RIGHT)

        elif keys[pygame.K_SPACE]:
            hero.shooting(game.shells)
            hero.draw_shooting()
        else:
            hero.draw_standing()

    game.stop_music()
    game.stop_game()
    draw_game()

pygame.quit()
