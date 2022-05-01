
from pygame import *

w = 700
h = 500

window = display.set_mode((w,h)) 
display.set_caption("Ping-Pong Game")


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y>0:
            self.rect.y -= 5
        if keys[K_s] and self.rect.y<420:
            self.rect.y += 5
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>0:
            self.rect.y -= 5
        if keys[K_DOWN] and self.rect.y<420:
            self.rect.y += 5

background = transform.scale(image.load("space.jpg"),(w,h))
player1 = Player("ufo.png",0,0,5,65,85)
player2 = Player("ufo.png",632,0,5,65,85)
ball = GameSprite("earth.png",335,230,5,30,30)

Game = True
clock = time.Clock()
FPS = 60
clock.tick(FPS)

ball_speed_x= 3
ball_speed_y = 3

finish = False

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSES!', True, (180,0,0))
lose2 = font1.render('PLAYER 2 LOSES!', True, (180,0,0))


while Game:
    window.blit(background,(0,0))
    player1.reset()
    player1.update_l()
    player2.reset()
    player2.update_r()
    ball.reset()
    if finish != True:
        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y
    if ball.rect.y > h - 50 or ball.rect.y < 0:
        ball_speed_y *= -1
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        ball_speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (240,240))
    if ball.rect.x > w-30:
        finish = True
        window.blit(lose2, (240,240))
    for e in event.get():
        if e.type == QUIT:
            Game = False
    display.update()
    clock.tick(FPS)
    