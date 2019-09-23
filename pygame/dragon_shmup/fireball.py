import pygame, os

width = 1024
height = 576

yellow = (210, 210, 0)


class Fireball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale((pygame.image.load(os.path.join("img", "fireball.png"))), (42, 28))
        self.rect = self.image.get_rect()
        self.speedx = 10

    def update(self):
        self.rect.x += self.speedx
        # kill if it moves off the right of the screen
        if self.rect.left > width:
            self.kill()
