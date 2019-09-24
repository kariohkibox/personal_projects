import pygame, random, os

black = 0, 0, 0

powerup_images = {"health": pygame.image.load(os.path.join("img", "health_up.png")),
                  "weapon": pygame.image.load(os.path.join("img", "weapon_up.png"))}


class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(["health", "weapon"])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedx = 5

    def update(self):
        self.rect.x -= self.speedx
        # kill if it moves off the left of the screen
        if self.rect.right < -20:
            self.kill()
