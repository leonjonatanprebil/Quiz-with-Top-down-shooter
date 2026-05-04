import pygame as pg
import math
from sys import exit
from settings import *
import time
from character import Player, player_bullets
import boss
from quizToPlay import *
root = tk.Tk()
app = Quiz(root)
root.mainloop()

pg.init()

FPS = 60
clock = pg.time.Clock()

bullets = pg.sprite.Group() 

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
p = Player()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    p.update()
    p.rect.clamp_ip(screen.get_rect())  
    bullets.update()
    screen.fill((105, 105, 105))

    #p.display_remaining_bullets()
    screen.blit(p.image, p.rect)
    bullets.draw(screen)
    #print(pg.mouse.get_pos())
    pg.display.update()
    clock.tick(FPS)
