import pygame as pg
import math
from sys import exit
from settings import *
import time
import player as john
import boss
from quizToPlay import *
pg.init()

FPS = 60
clock = pg.time.Clock()

player = john.Player()
bullets = pg.sprite.Group() 

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    player.update()
    bullets.update()
    screen.fill((105, 105, 105))

    player.display_remaining_bullets()
    screen.blit(player.image, player.rect)
    bullets.draw(screen)
    #print(pg.mouse.get_pos())
    pg.display.update()
    clock.tick(FPS)
