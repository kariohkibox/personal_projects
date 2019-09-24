import pygame, random, os

width = 1024
height = 576

red = 250, 0, 0

enemy_images = []
enemy_list = ['demon_red.png', 'demon_yellow.png', 'demon_green.png', 'demon_blue.png']
for img in enemy_list:
    enemy_images.append(pygame.transform.scale(pygame.image.load(os.path.join("img", img)), (80, 80)))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(enemy_images)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width + 10, width + 200)
        self.rect.y = random.randrange(100, 500)
        self.speedx = random.randrange(7, 10)

    def update(self):
        self.rect.x -= self.speedx
        # respawn if it moves off the left side of screen
        if self.rect.right < -20:
            self.rect.x = random.randrange(width + 10, 1200)
            self.rect.y = random.randrange(100, 500)
            self.speedx = random.randrange(7, 10)