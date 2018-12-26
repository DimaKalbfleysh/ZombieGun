from random import randrange

import pygame

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
position = 1  # if left then 0 else 1
total_killed = 0
zobmie_killed = 0
skeletons_killed = 0
clock = pygame.time.Clock()
money = 0
shots = []
zombies = []
skeletons = []
run = True
gift_y = -100
gift_x = randrange(20, 400)
