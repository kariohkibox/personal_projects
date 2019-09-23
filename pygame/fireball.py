import pygame, os

width = 1024
height = 576

yellow = (210, 210, 0)


class Fireball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.speedx = 10

    def update(self):
        self.rect.x += self.speedx
        # kill if it moves off the right of the screen
        if self.rect.left > width:
            self.kill()
