window = display.set_mode((700, 500))
from pygame import *
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
        if pressed[K_a] and self.rect.x + self.speed > 0:
            self.rect.x -= self.speed
        elif pressed[K_d] and self.rect.x + self.speed <  650:
            self.rect.x += self.speed
        if self.rect.x  > 650:
            self.rect.x -= self.speed
        if self.rect.x  < -50:
            self.rect.x += self.speed
    def update_2(self):
        pressed = key.get_pressed()
        if pressed[K_LEFT] and self.rect.x + self.speed > 0:
            self.rect.x -= self.speed
        elif pressed[K_RIGHT] and self.rect.x + self.speed <  650:
            self.rect.x += self.speed
        if self.rect.x  > 650:
            self.rect.x -= self.speed
        if self.rect.x  < -50:
            self.rect.x += self.speed