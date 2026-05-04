import pygame as pg
import math
from sys import exit
from settings import *
import time
from character import Player, player_bullets
import boss


pg.init()

FPS = 60
clock = pg.time.Clock()

bullets = pg.sprite.Group() 
p = Player()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    p.update()
    bullets.update()
    screen.fill((105, 105, 105))

    Player.display_remaining_bullets()
    Player.blit(p.image, p.rect)
    bullets.draw(screen)
    #print(pg.mouse.get_pos())
    pg.display.update()
    clock.tick(FPS)
