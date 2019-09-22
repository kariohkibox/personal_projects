import sys, pygame, random
import dragon, enemy

size = width, height = 1024, 576
black = 10, 10, 10
fps = 30

pygame.init()
pygame.display.set_caption("dragon shmup")
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = dragon.Dragon()
all_sprites.add(player)
for i in range(5):
    e = enemy.Enemy()
    all_sprites.add(e)
    enemies.add(e)

while 1:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    all_sprites.update()

    screen.fill(black)
    all_sprites.draw(screen)
    pygame.display.flip()
