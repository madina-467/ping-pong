from pygame import *
from random import randint
from time import time as tm

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, w, h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed() 
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 595:
            self.rect.x += self.speed
    def Fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)



window = display.set_mode((700, 500))
display.set_caption('Ping-pong')
background = transform.scale(image.load('fon.jpeg'), (700, 500))

clock = time.Clock()
FPS = 60


font.init()
font_1 = font.SysFont('Arial', 70)
font_2 = font.SysFont('Arial', 30)
win = font_1.render('YOU WIN!', True, (255, 215, 0))

lose = font_1.render('YOU LOSE!', True, (255, 215, 0))


player = Player('roketka.png', 5, 400, 80, 100, 10)

finish = False

lost = 0
skor = 0


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
               
    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        player.reset()
    

    display.update()
    clock.tick(FPS)
