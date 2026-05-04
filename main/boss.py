import random
from settings import *
from character.py import main.character as character 
import math
import time
import main 
import pygame as pg

bullets = pg.sprite.Group() 

class weirdo(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("main\GFX\boss.png").convert_alpha()
        self.base_boss_image = self.image
        self.rect = self.image.get_rect(center=(BOSS_START_POS_X, BOSS_START_POS_Y))
        self.speed = BOSS_SPEED

    def update(self):
        self.rotate_towards_player()
        self.handle_bullet_shooting()
        angle = math.degrees(math.atan2(character.rect.x - self.rect.centery, character.rect.y - self.rect.centerx))
    def rotate_towards_player(self):
        angle = math.degrees(math.atan2(character.rect.x - self.rect.centery, (character.rect.y) - self.rect.centerx))
        self.image = pg.transform.rotate(self.base_boss_image, -angle)
        self.rect = self.image.get_rect(center=self.rect.center)


    def handle_bullet_shooting(self):
        
        if main.clock %3 == 0:
            curr_time = time.time()
            dx = self.rect.x - self.rect.centerx
            dy = self.rect.y - self.rect.centery
            new_bullet = boss_bullets(self.rect.centerx, self.rect.centery, dx, dy)
            bullets.add(new_bullet)
        else:
            
            print(random.choice(BOSS_BULLET_YES))

class boss_bullets(pg.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        super().__init__()
        self.image = pg.Surface((5, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.pos = pg.math.Vector2(x, y)
        self.dir = pg.math.Vector2(dx, dy).normalize()
        self.speed = BULLET_SPEED

    def update(self):
        self.pos += self.dir * self.speed
        self.rect.center = (round(self.pos.x), round(self.pos.y))
        
        if not self.rect.colliderect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT):
            self.kill()
                
