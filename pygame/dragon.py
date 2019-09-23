import pygame

width = 1024
height = 576


class Dragon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale((pygame.image.load('dragon_2.png')), (150, 80))
        self.rect = self.image.get_rect()
        self.rect.centerx = 70
        self.rect.bottom = height / 2
        self.speedy = 0

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -5
        if keystate[pygame.K_DOWN]:
            self.speedy = 5
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
