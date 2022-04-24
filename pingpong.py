
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

while Game:
    window.blit(background,(0,0))
    player1.reset()
    player1.update_l()
    player2.reset()
    player2.update_r()
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
            Game = False
    display.update()
    clock.tick(FPS)
    