import random
from settings import *
import player 
import math
import time
import main 

player_position_x = player.player.rect.x

class weirdo(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("main\GFX\boss.png").convert_alpha()
        self.base_boss_image = self.image
        self.rect = self.image.get_rect(center=(BOSS_START_POS_X, BOSS_START_POS_Y))
        self.speed = BOSS_SPEED
        self.last_shot_time = 0

    def update(self):
        self.rotate_towards_player()
        if main.clock %3 == 0:
            self.handle_bullet_shooting()
        angle = math.degrees(math.atan2(player.rect.x - self.rect.centery, player.rect.y - self.rect.centerx))
    def rotate_towards_player(self):
        angle = math.degrees(math.atan2(player_pos[1] - self.rect.centery, (player) - self.rect.centerx))
        self.image = pg.transform.rotate(self.base_boss_image, -angle)
        self.rect = self.image.get_rect(center=self.rect.center)


    def handle_bullet_shooting(self):
        print(random.choice(BOSS_BULLET_YES))
        if BOSS_BULLET_YES == 1: 
            curr_time = time.time()
            dx = player_pos[0] - self.rect.centerx
            dy = player_pos[1] - self.rect.centery
            if ( abs(dx) > 0 or abs(dy) > 0 ) and self.mag > 0 and curr_time - self.last_shot_time > BULLETS_SHOOTING_INTERVAL:
                self.last_shot_time = curr_time
        else:
            time.sleep(time)
            print(random.choice(BOSS_BULLET_YES))
                
