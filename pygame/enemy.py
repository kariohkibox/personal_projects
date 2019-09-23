import pygame, random

width = 1024
height = 576

red = 250, 0, 0


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 20))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width + 10, width + 200)
        self.rect.y = random.randrange(100, 500)
        self.speedx = random.randrange(7, 10)

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.right < -20:
            self.rect.x = random.randrange(width + 10, 1200)
            self.rect.y = random.randrange(100, 500)
            self.speedx = random.randrange(7, 10)