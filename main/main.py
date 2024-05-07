import pygame as pg
import math
from sys import exit
from settings import *
import time

pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()
font = pg.font.Font(None, 36)

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("main/GFX/player.png").convert_alpha()
        self.base_player_image = self.image
        self.rect = self.image.get_rect(center=(PLAYER_START_POS_X, PLAYER_START_POS_Y))
        self.speed = PLAYER_SPEED
        self.mag = BULLETS_MAG_SIZE
        self.last_shot_time = 0

    def update(self):
        self.handle_input()
        self.rotate_towards_mouse()
        self.handle_bullet_shooting()

    def handle_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= self.speed
        if keys[pg.K_s]:
            self.rect.y += self.speed
        if keys[pg.K_a]:
            self.rect.x -= self.speed
        if keys[pg.K_d]:
            self.rect.x += self.speed
        if keys[pg.K_r]:
            self.mag = BULLETS_MAG_SIZE
        self.rect.clamp_ip(screen.get_rect())  

    def rotate_towards_mouse(self):
        mouse_pos = pg.mouse.get_pos()
        angle = math.degrees(math.atan2(mouse_pos[1] - self.rect.centery, mouse_pos[0] - self.rect.centerx))
        self.image = pg.transform.rotate(self.base_player_image, -angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def handle_bullet_shooting(self):
        if pg.mouse.get_pressed()[0]: 
            curr_time = time.time()
            mouse_pos = pg.mouse.get_pos()
            dx = mouse_pos[0] - self.rect.centerx
            dy = mouse_pos[1] - self.rect.centery
            if ( abs(dx) > 0 or abs(dy) > 0 ) and self.mag > 0 and curr_time - self.last_shot_time > BULLETS_SHOOTING_INTERVAL:
                self.last_shot_time = curr_time
                new_bullet = Bullet(self.rect.centerx, self.rect.centery, dx, dy)
                bullets.add(new_bullet)  
                self.mag -=1

    def display_remaining_bullets(self):
        text = "Remaining bullets: {0}".format(self.mag)
        text_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, (0, 0))

class Bullet(pg.sprite.Sprite):
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

player = Player()
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
