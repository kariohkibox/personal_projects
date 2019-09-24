import pygame, os

width = 1024
height = 576

powerup_time = 5000


class Dragon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale((pygame.image.load(os.path.join("img", "dragon_2.png"))), (150, 80))
        self.rect = self.image.get_rect()
        self.rect.centerx = 70
        self.rect.bottom = height / 2
        self.speedy = 0
        self.health = 100
        self.lives = 3
        self.power = 1
        self.power_time = pygame.time.get_ticks()
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

    def update(self):
        # unhides the player
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = 70
            self.rect.bottom = height / 2
        # timeout for powerups
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > powerup_time:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()
        # moves the player
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

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def hide(self):
        # hide the player temporarily
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (-200, height / 2)
