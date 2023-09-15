
from pygame import *
window = display.set_mode((1500, 500))
clock = time.Clock()
window.fill((100,100,100))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,w,h):
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
        pressed = key.get_pressed()
        if pressed[K_w]:
            self.rect.y -= self.speed
        elif pressed[K_s]:
            self.rect.y += self.speed
        if self.rect.y  > 450:
            self.rect.y -= self.speed
        if self.rect.y  < -50:
            self.rect.y += self.speed
    def update_2(self):
        pressed = key.get_pressed()
        if pressed[K_UP]: 
            self.rect.y -= self.speed
        elif pressed[K_DOWN]:
            self.rect.y += self.speed
        if self.rect.y  > 450:
            self.rect.y -= self.speed
        if self.rect.y  < -50:
            self.rect.y += self.speed
heroleft = Player('racket.png', 50, 400, 10, 50,100)
heroright = Player('racket.png', 1400, 400, 10, 50,100)
game = True

while game:
    window.fill((100,100,100))
    for e in event.get():
        if e.type == QUIT:
            quit()

    heroright.reset()
    heroright.update_2()
    heroleft.reset()
    heroleft.update()
    display.update()
    clock.tick(60)